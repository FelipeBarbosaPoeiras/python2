@extends('layouts.app')

@section('title', 'Álbuns')

@section('content')
<div class="card">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
        <h1>💿 Álbuns</h1>
        <a href="{{ route('albuns.create') }}" class="btn btn-primario">+ Novo Álbum</a>
    </div>

    @if($albuns->isEmpty())
        <p style="color:#888;">Nenhum álbum cadastrado ainda.</p>
    @else
        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Título</th>
                    <th>Artista</th>
                    <th>Ano</th>
                    <th>Gênero</th>
                </tr>
            </thead>
            <tbody>
                @foreach($albuns as $album)
                <tr>
                    <td>{{ $album->id }}</td>
                    <td><strong>{{ $album->titulo }}</strong></td>
                    <td>
                        {{-- Acessa o artista relacionado via belongsTo --}}
                        <a href="{{ route('artistas.show', $album->artista) }}"
                           style="color:#e94560; text-decoration:none;">
                            {{ $album->artista->nome }}
                        </a>
                    </td>
                    <td>{{ $album->ano_lancamento ?? '—' }}</td>
                    <td>{{ $album->genero ?? '—' }}</td>
                </tr>
                @endforeach
            </tbody>
        </table>
    @endif
</div>
@endsection
