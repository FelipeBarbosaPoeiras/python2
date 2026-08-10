import os
from functools import wraps

import requests
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database as db

app = Flask(__name__)

# 7) Segurança e boas práticas -------------------------------------------
# Em produção, defina a variável de ambiente SECRET_KEY com um valor forte
# e aleatório. Aqui usamos um valor de fallback apenas para desenvolvimento.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-troque-isso")
app.config["DEBUG"] = os.environ.get("FLASK_DEBUG", "0") == "1"  # DEBUG=False em produção

STATUS_VALIDOS = {"pendente", "andamento", "concluida"}


# ---------------------------------------------------------------------------
# Autenticação
# ---------------------------------------------------------------------------

def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Faça login para continuar.", "warning")
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped


@app.route("/")
def index():
    if "usuario_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        # Validação simples de dados de entrada
        if not nome or not email or not senha:
            flash("Preencha todos os campos.", "danger")
            return render_template("registro.html")
        if len(senha) < 6:
            flash("A senha deve ter pelo menos 6 caracteres.", "danger")
            return render_template("registro.html")

        senha_hash = generate_password_hash(senha)
        sucesso = db.criar_usuario(nome, email, senha_hash)
        if not sucesso:
            flash("Este e-mail já está cadastrado.", "danger")
            return render_template("registro.html")

        flash("Cadastro realizado com sucesso! Faça login.", "success")
        return redirect(url_for("login"))

    return render_template("registro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        usuario = db.buscar_usuario_por_email(email)
        # check_password_hash evita expor se o e-mail existe ou não
        if usuario and check_password_hash(usuario["senha"], senha):
            session.clear()
            session["usuario_id"] = usuario["id"]
            session["usuario_nome"] = usuario["nome"]
            return redirect(url_for("dashboard"))

        flash("E-mail ou senha inválidos.", "danger")
        return render_template("login.html")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("login"))


# ---------------------------------------------------------------------------
# Dashboard principal (listagem, filtro e frase motivacional)
# ---------------------------------------------------------------------------

@app.route("/dashboard")
@login_required
def dashboard():
    status_filtro = request.args.get("status", "todas")
    tarefas = db.listar_tarefas(session["usuario_id"], status_filtro)

    # 4) Integração com API externa: frase motivacional diária
    frase = None
    try:
        resposta = requests.get("https://api.adviceslip.com/advice", timeout=3)
        if resposta.ok:
            frase = resposta.json().get("slip", {}).get("advice")
    except requests.RequestException:
        frase = None  # segue sem quebrar a página caso a API externa falhe

    return render_template(
        "dashboard.html",
        tarefas=tarefas,
        frase=frase,
        status_filtro=status_filtro,
    )


# ---------------------------------------------------------------------------
# CRUD de tarefas
# ---------------------------------------------------------------------------

@app.route("/nova_tarefa", methods=["GET", "POST"])
@login_required
def nova_tarefa():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        status = request.form.get("status", "pendente")

        if not titulo:
            flash("O título é obrigatório.", "danger")
            return render_template("nova_tarefa.html")
        if status not in STATUS_VALIDOS:
            status = "pendente"

        db.criar_tarefa(titulo, descricao, status, session["usuario_id"])
        flash("Tarefa criada com sucesso!", "success")
        return redirect(url_for("dashboard"))

    return render_template("nova_tarefa.html")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar(id):
    tarefa = db.buscar_tarefa(id, session["usuario_id"])
    if tarefa is None:
        flash("Tarefa não encontrada.", "danger")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        status = request.form.get("status", "pendente")

        if not titulo:
            flash("O título é obrigatório.", "danger")
            return render_template("editar_tarefa.html", tarefa=tarefa)
        if status not in STATUS_VALIDOS:
            status = "pendente"

        db.atualizar_tarefa(id, session["usuario_id"], titulo, descricao, status)
        flash("Tarefa atualizada com sucesso!", "success")
        return redirect(url_for("dashboard"))

    return render_template("editar_tarefa.html", tarefa=tarefa)


@app.route("/excluir/<int:id>", methods=["POST"])
@login_required
def excluir(id):
    db.excluir_tarefa(id, session["usuario_id"])
    flash("Tarefa excluída.", "info")
    return redirect(url_for("dashboard"))


@app.route("/concluir/<int:id>", methods=["POST"])
@login_required
def concluir(id):
    db.atualizar_status_tarefa(id, session["usuario_id"], "concluida")
    flash("Tarefa marcada como concluída!", "success")
    return redirect(url_for("dashboard"))


# ---------------------------------------------------------------------------
# 8) Filtro de tarefas por status via AJAX (rota que retorna JSON)
# ---------------------------------------------------------------------------

@app.route("/api/tarefas", methods=["GET", "POST"])
@login_required
def api_tarefas():
    """GET: lista tarefas (com filtro opcional ?status=).
    POST: cria uma nova tarefa (desafio avançado - versão REST)."""
    if request.method == "GET":
        status_filtro = request.args.get("status", "todas")
        tarefas = db.listar_tarefas(session["usuario_id"], status_filtro)
        return jsonify([dict(t) for t in tarefas])

    dados = request.get_json(silent=True) or {}
    titulo = (dados.get("titulo") or "").strip()
    descricao = (dados.get("descricao") or "").strip()
    status = dados.get("status", "pendente")

    if not titulo:
        return jsonify({"erro": "O título é obrigatório."}), 400
    if status not in STATUS_VALIDOS:
        status = "pendente"

    novo_id = db.criar_tarefa(titulo, descricao, status, session["usuario_id"])
    tarefa = db.buscar_tarefa(novo_id, session["usuario_id"])
    return jsonify(dict(tarefa)), 201


@app.route("/api/tarefas/<int:id>", methods=["GET", "PUT", "DELETE"])
@login_required
def api_tarefa_detalhe(id):
    """Desafio avançado: versão REST completa (GET, PUT, DELETE)."""
    tarefa = db.buscar_tarefa(id, session["usuario_id"])
    if tarefa is None:
        return jsonify({"erro": "Tarefa não encontrada."}), 404

    if request.method == "GET":
        return jsonify(dict(tarefa))

    if request.method == "PUT":
        dados = request.get_json(silent=True) or {}
        titulo = (dados.get("titulo") or tarefa["titulo"]).strip()
        descricao = dados.get("descricao", tarefa["descricao"])
        status = dados.get("status", tarefa["status"])
        if status not in STATUS_VALIDOS:
            status = tarefa["status"]

        db.atualizar_tarefa(id, session["usuario_id"], titulo, descricao, status)
        tarefa_atualizada = db.buscar_tarefa(id, session["usuario_id"])
        return jsonify(dict(tarefa_atualizada))

    db.excluir_tarefa(id, session["usuario_id"])
    return jsonify({"mensagem": "Tarefa excluída."}), 200


# ---------------------------------------------------------------------------
# 10) Dashboard de progresso
# ---------------------------------------------------------------------------
# Observação de projeto: o enunciado pede uma rota "/dashboard" tanto no
# item 5 (painel de tarefas) quanto no item 10 (painel de progresso), o que
# gera conflito de nomes. Aqui /dashboard segue o item 5 (lista de tarefas)
# e a página de progresso do item 10 foi implementada em /progresso.

@app.route("/progresso")
@login_required
def progresso():
    return render_template("progresso.html")


@app.route("/api/progresso")
@login_required
def api_progresso():
    contagem = db.contar_tarefas_por_status(session["usuario_id"])
    return jsonify(contagem)


if __name__ == "__main__":
    db.init_db()
    app.run(debug=app.config["DEBUG"])
