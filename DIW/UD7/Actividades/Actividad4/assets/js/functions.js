'use strict'

function accionPlay(audioSrc) { 
    var reproducir = new Audio();
    reproducir.src = audioSrc;
    reproducir.play();
}

function iniciar() {
    var buttons = document.querySelectorAll("button");
    buttons[0].addEventListener("click", function() {
        accionPlay("./assets/audio/fart9.mp3");
    }, false);
    buttons[1].addEventListener("click", function() {
        accionPlay("./assets/audio/piuw.mp3"); 
    }, false);
    buttons[2].addEventListener("click", function() {
        accionPlay("./assets/audio/piw_RfU9dsM.mp3");
    }, false);
    buttons[3].addEventListener("click", function() {
        accionPlay("./assets/audio/tal-cual-hermano-tal-cual.mp3");
    }, false);
}

window.addEventListener("load", iniciar, false);