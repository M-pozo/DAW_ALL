
document.write("<h1>Miguel Pozo</h1>");

let repuesta = prompt("Que desea ver un gato o un perro?");
repuesta = repuesta.toLowerCase();
console.log(repuesta);
switch (repuesta){
    case 'gato':
        document.write("<img src=\"img/gato.jpg\">");
        break;
    case 'perro':
        document.write("<img src=\"img/perro.jpg\">");
        break;
    default: 
    document.write("Error");
}