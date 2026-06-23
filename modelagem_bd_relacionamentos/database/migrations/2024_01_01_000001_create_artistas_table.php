<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

/*
 * PERGUNTA: Qual tabela deve receber a Foreign Key?
 *
 * RESPOSTA: A tabela ÁLBUNS deve receber a Foreign Key (artista_id).
 *
 * JUSTIFICATIVA: No relacionamento 1:N (Um para Muitos), a chave estrangeira
 * sempre fica no lado "Muitos". Como UM artista pode ter MUITOS álbuns,
 * cada álbum precisa "saber" a qual artista pertence — portanto, a coluna
 * `artista_id` vai na tabela `albuns`, apontando para o `id` da tabela `artistas`.
 * Se a FK ficasse em `artistas`, só seria possível ligar um único álbum por
 * artista (relacionamento 1:1), o que contradiz o modelo proposto.
 */

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('artistas', function (Blueprint $table) {
            $table->id();
            $table->string('nome');
            $table->string('genero')->nullable();
            $table->string('pais')->nullable();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('artistas');
    }
};
