from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        # ⚠️ Altere aqui com o seu nome e sua matrícula da escola
        NOME_CORRETO = 'Felipe'
        MATRICULA_CORRETA = '12402320'

        # Validação dos dados digitados
        if usuario.lower() == NOME_CORRETO.lower() and senha == MATRICULA_CORRETA:
            return f"<h1>Acesso permitido! Bem-vindo(a), {usuario}!</h1>"
        else:
            # Se errar, recarrega a página enviando uma mensagem de erro
            return render_template('login.html', erro="Nome ou Matrícula incorretos.")
    
    # Se for uma requisição GET, apenas mostra o formulário limpo
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)

