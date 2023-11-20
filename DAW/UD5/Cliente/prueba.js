'use strict'

//let subVentana = window.open("https://www.google.es", "nueva", "height=600", "width=800")
//subVentana.close();

//window.location.assign("https://www.google.es")

document.write(navigator.appCodeName);
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