let = conec = new XMLHttpRequest();

let datos;
let contador = 0;
conec.addEventListener("load", function () {
    //Función de callback que se ejecutará cuando se carguen los datos
    if (conec.status >= 200 && conec.status < 400) {
        datos = this.response; //En el objeto response tenemos la respuesta
        //Aquí sí tenemos los datos disponibles
        datos = JSON.parse(datos);
        datos.results.forEach(p => {
            contador = contador + 1;
            let contenedor = document.createElement("div");
            if (contador % 2 == 0){
                contenedor.style.backgroundColor = "grey";
            };
            contenedor.textContent = "Name:"+p.name + " Height:" + p.height + " Mass:" + p.mass
            document.body.appendChild(contenedor);
        });
    }
    else {
        console.log("error " + conec.status + ":" + conec.statusText);
    }
})
//URL a la que hacemos la petición de datos
conec.open("GET", "https://swapi.dev/api/people/", true);
//Hace la petición propiamente dicha
conec.send();
//Si hacemos esto aquí, el resultado será UNDEFINED, porque aún no tenemos
//la respuesta del servidor.
console.log("Voy después de la llamada, y los datos recibidos son: " + datos);
