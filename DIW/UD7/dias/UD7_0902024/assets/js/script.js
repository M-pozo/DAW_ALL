'use strict'

alert('hola');
console.log(document);
console.log(window);
//const divPrueba = document.getElementById('prueba');
//console.log(document.querySelector('p'));

/*if(divPrueba){ //if (divPrueva !== null && divPrueba !== undefined)
    console.log(divPrueba.getElementById('parrafo'));
};*/

const arr = [1, 2, 3];
const arr2 = arr;

arr2.push(4);
console.log(arr);

const divPrueba = document.querySelector('#prueba');
const modulo = ["diw", 'dwc', 'dws', 'daw']
const ejObjeto = [
    nombreCorto = "fasdfsf",
    horario = [
        {
            diaSemana: "fasdf"
        },
        {
            diaSemana: "safea"
        }
    ],
];


for (const modulos of modulo) {
    const newP = document.createElement('p');
    newP.textContent = modulos
    divPrueba.appendChild(newP)
}

/*modulo.forEach( item => {

})*/