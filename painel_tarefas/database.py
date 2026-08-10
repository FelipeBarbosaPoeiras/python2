import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "instance" / "banco.db"


def get_conn():
    """Abre uma conexão com o banco SQLite, retornando linhas como dicionários."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Cria as tabelas usuarios e tarefas caso ainda não existam."""
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = get_conn()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT NOT NULL DEFAULT 'pendente',
            usuario_id INTEGER NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE
        )
        """
    )
    conn.commit()
    conn.close()


# ---------- Usuários ----------

def criar_usuario(nome, email, senha_hash):
    conn = get_conn()
    try:
        conn.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
            (nome, email, senha_hash),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def buscar_usuario_por_email(email):
    conn = get_conn()
    usuario = conn.execute(
        "SELECT * FROM usuarios WHERE email = ?", (email,)
    ).fetchone()
    conn.close()
    return usuario


def buscar_usuario_por_id(usuario_id):
    conn = get_conn()
    usuario = conn.execute(
        "SELECT * FROM usuarios WHERE id = ?", (usuario_id,)
    ).fetchone()
    conn.close()
    return usuario


# ---------- Tarefas ----------

def listar_tarefas(usuario_id, status=None):
    conn = get_conn()
    if status and status != "todas":
        tarefas = conn.execute(
            "SELECT * FROM tarefas WHERE usuario_id = ? AND status = ? ORDER BY id DESC",
            (usuario_id, status),
        ).fetchall()
    else:
        tarefas = conn.execute(
            "SELECT * FROM tarefas WHERE usuario_id = ? ORDER BY id DESC",
            (usuario_id,),
        ).fetchall()
    conn.close()
    return tarefas


def buscar_tarefa(tarefa_id, usuario_id):
    conn = get_conn()
    tarefa = conn.execute(
        "SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?",
        (tarefa_id, usuario_id),
    ).fetchone()
    conn.close()
    return tarefa


def criar_tarefa(titulo, descricao, status, usuario_id):
    conn = get_conn()
    cur = conn.execute(
        "INSERT INTO tarefas (titulo, descricao, status, usuario_id) VALUES (?, ?, ?, ?)",
        (titulo, descricao, status, usuario_id),
    )
    conn.commit()
    novo_id = cur.lastrowid
    conn.close()
    return novo_id


def atualizar_tarefa(tarefa_id, usuario_id, titulo, descricao, status):
    conn = get_conn()
    conn.execute(
        """UPDATE tarefas SET titulo = ?, descricao = ?, status = ?
           WHERE id = ? AND usuario_id = ?""",
        (titulo, descricao, status, tarefa_id, usuario_id),
    )
    conn.commit()
    conn.close()


def atualizar_status_tarefa(tarefa_id, usuario_id, status):
    conn = get_conn()
    conn.execute(
        "UPDATE tarefas SET status = ? WHERE id = ? AND usuario_id = ?",
        (status, tarefa_id, usuario_id),
    )
    conn.commit()
    conn.close()


def excluir_tarefa(tarefa_id, usuario_id):
    conn = get_conn()
    conn.execute(
        "DELETE FROM tarefas WHERE id = ? AND usuario_id = ?",
        (tarefa_id, usuario_id),
    )
    conn.commit()
    conn.close()


def contar_tarefas_por_status(usuario_id):
    conn = get_conn()
    linhas = conn.execute(
        """SELECT status, COUNT(*) as total FROM tarefas
           WHERE usuario_id = ? GROUP BY status""",
        (usuario_id,),
    ).fetchall()
    conn.close()
    contagem = {"pendente": 0, "andamento": 0, "concluida": 0}
    for linha in linhas:
        contagem[linha["status"]] = linha["total"]
    return contagem
