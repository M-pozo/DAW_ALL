'use strict'

const dato = {
    name: 'Portátil HP del Nano',
    data: {
        ram: '8 GB',
        cpu: 'i711thGen',
        gpu: '1060'
    }
};

const opciones = {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(dato),
};

//fetch("https://api.restful-api.dev/objects/ff8081818d853621018d8f5bf92e0a55", opciones)
fetch("https://api.restful-api.dev/objects/ff8081818d853621018d8f5bf92e0a55")
.then(respuesta => respuesta.json())
.then(dato => console.log(dato))
.catch(error=>console.log(error));