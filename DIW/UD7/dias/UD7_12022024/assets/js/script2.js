/*'use strict'

const divPrueba = document.querySelector('#prueba');
const divPrueba2 = document.querySelector('#prueba2');
const modulo = ['DIW', 'DWC', 'DWS', 'DAW'];

console.log(divPrueba2.innerHTML);

const iniTime = performance.now();
modulo.forEach( (item) => {
    const newP = document.createElement('p');
    newP.textContent = item;
    divPrueba.appendChild(newP);

    divPrueba2.innerHTML += "<p>" + item + "</p>";
});

const endTime = performance.now();
console.log(endTime - iniTime);*/
async function ReadPokemonInfo(url, domObject) {
    await fetch(url)
        .then(response => response.json())
        .then(datoJson => {
            console.log(datoJson);
            const newImg = document.createElement('img');
            newImg.src = datoJson.sprites.front_default;
            domObject.appendChild(newImg);
        });
}
fetch('https://pokeapi.co/api/v2/pokemon')
    .then( response => {
        console.log('soy una promesa del fetch y voy a mi bola también.');
        console.log(response);
        response.json()
        .then(datosJson => {
                console.log('Soy un apromesa del json y voy a mi bola también')
                console.log(datosJson);
            })
    .catch( error => {
        console.log(error)
    })
});

    console.log('Soy el hilo principal y voy a mi bola')

