'use strict'

function accionPlay(audioSrc) { 
    var reproducir = new Audio(audioSrc);
    reproducir.play();
}

function iniciar() {
    var buttons = document.querySelectorAll("button");
    buttons[0].addEventListener("click", function() {
        accionPlay("https://cdn.freesound.org/previews/721/721044_2853872-lq.mp3");
    }, false);
    buttons[1].addEventListener("click", function() {
        accionPlay("https://cdn.freesound.org/previews/721/721044_2853872-lq.mp3"); 
    }, false);
    buttons[2].addEventListener("click", function() {
        accionPlay("https://cdn.freesound.org/previews/721/721044_2853872-lq.mp3");
    }, false);
    buttons[3].addEventListener("click", function() {
        accionPlay("https://cdn.freesound.org/previews/721/721044_2853872-lq.mp3");
    }, false);
}

window.addEventListener("load", iniciar, false);