let = conec = new XMLHttpRequest();
let datos;
let contador = 0;
let pagina = 1;  
conec.addEventListener("load", function () {
    //Función de callback que se ejecutará cuando se carguen los datos
    if (conec.status >= 200 && conec.status < 400) {
        datos = this.response; //En el objeto response tenemos la respuesta
        //Aquí sí tenemos los datos disponibles
        datos = JSON.parse(datos);
        let url = datos.results.url
        datos.results.forEach(p => {
            contador = contador + 1;
            let contenedor = document.createElement("div");
            if (contador % 2 == 0) {
                contenedor.style.backgroundColor = "grey";
            };
            document.write('<a href="'+url+'">')
            contenedor.textContent = "Name:" + p.name + " - - Height:" + p.height + " - - Mass:" + p.mass
            document.write("</a>")
            document.body.appendChild(contenedor);
            document.write("<br>")
            next();
        });
    }
    else {
        console.log("error " + conec.status + ":" + conec.statusText);
    }
})
//URL a la que hacemos la petición de datos
function next() {
    if (datos.next != null) {
        conec.open("GET", datos.next, true)
        conec.send()
    }
    
}
conec.open("GET", "https://swapi.dev/api/people/?page="+pagina, true);
//Hace la petición propiamente dicha
conec.send();
//Si hacemos esto aquí, el resultado será UNDEFINED, porque aún no tenemos
//la respuesta del servidor.
console.log("Voy después de la llamada, y los datos recibidos son: " + datos);

//Si hacemos esto aquí, el resultado será UNDEFINE, poruqe aún no tenemos la respuesta del servidor.
