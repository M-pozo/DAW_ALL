function accionPlay() {
    if (!medio.paused && !medio.ended) {
        medio.pause();
        play.value = '\u25BA';
        document.body.style.backgroundColor = '#fff';
    } else {
        medio.play();
        play.value = '||';
        document.body.style.backgroundColor = 'grey';
    }
}

function accionReiniciar() {
    medio.currentTime = 0;
    medio.play();
    play.value = '||';
    document.body.style.backgroundColor = 'grey';
}

function accionRetrasar() {
    if (medio.currentTime >= 5) {
        medio.currentTime -= 5;
    } else {
        medio.currentTime = 0;
    }
}

function accionAdelantar() {
    if (medio.currentTime < medio.duration) {
        medio.currentTime += 5;
    } else {
        medio.currentTime = medio.duration;
    }
}

function accionSilenciar() {
    medio.muted = !medio.muted;
}

function accionMasVolumen() {
    if (medio.volume < 1) {
        medio.volume += 0.1;
    }
}

function accionMenosVolumen() {
    if (medio.volume > 0) {
        medio.volume -= 0.1;
    }
}

function iniciar() {
    medio = document.getElementById('medio');
    play = document.getElementById('play');
    reiniciar = document.getElementById('reiniciar');
    retrasar = document.getElementById('retrasar');
    adelantar = document.getElementById('adelantar');
    silenciar = document.getElementById('silenciar');
    menosVolumen = document.getElementById('menosVolumen');
    masVolumen = document.getElementById('masVolumen');

    play.addEventListener('click', accionPlay);
    reiniciar.addEventListener('click', accionReiniciar);
    retrasar.addEventListener('click', accionRetrasar);
    adelantar.addEventListener('click', accionAdelantar);
    silenciar.addEventListener('click', accionSilenciar);
    menosVolumen.addEventListener('click', accionMenosVolumen);
    masVolumen.addEventListener('click', accionMasVolumen);
}

window.addEventListener('load', iniciar, false);
