'use strict'
//Función que hace una llamada a una API y devuelve una promesa
function llamadaApi(url) {
    return new Promise((resolver, rechazar) => {
        let req = new XMLHttpRequest();
        setTimeout(function () {
            req.onload = function () {
                if (req.status >= 200 && req.status < 400) {
                    let respuesta = JSON.parse(this.response);
                    resolver(respuesta);
                }
                else {
                    rechazar("error " + req.status + ":" + req.statusText);
                }
            }
            req.open("GET", url, true);
            req.send();
        }, 3000);
    });
}

//En la variable personaje tenemos una promesa, que internamente ha hecho una llamada
//a una API con el objeto XMLHttpRequest
let personaje = llamadaApi("https://swapi.dev/api/people/1/");
//Ahora podemos consumir la promesa
personaje
    .then(dato => console.log(dato.name))
    .catch(error => console.log(error));

console.log("🇾🇪")