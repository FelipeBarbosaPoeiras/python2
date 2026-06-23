<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Album extends Model
{
    protected $table = 'albuns';

    protected $fillable = [
        'artista_id',
        'titulo',
        'ano_lancamento',
        'genero',
    ];

    /**
     * Relacionamento 1:N — Um Álbum pertence a um Artista.
     *
     * belongsTo() é definido no modelo do lado "Muitos" (Album),
     * pois é ele que carrega a Foreign Key (artista_id).
     */
    public function artista(): BelongsTo
    {
        return $this->belongsTo(Artista::class, 'artista_id');
    }
}
