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
//let personaje = llamadaApi("https://swapi.dev/api/people/1/");
//Ahora podemos consumir la promesa
/*personaje
    .then(dato => console.log(dato.name))
    .catch(error => console.log(error))

.then(personaje=>{
    console.log(personaje);
    console.log(personaje.name);
    personaje.films.forEach(peli=>{
        llamadaApi(api)
        .then(json_peli=>console.log(json_peli.title))
    })

    let arrayDePromesa=personaje.films.map(peli=>llamadaApi(peli));
    return Promise.all(arrayDePromesa);
})
.catch(error=>console.log("catch: "+error));

console.log("Después de la promesa")
*/
//personaje peliculas > planetas

let personajes = llamadaApi("https://swapi.dev/api/people/1")
personajes.then(personaje => {
    console.log(personaje.name)
    personaje.films.forEach(pelicula => {
        let peliculas = llamadaApi(pelicula)
        peliculas.then(pelicula => {
            console.log(pelicula.title)
            pelicula.planets.forEach(planeta => {
                let planetas = llamadaApi(planeta)
                planetas.then(planet => console.log(planet.name))
            })

        })
    })

})
.catch(error => console.log(error));