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

let nuevoElemento = document.createElement("ol");
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
div3.remove();

