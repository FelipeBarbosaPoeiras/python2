# 🎵 Music DB — Atividade Laravel (Relacionamento 1:N)

## 📌 Resposta à Pergunta da Atividade

> **Qual tabela deve receber a Foreign Key?**

**A tabela `albuns` deve receber a Foreign Key (`artista_id`).**

No relacionamento **1:N (Um para Muitos)**, a chave estrangeira sempre fica
no lado **"Muitos"**. Como *um* Artista pode ter *muitos* Álbuns, cada álbum
precisa "saber" a qual artista ele pertence — por isso a coluna `artista_id`
fica em `albuns`, referenciando o `id` de `artistas`.

Se colocássemos a FK em `artistas`, cada artista só poderia ter um único álbum
(comportamento 1:1), o que contradiz o modelo proposto.

---

## 🗂 Estrutura de Arquivos Entregues

```
database/migrations/
  2024_01_01_000001_create_artistas_table.php   ← cria tabela artistas
  2024_01_01_000002_create_albuns_table.php     ← cria tabela albuns + FK

app/Models/
  Artista.php   ← hasMany(Album::class)
  Album.php     ← belongsTo(Artista::class)

app/Http/Controllers/
  ArtistaController.php   ← index, create, store, show
  AlbumController.php     ← index, create, store

routes/web.php            ← todas as rotas

resources/views/
  layouts/app.blade.php
  home.blade.php
  artistas/{index,create,show}.blade.php
  albuns/{index,create}.blade.php
```

---

## ⚙️ Como Instalar e Rodar

```bash
# 1. Clone / extraia o projeto e entre na pasta
cd seu-projeto-laravel

# 2. Copie os arquivos desta entrega para as pastas corretas

# 3. Instale dependências
composer install

# 4. Configure o .env
cp .env.example .env
php artisan key:generate

# 5. Configure o banco de dados no .env
DB_CONNECTION=mysql
DB_DATABASE=music_db
DB_USERNAME=root
DB_PASSWORD=sua_senha

# 6. Execute as migrations
php artisan migrate

# 7. Suba o servidor
php artisan serve
# Acesse: http://localhost:8000
```

---

## 🔗 Rotas Disponíveis

| Método | URL               | Ação                              |
|--------|-------------------|-----------------------------------|
| GET    | /                 | Página inicial com links          |
| GET    | /artistas         | Lista todos os artistas           |
| GET    | /artistas/criar   | Formulário de novo artista        |
| POST   | /artistas         | Salva o novo artista              |
| GET    | /artistas/{id}    | Detalhe do artista + seus álbuns  |
| GET    | /albuns           | Lista todos os álbuns             |
| GET    | /albuns/criar     | Formulário com `<select>` de artistas |
| POST   | /albuns           | Salva o novo álbum vinculado      |

---

## 🧩 Diagrama do Relacionamento

```
┌─────────────┐          ┌──────────────────┐
│  artistas   │  1     N │  albuns          │
│─────────────│──────────│──────────────────│
│ id (PK)     │          │ id (PK)          │
│ nome        │          │ artista_id (FK)  │
│ genero      │          │ titulo           │
│ pais        │          │ ano_lancamento   │
│ timestamps  │          │ genero           │
└─────────────┘          │ timestamps       │
                         └──────────────────┘

Artista → hasMany  → Album
Album   → belongsTo → Artista
```
