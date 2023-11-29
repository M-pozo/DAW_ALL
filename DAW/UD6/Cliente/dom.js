'use strict'

let elemento = document.getElementById("padre")
if (elemento % 2 == 0) {
    console.log("hola")
    console.log(elemento)
}

console.log(elemento.childNodes[2])
console.log(elemento.children)
console.log(elemento.parentNode)
console.log(elemento.nestElementSibling)
console.log(elemento.previousElementSibling)

//elemento.childNode[2] = "Hola <b>Baracola</b>"

/*let nuevoElemento = document.createElement("div");
nuevoElemento.textContent = "este es el nuevo elemento";
let padre = document.getElementById("padre");
padre.appendChild(nuevoElemento);*/

/*let nuevoElemento = document.createElement("ol");
let contador = parseInt(prompt("Cuantas filas quieres?"))
for (let index = 1; index <= contador; index++) {
    let li = document.createElement("li")
    nuevoElemento.appendChild(li);
    let contenido = prompt("Que le añadimos a la fila"+index)
    li.textContent = contenido;
    nuevoElemento.removeChild(li)
}
let actividad = document.getElementById("actividad");
actividad.insertBefore(nuevoElemento, actividad.children[1]);

let div3 = document.getElementById("3");
div3.remove();*/

/*let actividad2 = document.getElementById("actividad2")
for (let index = 1; index <= 10; index++) {
    let div = document.createElement("div")
    actividad2.appendChild(div)
    div.setAttribute("id", index)
    div.textContent = "Este es el div hijo "+index
}
let seleccionDiv = parseInt(prompt("A que div quieres añadirle contenido"))
let divSeleccionado = actividad2.children[seleccionDiv-1]
let contenidoDiv = prompt("Que contenido quieres añadir?")
divSeleccionado.textContent = contenidoDiv*/
let actividad3 = document.getElementById("actividad3")
function crearDivs(color) {
    for (let index = 0; index < 255; index++) {
        let div = document.createElement("div")
        actividad3.appendChild(div)
        div.style.width = "100%"
        div.style.height = "2px"
        if (color == "gris") { 
            div.style.backgroundColor = "rgb(" + index + ", " + index + ", " + index + ")" 
        } else if (color == "verde") {
            div.style.backgroundColor = "rgb(000, " + index + ", 000)"
        } else if (color == "rojo") {
            div.style.backgroundColor = "rgb(" + index + ", 000, 000)"
        };
    }
}
let resultado = parseInt(prompt(`Que color quieres? 
    1. Grises
    2. verde
    3. rojo`));
switch (resultado) {
    case 1:
        crearDivs("gris")
        break;
    case 2:
        crearDivs("verde")
        break;
    case 3:
        crearDivs("rojo")
        break;
    default:
        break;
}