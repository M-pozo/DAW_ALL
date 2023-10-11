
document.write("<h1>Miguel Pozo</h1>");

//UD3.2.1 BEGIN
/*let repuesta = prompt("Que desea ver un gato o un perro?");
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
}*/
//UD3.2.3 END
//UD3.2.1 END

//UD3.2.2 BEGIN
//let repuestaNumerica = prompt("Un número del 1 al 4");

/*switch (repuestaNumerica){
    case 1:
        document.write("<img src=\"img/gato.jpg\">");
        break;
    case 2:
        document.write("<img src=\"img/perro.jpg\">");
        break;
    case 3:
        document.write("<img src=\"img/tortuga.jpg\">");
        break;
    case 4:
        document.write("<img src=\"img/lobo.jpg\">");
        break;
    default: 
    document.write("Error <br>");
}*/

//UD3.2.2 END

//UD3.3.1 BEGIN
//UD3.3.2 BEGIN
let condicion = "s"
let x = 1
let y = 1
document.write("<table>");
while (condicion == "s") {
    let filas = prompt("Número de filas");
    let columnas = prompt("Número de columnas");
    for (; x <= filas; x++) {
        document.write("<tr>");
        for (; y <= columnas; y++) {
            document.write("<td>CELDA"+x+","+y+"</td>");
    
        }
        document.write("</tr>");
    }
    condicion = prompt("Desea continuar? S/N");    
}
document.write("<table>");
//UD3.3.2 END
//UD3.3.1 END

