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

let personas =[
    ["Jose", 35],
    ["María", 74],
    ["Pepe", 40],
    ["Antonio", 18],
    ["Martin", 29],
    ["Javi", 65],
    ["Alejandro", 51],
    ["Mario", 33],
    ["Adrian", 29],
    ["Daniel", 93]
]
console.log(personas)
let personasAsc = JSON.parse(JSON.stringify(personas));
//personasAsc.sort((n1, n2) => n2[1] - n1[1]);
/*personasAsc.sort((n1, n2)=> {
    if (n1[1] === n2[1]) {
        return n1[0] - n2[0]
    }else{
        return n2[1] - n1[1]
    }
}
);*/
personasAsc.sort((n1, n2)=> {
    if ((n2[1]-n1[1]) == 0) {
        if (n1[0] > n2[0]) {
            return 1;
        }
        else if (n1[0]<n2[0]) {
            return -1;
        }else{
            return 0;
        }
    } else {
        return n2[1] - n1[1];
    }
});
console.log(personasAsc);
