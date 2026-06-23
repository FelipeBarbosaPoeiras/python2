@extends('layouts.app')

@section('title', 'Artistas')

@section('content')
<div class="card">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
        <h1>🎤 Artistas</h1>
        <a href="{{ route('artistas.create') }}" class="btn btn-primario">+ Novo Artista</a>
    </div>

    @if($artistas->isEmpty())
        <p style="color:#888;">Nenhum artista cadastrado ainda.</p>
    @else
        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Nome</th>
                    <th>Gênero</th>
                    <th>País</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                @foreach($artistas as $artista)
                <tr>
                    <td>{{ $artista->id }}</td>
                    <td><strong>{{ $artista->nome }}</strong></td>
                    <td>{{ $artista->genero ?? '—' }}</td>
                    <td>{{ $artista->pais ?? '—' }}</td>
                    <td>
                        <a href="{{ route('artistas.show', $artista) }}" class="btn btn-secundario btn-sm">
                            Ver Álbuns
                        </a>
                    </td>
                </tr>
                @endforeach
            </tbody>
        </table>
    @endif
</div>
@endsection
