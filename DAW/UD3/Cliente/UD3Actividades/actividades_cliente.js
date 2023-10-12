//Miguel Pozo Pérez
//UD3.2.1 BEGIN
/*let repuesta = prompt("Que desea ver un gato o un perro?");
repuesta = repuesta.toLowerCase();
switch (repuesta){
    case 'gato':
        document.write("<img src=\"img/gato.jpg\">");
        break;
    case 'perro':
        document.write("<img src=\"img/perro.jpg\">");
        break;
    default: 
    document.write("Error <br>");
}*/
//UD3.2.1 END

//UD3.2.2 BEGIN
/*let repuestaNumerica = prompt("1 o 2");
repuestaNumerica = parseInt(repuestaNumerica);
switch (repuestaNumerica){
    case 1:
        document.write("<img src=\"img/gato.jpg\">");
        break;
    case 2:
        document.write("<img src=\"img/perro.jpg\">");
        break;
    default: 
    document.write("Error <br>");
}*/
//UD3.2.2 END

//UD3.2.3 BEGIN
/*let repuestaNumerica = prompt("Un número del 1 al 4");
repuestaNumerica = parseInt(repuestaNumerica);
switch (repuestaNumerica){
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
//UD3.2.3 END

//UD3.3.1 BEGIN
/*document.write("<table>");
let filas = prompt("Número de filas");
let columnas = prompt("Número de columnas");
for (let x = 1 ; x <= filas; x++) {
    document.write("<tr>");
    for (let y = 1; y <= columnas; y++) {
        document.write("<td>CELDA"+x+","+y+"</td>");

    }
    document.write("</tr>");
}
document.write("<table>");*/
//UD3.3.1 END

//UD3.3.2 BEGIN
let condicion = "n";
let n = 0;
//Asignamos el número de filas y columnas iniciales
let filas = prompt("Número de filas");
let columnas = prompt("Número de columnas");

//Asignamos donde el usuario quiere parar
let filas2 = prompt("¿En qué fila deseas parar?");
let columnas2 = prompt("¿En qué columna deseas parar?");
/*Iniciamos la tabla y vamos añadiendo filas y columnas con los for()
 - He utilizado dos bucles for para pintar la tabla y después 
 - if encadenados para que el usuario pueda decidir si seguir pintando la tabla o parar la ejecución*/
document.write("<table>");
for (let x = 1 ; x <= filas; x++) {
    document.write("<tr>");
    for (let y = 1; y <= columnas; y++) {
        document.write("<td>CELDA"+x+","+y+"</td>");
        //Añadimos las condiciones para parar la ejecución de la tabla
        if (y == columnas2 && condicion == "n") {
            if (condicion == "n" && n!=1) {
                condicion = prompt("Desea continuar: S/N").toLowerCase();
                n = 1;
                if (condicion == "n") {
                    break;
                }  
            }else{
                break;
            }
        }
    }
    document.write("</tr>");
    if (x == filas2 && condicion == "n") {
        x = filas;
        break;  
    }
}
document.write("<table>");
//UD3.3.2 END

