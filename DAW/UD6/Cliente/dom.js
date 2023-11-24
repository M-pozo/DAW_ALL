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
