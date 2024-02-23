function accionPlay() {
    if (!medio.paused && !medio.ended) {
        medio.pause();
        play.textContent = '\u25BA'; // Cambia el icono a "play"
        document.body.style.backgroundColor = '#fff'; // Cambia el color de fondo
    } else {
        medio.play();
        play.textContent = '||'; // Cambia el icono a "pausa"
        document.body.style.backgroundColor = 'grey'; // Cambia el color de fondo
    }
}

function accionReiniciar() {
    medio.currentTime = 0; // Reinicia el vídeo al principio
    medio.play(); // Comienza a reproducir el vídeo
    play.textContent = '||'; // Cambia el icono a "pausa"
    document.body.style.backgroundColor = 'grey'; // Cambia el color de fondo
}

function accionRetrasar() {
    if (medio.currentTime >= 5) {
        medio.currentTime -= 5; // Retrocede 5 segundos
    } else {
        medio.currentTime = 0; // Vuelve al inicio si ya está al principio
    }
}

function accionAdelantar() {
    if (medio.currentTime < medio.duration - 5) {
        medio.currentTime += 5; // Adelanta 5 segundos
    } else {
        medio.currentTime = medio.duration; // Avanza al final si ya está al final
    }
}

function accionSilenciar() {
    medio.muted = !medio.muted; // Activa/desactiva el silencio
    if (medio.muted) {
        silenciar.textContent = 'Escuchar'; // Cambia el texto del botón a "Escuchar"
    } else {
        silenciar.textContent = 'Silenciar'; // Cambia el texto del botón a "Silenciar"
    }
}

function accionMasVolumen() {
    if (medio.volume < 1) {
        medio.volume += 0.1; // Incrementa el volumen en 0.1
    }
}

function accionMenosVolumen() {
    if (medio.volume > 0) {
        medio.volume -= 0.1; // Decrementa el volumen en 0.1
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
