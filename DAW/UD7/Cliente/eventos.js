'use strict'
let contador = document.getElementById("contador")

function inputClick(elemento, even) {
    let a = 0
    let p = contador.createElement("p")
    p.textContent = parseInt(a+1)  
}

contador.addEventListener('click', console.log).inputClick
