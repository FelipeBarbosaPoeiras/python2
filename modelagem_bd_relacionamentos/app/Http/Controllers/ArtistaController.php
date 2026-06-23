<?php

namespace App\Http\Controllers;

use App\Models\Artista;
use Illuminate\Http\Request;

class ArtistaController extends Controller
{
    /** Lista todos os artistas (página inicial de artistas) */
    public function index()
    {
        $artistas = Artista::orderBy('nome')->get();
        return view('artistas.index', compact('artistas'));
    }

    /** Exibe o formulário de cadastro */
    public function create()
    {
        return view('artistas.create');
    }

    /** Processa e salva o novo artista */
    public function store(Request $request)
    {
        $request->validate([
            'nome'   => 'required|string|max:255',
            'genero' => 'nullable|string|max:100',
            'pais'   => 'nullable|string|max:100',
        ]);

        Artista::create($request->only('nome', 'genero', 'pais'));

        return redirect()->route('artistas.index')
                         ->with('sucesso', 'Artista cadastrado com sucesso!');
    }

    /** Exibe os detalhes de um artista e seus álbuns */
    public function show(Artista $artista)
    {
        // Carrega os álbuns relacionados via eager loading
        $artista->load('albuns');
        return view('artistas.show', compact('artista'));
    }
}
