# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: __Felipe Barbosa Poeiras__
- Turma: __3B1__

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.
H:\Aula12 - Alunos\models\base.py
**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?
 É streamflix.db, está em app.py

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?

 ModeloBase  models/base.py FilmeFavorito  models/filme_favorito.py HistoricoBusca  models/historico_busca.py 
**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?
 de ModeloBas Ganham id data_criacao , data_atualizacao   
**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?
filmes_favoritos Sem ele, o SQLAlchemy geraria `filmefavorito`  Com ele controlamos o nome exato da tabela no banco.
**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?
`tmdb_id` — com `nullable=False` e `unique=True`.
**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?
Verifica se o filme já existe via buscar_por_tmdb Se existir, retorna None Se não, cria o objeto, faz session.add + commit e retorna o favorito salvo.
**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?
 HistoricoBusca em models/historico_busca.py, método ultimas

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.
Só campos espelhados tmdb_id, titulo, poster_path, nota
**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?
 db, ModeloBase, FilmeFavorito, HistoricoBusca. O __init__.pY , o controller não precisa saber em qual arquivo cada classe está
---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).
 Blueprint  url_prefix dashboard_bp filmes_bp /filmes
favoritos_bp /favoritos

---

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?
controllers/filmes_controller.py, função populares()
**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).
api.filmes_populares()  busca os filmes na API TMDB
FilmeFavorito.listar() busca os favoritos salvos no banco para marcar quais já foram favoritados

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?
filmes_controller.py, função buscar(), USA HistoricoBusca.registrar(termo, len(filmes))
**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?
Método POST URL: /favoritos/adicionar/550
**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?
 /filmes/populares com redirect(url_for("filmes.populares"))
**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).
Em app.py python
app.register_blueprint(dashboard_bp)
app.register_blueprint(filmes_bp)
app.register_blueprint(favoritos_bp)    
```
**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?
`dashboard_controller.py`, função `index()`. Envia: `populares`, `melhores`, `total_favoritos`, `historico`, `modo_demo`.
**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?
É um **Service** (camada de serviço). Os controllers a chamam para buscar dados da API externa — ela não salva no banco (não é Model) e não renderiza nada (não é View).

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.
Vem de **`request.args`** quando o formulário da home usa `method="GET"`. A diferença: `request.args` lê parâmetros da URL (`?q=batman`), usado em GET. `request.form` lê o corpo da requisição, usado em POST. O formulário da home usa GET, então o termo vai na URL.
---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?
H:\Aula12 - Alunos\views\templates
**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?
nao sei 
**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.
url_for('dashboard.index
url_for('filmes.populares
url_for('filmes.melhores
url_for('filmes.buscar
url_for('favoritos.listar
**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?
PEDAÇO REUTILIZADO QUE INCLUI O BUSCAR.HYML , DETALHE.HTML , LISTA.HTML E TODOS ESTÃO DENTRO DE VIEW
**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?
NAO SEI, A VARIAVEL {% if favorito %}
**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?
ESTA DENTRO DAPASTA VIEW EM STATIC, NAO SEI COMO LAYOUT CARREGA O ARQUIVO
**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.
  NAO SEI
**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?
 MODO DE TESTE, NAO SEI

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.
NAO ENTENDI
---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!

