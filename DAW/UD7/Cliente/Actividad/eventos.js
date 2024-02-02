'use strict'
let tarea1 = document.createElement("h1");
tarea1.textContent = "Tarea1";
document.body.appendChild(tarea1);

//UD7 Tarea 1
// Crear div y añadir stilos
let contenedor = document.createElement("div");
contenedor.style.height = "100px";
contenedor.style.width = "100px";
contenedor.style.backgroundColor = "black";
// Crear el parrafo del div para el mensaje
let parrafo = document.createElement("p");
parrafo.textContent = "Pulsa aquí";
parrafo.style.color = "white";

//Añadir los elementos al documento
contenedor.appendChild(parrafo);
document.body.appendChild(contenedor);

contenedor.addEventListener("click", function () {
    window.alert("Pulsaste sobre el div");
})

/*----------------------------------------------------------*/
let tarea2 = document.createElement("h1");
tarea2.textContent = "Tarea2";
document.body.appendChild(tarea2);
//UD7 Tarea 2
let div1 = document.createElement("div");
let contenidoDiv1 = document.createElement("p");
contenidoDiv1.textContent = "Pasa por aqui";
div1.style.height = "100px";
div1.style.width = "100px";
div1.appendChild(contenidoDiv1);
document.body.appendChild(div1);

let div2 = document.createElement("div");
div2.id = "efecto"
let contenidoDiv2 = document.createElement("p");
contenidoDiv2.textContent = "Efectos del movimiento";
div2.style.backgroundColor = "red";
div2.style.height = "100px";
div2.style.width = "100px";
div2.appendChild(contenidoDiv2);
document.body.appendChild(div2);

div1.addEventListener("mouseenter", function () {
    div2.style.backgroundColor = "green";
})
div1.addEventListener("mouseleave", function () {
    div2.style.backgroundColor = "red";
})

let tarea3 = document.createElement("h1");
tarea3.textContent = "Tarea3";
document.body.appendChild(tarea3);
//UD7 Tarea 3
let form = document.createElement("form");
    document.body.appendChild(form);

let input = document.createElement("input");
    input.type = "number"
    input.readonly = true;
    document.body.appendChild(input);

let input2 = document.createElement("input");
    input2.type = "number"
    input2.readonly = true
    document.body.appendChild(input2);

let textArea = document.createElement("input");
    input2.type = "text"
    document.body.appendChild(textArea);

let button = document.createElement("button")
    button.textContent = "Enviar"
    document.body.appendChild(button);

//UD7 Tarea 4
//UD7 Tarea 8 Expreseiones Regulares




