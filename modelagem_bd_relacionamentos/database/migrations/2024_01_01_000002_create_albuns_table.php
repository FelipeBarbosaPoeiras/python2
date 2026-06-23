<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('albuns', function (Blueprint $table) {
            $table->id();

            // Foreign Key — fica aqui pois Álbum é o lado "Muitos" do relacionamento 1:N
            $table->foreignId('artista_id')
                  ->constrained('artistas')   // referencia a tabela artistas
                  ->onDelete('cascade');       // ao deletar artista, remove seus álbuns

            $table->string('titulo');
            $table->integer('ano_lancamento')->nullable();
            $table->string('genero')->nullable();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('albuns');
    }
};
