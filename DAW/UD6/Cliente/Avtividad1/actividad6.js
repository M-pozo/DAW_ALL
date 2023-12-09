//ALUMNO: MIGUEL POZO PÉREZ

'use strict';

// Función para modificar elementos
function modifica() {
    // Solicitar al usuario la posición y el nuevo contenido
    let posicion = prompt("Introduce el número de película a modificar:");
    let nuevoContenido = prompt("Introduce el nuevo texto:");

    // Validación de entrada
    if (posicion && nuevoContenido) {
        let lista = document.getElementById('lista');
        let elementos = lista.getElementsByTagName('li');

        // Validación de posición válida
        if (posicion > 0 && posicion <= elementos.length) {
            // Modificar el contenido del elemento en la posición especificada
            elementos[posicion - 1].textContent = nuevoContenido;
        } else {
            alert("Posición no válida. Introduce un número entre 1 y " + elementos.length);
        }
    } else {
        alert("Entrada no válida. Asegúrate de ingresar datos.");
    }
}

// Función para añadir elementos
function anyade() {
    // Solicitar al usuario la posición y el nuevo contenido
    let posicion = prompt("En qué posición vas a insertar:");
    let nuevoContenido = prompt("Introduce el título de la nueva película:");

    // Validación de entrada
    if (posicion && nuevoContenido) {
        let lista = document.getElementById('lista');
        let elementos = lista.getElementsByTagName('li');

        // Validación de posición válida
        if (posicion > 0 && posicion <= elementos.length + 1) {
            // Crear un nuevo elemento y agregarlo a la lista en la posición especificada
            let nuevoElemento = document.createElement('li');
            nuevoElemento.textContent = nuevoContenido;

            // Insertar en la posición deseada
            if (posicion === elementos.length + 1) {
                lista.appendChild(nuevoElemento);
            } else {
                lista.insertBefore(nuevoElemento, elementos[posicion - 1]);
            }
        } else {
            alert("Posición no válida. Introduce un número entre 1 y " + (elementos.length + 1));
        }
    } else {
        alert("Entrada no válida. Asegúrate de ingresar datos.");
    }
}

// Función para borrar elementos
function borra() {
    // Solicitar al usuario la posición del elemento a borrar
    let posicion = prompt("Qué elemento vas a borrar:");

    // Validación de entrada
    if (posicion) {
        let lista = document.getElementById('lista');
        let elementos = lista.getElementsByTagName('li');

        // Validación de posición válida
        if (posicion > 0 && posicion <= elementos.length) {
            // Borrar el elemento en la posición especificada
            lista.removeChild(elementos[posicion - 1]);
        } else {
            alert("Posición no válida. Introduce un número entre 1 y " + elementos.length);
        }
    } else {
        alert("Entrada no válida. Asegúrate de ingresar datos.");
    }
}
