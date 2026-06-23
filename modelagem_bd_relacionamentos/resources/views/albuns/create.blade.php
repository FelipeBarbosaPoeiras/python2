@extends('layouts.app')

@section('title', 'Cadastrar Álbum')

@section('content')
<div class="card" style="max-width:540px; margin:0 auto;">
    <h1>➕ Cadastrar Álbum</h1>

    @if($errors->any())
        <div class="alert-erro">
            <ul style="padding-left:1rem;">
                @foreach($errors->all() as $erro)
                    <li>{{ $erro }}</li>
                @endforeach
            </ul>
        </div>
    @endif

    <form action="{{ route('albuns.store') }}" method="POST">
        @csrf

        {{-- SELECT carregado com todos os artistas do banco --}}
        <div class="form-group">
            <label for="artista_id">Artista *</label>
            <select id="artista_id" name="artista_id" required>
                <option value="">— Selecione um artista —</option>
                @foreach($artistas as $artista)
                    <option value="{{ $artista->id }}"
                        {{ old('artista_id') == $artista->id ? 'selected' : '' }}>
                        {{ $artista->nome }}
                        @if($artista->pais) ({{ $artista->pais }}) @endif
                    </option>
                @endforeach
            </select>
            @if($artistas->isEmpty())
                <small style="color:#e94560;">
                    Nenhum artista cadastrado.
                    <a href="{{ route('artistas.create') }}">Cadastre um artista primeiro.</a>
                </small>
            @endif
        </div>

        <div class="form-group">
            <label for="titulo">Título do Álbum *</label>
            <input type="text" id="titulo" name="titulo"
                   value="{{ old('titulo') }}" placeholder="Ex: Abbey Road" required>
        </div>

        <div class="form-group">
            <label for="ano_lancamento">Ano de Lançamento</label>
            <input type="number" id="ano_lancamento" name="ano_lancamento"
                   value="{{ old('ano_lancamento') }}"
                   placeholder="Ex: 1969" min="1900" max="2099">
        </div>

        <div class="form-group">
            <label for="genero">Gênero</label>
            <input type="text" id="genero" name="genero"
                   value="{{ old('genero') }}" placeholder="Ex: Rock Progressivo">
        </div>

        <div style="display:flex; gap:.8rem; margin-top:1.5rem;">
            <button type="submit" class="btn btn-primario">Salvar Álbum</button>
            <a href="{{ route('albuns.index') }}" class="btn btn-secundario">Cancelar</a>
        </div>
    </form>
</div>
@endsection
