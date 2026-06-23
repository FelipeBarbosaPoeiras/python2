<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ArtistaController;
use App\Http\Controllers\AlbumController;

/*
|--------------------------------------------------------------------------
| Rota inicial — redireciona para a home
|--------------------------------------------------------------------------
*/
Route::get('/', function () {
    return view('home');
})->name('home');

/*
|--------------------------------------------------------------------------
| Rotas de Artistas
| GET  /artistas           → index   (lista artistas)
| GET  /artistas/criar     → create  (formulário)
| POST /artistas           → store   (salva)
| GET  /artistas/{id}      → show    (detalhe + álbuns)
|--------------------------------------------------------------------------
*/
Route::get('/artistas',         [ArtistaController::class, 'index'])->name('artistas.index');
Route::get('/artistas/criar',   [ArtistaController::class, 'create'])->name('artistas.create');
Route::post('/artistas',        [ArtistaController::class, 'store'])->name('artistas.store');
Route::get('/artistas/{artista}', [ArtistaController::class, 'show'])->name('artistas.show');

/*
|--------------------------------------------------------------------------
| Rotas de Álbuns
| GET  /albuns           → index   (lista álbuns)
| GET  /albuns/criar     → create  (formulário com <select> de artistas)
| POST /albuns           → store   (salva)
|--------------------------------------------------------------------------
*/
Route::get('/albuns',       [AlbumController::class, 'index'])->name('albuns.index');
Route::get('/albuns/criar', [AlbumController::class, 'create'])->name('albuns.create');
Route::post('/albuns',      [AlbumController::class, 'store'])->name('albuns.store');
