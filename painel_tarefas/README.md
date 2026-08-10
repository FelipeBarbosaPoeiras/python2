# Painel de Controle de Tarefas (Flask)

Projeto completo desenvolvido conforme o roteiro de exercícios, cobrindo os 10 itens
pedidos (rotas/templates, SQLite, autenticação, CRUD, API externa, Bootstrap,
segurança, filtro por status via AJAX, modo escuro e dashboard de progresso) além
do desafio avançado (API REST completa).

## Como rodar

```bash
# 1) Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# 2) Instale as dependências
pip install -r requirements.txt

# 3) Rode a aplicação
python app.py
```

Acesse http://127.0.0.1:5000 no navegador. O banco `instance/banco.db` é criado
automaticamente na primeira execução.

Para produção, defina uma `SECRET_KEY` própria antes de rodar:

```bash
export SECRET_KEY="uma-chave-bem-aleatoria"   # Linux/Mac
set SECRET_KEY=uma-chave-bem-aleatoria        # Windows
```

`DEBUG` já vem `False` por padrão; para ativar em desenvolvimento, defina
`FLASK_DEBUG=1` antes de rodar.

## Estrutura

```
painel_tarefas/
├── app.py                 # Rotas e lógica da aplicação
├── database.py             # Funções de acesso ao SQLite
├── requirements.txt
├── instance/
│   └── banco.db             # Criado automaticamente
├── static/
│   ├── css/style.css
│   └── js/main.js           # Modo escuro persistente
└── templates/
    ├── base.html            # Layout, menu e Bootstrap
    ├── login.html
    ├── registro.html
    ├── dashboard.html        # Lista de tarefas + filtro + frase motivacional
    ├── _lista_tarefas.html   # Partial reaproveitado no render inicial
    ├── nova_tarefa.html
    ├── editar_tarefa.html
    └── progresso.html        # Gráficos Chart.js (item 10)
```

## Rotas principais

| Rota                | Método(s)        | Descrição                                     |
|----------------------|-------------------|------------------------------------------------|
| `/registro`          | GET/POST          | Cadastro de usuário                             |
| `/login`              | GET/POST          | Login (sessão)                                  |
| `/logout`             | GET               | Encerra a sessão                                |
| `/dashboard`          | GET               | Lista de tarefas do usuário logado + filtro + frase motivacional |
| `/nova_tarefa`        | GET/POST          | Formulário de criação                           |
| `/editar/<id>`        | GET/POST          | Formulário de edição                            |
| `/excluir/<id>`       | POST              | Remove a tarefa                                 |
| `/concluir/<id>`      | POST              | Atalho para marcar como concluída               |
| `/progresso`          | GET               | Dashboard de progresso com gráficos (item 10)   |
| `/api/tarefas`        | GET/POST          | Lista (com filtro `?status=`) e cria via JSON   |
| `/api/tarefas/<id>`   | GET/PUT/DELETE    | Versão REST completa (desafio avançado)         |
| `/api/progresso`      | GET               | Contagem de tarefas por status (JSON p/ gráficos)|

## Observação sobre o enunciado

O roteiro original define `/dashboard` tanto para o painel de tarefas (item 5)
quanto para o painel de progresso (item 10), o que gera um conflito de nomes.
Neste projeto, `/dashboard` segue o item 5 (lista de tarefas, com frase
motivacional e filtro), e o painel de progresso do item 10 foi implementado em
`/progresso`.

## Segurança implementada

- Senhas com hash via `werkzeug.security` (nunca armazenadas em texto puro).
- Rotas internas protegidas por decorator `@login_required` baseado em `session`.
- `SECRET_KEY` configurável por variável de ambiente.
- `DEBUG=False` por padrão.
- Validação básica de campos obrigatórios e tamanho mínimo de senha.
