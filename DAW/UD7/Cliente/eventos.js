'use strict'
let element = document.getElementById("prueba")

element.onclick = inputClick;

function inputClick(element, event) {
    alert("Un evento" + event.type + " ha sido detectado en:" + element.id);
}