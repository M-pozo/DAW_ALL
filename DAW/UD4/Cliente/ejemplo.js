/*let filas = prompt("Número de filas");
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
*/

let array = [];
array.push("Bocata")
array.push("Jamón")
array.push("con tozino")
array.unshift("Primer")
document.write(array)
console.log(array)
console.log(array.join('*'))
document.write('<p>'+array.join('</p><p>')+'</p>')

let subArray = array.slice(1, 3);
console.log(subArray);

let a = ['a', 'b', 'c', 'd', 'e'];
let b = ["1", "2", "3", "4", "5"];

//Usando bucle
/*for (let i in b){
    a.splice(3+parseInt(i),0,b[i])
}*/
//a=a.splice(0,3).concat(b.concat(a.splice(3)));

a.splice(3,0,...b);
console.log(a);

a.push(11)