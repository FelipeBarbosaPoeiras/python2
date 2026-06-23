<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Artista extends Model
{
    protected $table = 'artistas';

    protected $fillable = [
        'nome',
        'genero',
        'pais',
    ];

    /**
     * Relacionamento 1:N — Um Artista possui muitos Álbuns.
     *
     * hasMany() é definido no modelo do lado "Um" (Artista),
     * apontando para o modelo do lado "Muitos" (Album).
     */
    public function albuns(): HasMany
    {
        return $this->hasMany(Album::class, 'artista_id');
    }
}
