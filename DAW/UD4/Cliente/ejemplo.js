//UD3.3.1 BEGIN
let filas = prompt("Número de filas");
let columnas = prompt("Número de columnas");
let array = []
let random = parseInt(Math.random() * 100)
for (let x = 0 ; x < filas; x++) {
    array[x] = [];
    for (let y = 0; y < columnas; y++) {
        array[x][y] = parseInt(Math.random() * 100);
    }
    //array[x] = JSON.parse(JSON.stringify(array2))
}
console.log(array)
//UD3.3.1 END