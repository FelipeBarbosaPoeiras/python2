@extends('layouts.app')

@section('title', 'Cadastrar Artista')

@section('content')
<div class="card" style="max-width:540px; margin:0 auto;">
    <h1>➕ Cadastrar Artista</h1>

    @if($errors->any())
        <div class="alert-erro">
            <ul style="padding-left:1rem;">
                @foreach($errors->all() as $erro)
                    <li>{{ $erro }}</li>
                @endforeach
            </ul>
        </div>
    @endif

    <form action="{{ route('artistas.store') }}" method="POST">
        @csrf

        <div class="form-group">
            <label for="nome">Nome do Artista *</label>
            <input type="text" id="nome" name="nome"
                   value="{{ old('nome') }}" placeholder="Ex: The Beatles" required>
        </div>

        <div class="form-group">
            <label for="genero">Gênero Musical</label>
            <input type="text" id="genero" name="genero"
                   value="{{ old('genero') }}" placeholder="Ex: Rock, Pop, MPB...">
        </div>

        <div class="form-group">
            <label for="pais">País de Origem</label>
            <input type="text" id="pais" name="pais"
                   value="{{ old('pais') }}" placeholder="Ex: Brasil">
        </div>

        <div style="display:flex; gap:.8rem; margin-top:1.5rem;">
            <button type="submit" class="btn btn-primario">Salvar Artista</button>
            <a href="{{ route('artistas.index') }}" class="btn btn-secundario">Cancelar</a>
        </div>
    </form>
</div>
@endsection
