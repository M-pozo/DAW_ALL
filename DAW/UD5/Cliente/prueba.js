'use strict'

//let subVentana = window.open("https://www.google.es", "nueva", "height=600", "width=800")
//subVentana.close();

//window.location.assign("https://www.google.es")

/*document.write(navigator.appCodeName);
document.write('<br>')
document.write(navigator.appName);
document.write('<br>')
document.write(navigator.appVersion);
document.write('<br>')
document.write(navigator.cookieEnabled);
document.write('<br>')
document.write(navigator.platform);
document.write('<br>')
document.write(navigator.userAgent);

document.write("Miguel");
document.write("Pozo");
document.title = "Pagina JS"

let date = new Date(); // Crea objeto Date almacena la fecha actual
console.log(typeof date); // Imprime object
console.log(date instanceof Date); // Imprime true
console.log(date); // Imprime fecha actual

let miExp = /[0-9]{8}[-][A-Z]{1}/;
document.write("15236987K")

let dateRgex = /^\d{2}\/\d{2}\/(\d{2}|\d{4})$/
let telefonoRegex = /^\(\+([0-9]){3}\)(([0-9]{3})[-]){2}([0-9]){3}$/
let gmailRegex = /^\w\@*.*$/
*/

let p2 = parseInt(prompt("De cuanto va a ser el salto?"))
let p1 = prompt("Indique durante cuanto tiempo")
let num = 0;
let idInterval = setInterval(() => {
    if (num > p1) { // Cuando imprimimos 10, paramos el timer para que no se repita más
        window.alert("Trancurrio " + p1 + "s")
        let continuar = prompt("Desea continuar S/N").toUpperCase()
        if (continuar == "S") {
            num = 0;
            p2 = parseInt(prompt("De cuanto va a ser el salto?"))
            p1 = prompt("Indique durante cuanto tiempo")
        }else{
            clearInterval(idInterval);
            //window.location = "https://www.google.es"
        }
    }else{
        console.log(num + "s trancurrido");
        num = num + p2
    }
}, 1000)