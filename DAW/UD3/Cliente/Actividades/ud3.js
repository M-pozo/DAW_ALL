'use strict'
function miFuncion(a) {
    let
    potencia = 10;
    return a * potencia; //Devuelve a multiplicado por 10
}
console.log(miFuncion('1e1'));

let nano = 33 + false + '';
console.log(nano);

if (nano == 33){
    console.log("padreada");
}
let limit = 5;
for (let i = 1, j = limit; i <= limit && j > 0; i++, j--) {
console.log(i + " - " + j);
}

let a =["a","b","c"];
for (let i = 0; i < a.length(); i++) {
    console.log(a[i]);
}
for (let k of a) {
    console.log(k);
}
for (let id in a) {
    console.log(id);
}