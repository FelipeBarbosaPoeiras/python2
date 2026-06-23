<?php

namespace App\Http\Controllers;

use App\Models\Album;
use App\Models\Artista;
use Illuminate\Http\Request;

class AlbumController extends Controller
{
    /** Lista todos os álbuns com seus artistas */
    public function index()
    {
        $albuns = Album::with('artista')->orderBy('titulo')->get();
        return view('albuns.index', compact('albuns'));
    }

    /** Exibe o formulário de criação — carrega artistas para o <select> */
    public function create()
    {
        // Todos os artistas são enviados para popular o <select> do formulário
        $artistas = Artista::orderBy('nome')->get();
        return view('albuns.create', compact('artistas'));
    }

    /** Processa e salva o novo álbum */
    public function store(Request $request)
    {
        $request->validate([
            'artista_id'      => 'required|exists:artistas,id',
            'titulo'          => 'required|string|max:255',
            'ano_lancamento'  => 'nullable|integer|min:1900|max:2099',
            'genero'          => 'nullable|string|max:100',
        ]);

        Album::create($request->only('artista_id', 'titulo', 'ano_lancamento', 'genero'));

        return redirect()->route('albuns.index')
                         ->with('sucesso', 'Álbum cadastrado com sucesso!');
    }
}
