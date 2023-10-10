
document.write("<h1>Miguel Pozo</h1>");

//UD3.2.1 BEGIN
let repuesta = prompt("Que desea ver un gato o un perro?");
repuesta = repuesta.toLowerCase();
//UD3.2.3 BEGIN
switch (repuesta){
    case 'gato':
        document.write("<img src=\"img/gato.jpg\">");
        break;
    case 'perro':
        document.write("<img src=\"img/perro.jpg\">");
        break;
    case 'tortuga':
        document.write("<img src=\"img/tortuga.jpg\">");
        break;
    case 'lobo':
        document.write("<img src=\"img/lobo.jpg\">");
        break;
    default: 
    document.write("Error <br>");
}
//UD3.2.3 END
//UD3.2.1 END

//UD3.3.1 BEGIN
let filas = prompt("Número de filas");
let columnas = prompt("Número de columnas");

let condicion = true;

for (let index = 0; index < filas; index++) {
    for (let index = 0; index < columnas; index++) {
        document.write("*");

    }
    document.write("<br>");
}
let  = prompt("Desea continuar? S/N");


//UD3.3.1 END

