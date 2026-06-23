@extends('layouts.app')

@section('title', $artista->nome)

@section('content')
<div class="card">
    <div style="margin-bottom:1.5rem;">
        <a href="{{ route('artistas.index') }}" style="color:#e94560; text-decoration:none;">← Voltar</a>
    </div>

    <h1>🎤 {{ $artista->nome }}</h1>
    <p style="color:#666; margin:.5rem 0 1.5rem;">
        @if($artista->genero) <span class="tag">{{ $artista->genero }}</span> @endif
        @if($artista->pais) &nbsp;📍 {{ $artista->pais }} @endif
    </p>

    <h2>💿 Álbuns ({{ $artista->albuns->count() }})</h2>

    @if($artista->albuns->isEmpty())
        <p style="color:#888;">Nenhum álbum cadastrado para este artista.</p>
    @else
        <table>
            <thead>
                <tr>
                    <th>Título</th>
                    <th>Ano</th>
                    <th>Gênero</th>
                </tr>
            </thead>
            <tbody>
                @foreach($artista->albuns as $album)
                <tr>
                    <td>{{ $album->titulo }}</td>
                    <td>{{ $album->ano_lancamento ?? '—' }}</td>
                    <td>{{ $album->genero ?? '—' }}</td>
                </tr>
                @endforeach
            </tbody>
        </table>
    @endif

    <div style="margin-top:1.5rem;">
        <a href="{{ route('albuns.create') }}" class="btn btn-primario btn-sm">+ Adicionar Álbum</a>
    </div>
</div>
@endsection
