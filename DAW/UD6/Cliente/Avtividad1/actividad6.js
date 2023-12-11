//ALUMNO: MIGUEL POZO PÉREZ

'use strict';

function modifica() {
    let posicion = prompt("Introduce el número de película a modificar");
    let titulo = prompt("Introduce el nuevo título");

    if (posicion && titulo) {
        let lista = document.getElementById('lista');
        let elementos = lista.getElementsByTagName('li');

        if (posicion > 0 && posicion <= elementos.length) {
            /* Modificar el contenido*/
            elementos[posicion - 1].textContent = titulo;
        } else {
            alert("Introduce un número entre 1 y " + elementos.length);
        }
    } else {
        alert("Introduce algo");
    }
}

function anyade() {
    /*Solicitar al usuario la posición y el titulo*/
    let posicion = prompt("En qué posición vas a insertar:");
    let titulo = prompt("Introduce el título de la nueva película:");

    if (posicion && titulo) {
        let lista = document.getElementById('lista');
        let elementos = lista.getElementsByTagName('li');

        if (posicion > 0 && posicion <= elementos.length + 1) {
            /* Crear un nuevo elemento y agregarlo*/
            let nuevoElemento = document.createElement('li');
            nuevoElemento.textContent = titulo;

            /*Insertar en la posición*/
            if (posicion == elementos.length + 1) {
                lista.appendChild(nuevoElemento);
            } else {
                lista.insertBefore(nuevoElemento, elementos[posicion - 1]);
            }
        } else {
            alert("Introduce un número entre 1 y " + (elementos.length + 1));
        }
    } else {
        alert("Introduce algo");
    }
}

function borra() {
    /*Solicitar al usuario la posición del elemento a borrar*/
    let posicion = prompt("Qué elemento vas a borrar:");

    if (posicion) {
        let lista = document.getElementById('lista');
        let elementos = lista.getElementsByTagName('li');

        if (posicion > 0 && posicion <= elementos.length) {
            lista.removeChild(elementos[posicion - 1]);
        } else {
            alert("Introduce un número entre 1 y " + elementos.length);
        }
    } else {
        alert("Introduce algo");
    }
}
