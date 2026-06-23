@extends('layouts.app')

@section('title', 'Início — Music DB')

@section('content')
<div class="card" style="text-align:center; padding: 3rem 2rem;">
    <h1>🎵 Bem-vindo ao Music DB</h1>
    <p style="color:#666; margin: 1rem 0 2rem;">
        Gerencie artistas e álbuns com relacionamentos 1:N no Laravel.
    </p>

    <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
        <a href="{{ route('artistas.index') }}" class="btn btn-secundario">
            🎤 Ver Artistas
        </a>
        <a href="{{ route('artistas.create') }}" class="btn btn-primario">
            ➕ Cadastrar Artista
        </a>
        <a href="{{ route('albuns.index') }}" class="btn btn-secundario">
            💿 Ver Álbuns
        </a>
        <a href="{{ route('albuns.create') }}" class="btn btn-primario">
            ➕ Cadastrar Álbum
        </a>
    </div>
</div>
@endsection
