<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title', 'Music DB')</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Segoe UI', sans-serif; background: #f5f5f5; color: #333; }

        nav {
            background: #1a1a2e;
            padding: 1rem 2rem;
            display: flex;
            gap: 1.5rem;
            align-items: center;
        }
        nav a {
            color: #e0e0e0;
            text-decoration: none;
            font-weight: 500;
            transition: color .2s;
        }
        nav a:hover { color: #e94560; }
        nav .brand { color: #e94560; font-size: 1.2rem; font-weight: 700; margin-right: auto; }

        .container { max-width: 900px; margin: 2rem auto; padding: 0 1rem; }

        .card {
            background: #fff;
            border-radius: 8px;
            padding: 1.5rem 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,.08);
            margin-bottom: 1.5rem;
        }

        h1 { font-size: 1.8rem; margin-bottom: 1rem; color: #1a1a2e; }
        h2 { font-size: 1.3rem; margin-bottom: .8rem; color: #1a1a2e; }

        .alert-sucesso {
            background: #d4edda; color: #155724;
            border: 1px solid #c3e6cb; border-radius: 6px;
            padding: .75rem 1rem; margin-bottom: 1rem;
        }
        .alert-erro {
            background: #f8d7da; color: #721c24;
            border: 1px solid #f5c6cb; border-radius: 6px;
            padding: .75rem 1rem; margin-bottom: 1rem;
        }

        /* Formulários */
        .form-group { margin-bottom: 1rem; }
        label { display: block; font-weight: 600; margin-bottom: .4rem; }
        input[type=text], input[type=number], select {
            width: 100%; padding: .6rem .8rem;
            border: 1px solid #ccc; border-radius: 6px; font-size: 1rem;
        }
        input:focus, select:focus { outline: none; border-color: #e94560; }

        .btn {
            display: inline-block; padding: .6rem 1.4rem;
            border: none; border-radius: 6px; cursor: pointer;
            font-size: 1rem; font-weight: 600; text-decoration: none;
            transition: opacity .2s;
        }
        .btn:hover { opacity: .85; }
        .btn-primario { background: #e94560; color: #fff; }
        .btn-secundario { background: #1a1a2e; color: #fff; }
        .btn-sm { padding: .35rem .9rem; font-size: .85rem; }

        /* Tabelas */
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: .75rem 1rem; text-align: left; border-bottom: 1px solid #eee; }
        th { background: #1a1a2e; color: #fff; }
        tr:hover td { background: #fafafa; }

        .tag {
            display: inline-block; padding: .2rem .6rem;
            border-radius: 20px; font-size: .8rem; font-weight: 600;
            background: #e94560; color: #fff;
        }
    </style>
</head>
<body>

<nav>
    <span class="brand">🎵 Music DB</span>
    <a href="{{ route('home') }}">Início</a>
    <a href="{{ route('artistas.index') }}">Artistas</a>
    <a href="{{ route('artistas.create') }}">+ Novo Artista</a>
    <a href="{{ route('albuns.index') }}">Álbuns</a>
    <a href="{{ route('albuns.create') }}">+ Novo Álbum</a>
</nav>

<div class="container">
    @if(session('sucesso'))
        <div class="alert-sucesso">✅ {{ session('sucesso') }}</div>
    @endif

    @yield('content')
</div>

</body>
</html>
