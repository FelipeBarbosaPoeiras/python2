from flask import Flask

app = Flask(__name__)

# 1. Dados estruturados do currículo (Escopo Global)
nome = "Felipe Barbosa Poeiras"
cargo = "Estudante de T.I"
telefone = "31 9 8942-6287"
email = "felipepoeiras21@gmail.com"
localizacao = "Vila Oeste Belo Horizonte"
objetivo = "Busco estágio para adquirir experiência na área de T.I"

# 2. Criação das listas em HTML de forma nativa no Python
formacao_html = "".join([f"<p class='mb-1 text-secondary fs-5'>{item}</p>" for item in [
    "Cursando Ensino Médio e Técnico",
    "Aluno do 3º ano do Curso de T.I"
]])

qualidades_html = "".join([f"<li>{item}</li>" for item in [
    "Trabalho em equipe",
    "Comunicativo",
    "Inglês Básico",
    "Proativo"
]])

habilidades_html = "".join([f"<li>{item}</li>" for item in [
    "Lógica de programação",
    "Python (básico)",
    "HTML, CSS e JavaScript (básico)",
    "Banco de dados",
    "Pacote Office Word, Excel, PowerPoint",
    "GitHub"
]])

# 3. Rota única e principal para exibir o currículo
@app.route('/')
def curriculo():
    # Retorna o HTML estruturado usando f-string legítima
    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo - {nome}</title>
        <link href="jsdelivr.net" rel="stylesheet">
        <style>
            body {{ font-family: Arial, sans-serif; color: #333; }}
            .text-navy {{ color: #1a2e40; }}
            .sidebar-accent {{ width: 30px; background-color: #1a2e40; min-height: 100%; position: absolute; left: 0; top: 0; }}
            .cv-container {{ max-width: 900px; position: relative; padding-left: 50px; }}
            .section-title {{ color: #1a2e40; font-weight: bold; margin-bottom: 15px; }}
            ul {{ padding-left: 20px; }}
            li {{ margin-bottom: 8px; }}
        </style>
    </head>
    <body class="bg-light py-5">

        <div class="container bg-white p-5 shadow rounded cv-container">
            <div class="sidebar-accent rounded-start"></div>

            <header class="row align-items-center mb-5">
                <div class="col-md-7">
                    <h1 class="display-5 fw-bold text-navy mb-1">{nome}</h1>
                    <p class="h4 text-secondary fw-normal">{cargo}</p>
                </div>
                <div class="col-md-5 border-start ps-4 text-secondary small">
                    <div class="mb-2">📞 {telefone}</div>
                    <div class="mb-2">✉️ {email}</div>
                    <div>📍 {localizacao}</div>
                </div>
            </header>

            <section class="mb-5">
                <h3 class="section-title">Objetivo</h3>
                <p class="fs-5 text-secondary">{objetivo}</p>
            </section>

            <div class="row">
                <div class="col-md-6 pe-4">
                    <div class="mb-5">
                        <h3 class="section-title">Formação</h3>
                        {formacao_html}
                    </div>

                    <div>
                        <h3 class="section-title">Qualidades</h3>
                        <ul class="fs-5 text-secondary">
                            {qualidades_html}
                        </ul>
                    </div>
                </div>

                <div class="col-md-6 ps-4 border-start">
                    <h3 class="section-title">Habilidades Técnicas Desenvolvidas e em desenvolvimento</h3>
                    <ul class="fs-5 text-secondary">
                        {habilidades_html}
                    </ul>
                </div>
            </div>
        </div>

    </body>
    </html>
    """

# 4. Inicialização única do servidor
if __name__ == '__main__':
    app.run(debug=True)
