// 9) Modo escuro com persistência em localStorage
(function () {
    const html = document.documentElement;
    const botao = document.getElementById('toggleTema');

    function aplicarTema(tema) {
        html.setAttribute('data-bs-theme', tema);
        if (botao) {
            const icone = botao.querySelector('i');
            icone.className = tema === 'dark' ? 'bi bi-sun' : 'bi bi-moon-stars';
        }
    }

    const temaSalvo = localStorage.getItem('tema') || 'light';
    aplicarTema(temaSalvo);

    if (botao) {
        botao.addEventListener('click', () => {
            const temaAtual = html.getAttribute('data-bs-theme');
            const novoTema = temaAtual === 'dark' ? 'light' : 'dark';
            localStorage.setItem('tema', novoTema);
            aplicarTema(novoTema);
        });
    }
})();
