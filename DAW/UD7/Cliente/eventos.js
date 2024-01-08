'use strict'
let elemento = document.getElementById("contador")

function inputClick(event) {
    let iz=document.getElementById("iz")
    let dr = document.getElementById("dr")
    if (event.button == 0) {
        document.write("fadsfa")
        if (iz == undefined) {
            iz = document.createElement("div")
            iz.style.float = "right"
            iz.textContent = "1"
            iz.id = "iz"
            iz.body.appendChild(iz)
        } else {
            iz.textContent = (parseInt(iz.textContent) + 1)
        }
    } else if (dr == undefined){
        if (dr == undefined) {
            dr = document.createElement("div")
            dr.style.float = "right"
            dr.textContent = "1"
            dr.id = "dr"
            document.body.appendChild(dr)
        } else {
            dr.textContent = (parseInt(dr.textContent) + 1)
        }
    }
}

