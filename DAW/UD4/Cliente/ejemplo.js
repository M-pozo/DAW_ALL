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

/*let array = [];
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
let b = ["1", "2", "3", "4", "5"];*/

//Usando bucle
/*for (let i in b){
    a.splice(3+parseInt(i),0,b[i])
}*/
//a=a.splice(0,3).concat(b.concat(a.splice(3)));

/*a.splice(3,0,...b);
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
let personasAsc = JSON.parse(JSON.stringify(personas));*/
//personasAsc.sort((n1, n2) => n2[1] - n1[1]);
/*personasAsc.sort((n1, n2)=> {
    if (n1[1] === n2[1]) {
        return n1[0] - n2[0]
    }else{
        return n2[1] - n1[1]
    }
}
);*/
/*personasAsc.sort((n1, n2)=> {
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
console.log(personasAsc);*/
/*let enteros =[0,1,2,3,4,5,6,7,8,9,10]
console.log(enteros.every(n => n%2 == 0))
enteros.forEach((num, indice, array) => {
    console.log("Índice "+ indice + " en [" + array + "] es " + num)
});
let sum = 0;
enteros.forEach(num => sum += num)
sum = sum/enteros.length 
enteros.forEach((num) =>{
    if (num > sum) {
        console.log(num);
    }
});

console.log(enteros.map(num => num % 2 == 0));
console.log(enteros.filter(num => num % 2 == 0));

console.log(enteros.reduce((acum, n) => {
    return valor;
}, valInicial)
);*/
/*const mi_objeto ={
    nombre:"miguel"
}
mi_objeto.apllidos="López Vélez";
console.log(mi_objeto.nombre);
console.log(mi_objeto.apellidos);

let nuevo_objeto = mi_objeto;
nuevo_objeto.nombre ="Pepe33";
console.log(mi_objeto.nomrbe);
console.log(mi_objeto['nombre']);

for (const key in mi_objeto) {
    console.log(key)
}
*/
/*const alumno={
    nombre:"Pepe",
    apellidos:"Viruelas Pontebedra",
    genero:"n/a",
    edad:"33",
    nia:"1029374895",
    mochila:{
        bomba:"5367234",
        navaja:"mariposa",
        drogas:"cocaína",
        mujer:"Que es eso?"
    }
}


function queHayEnMiMochila(){
    for (const key in alumno) {
    if(typeof alumno[key]== "object"){
        for (const key2 in alumno[key]) {
            console.log(key2)
        }
    }
}
}
queHayEnMiMochila();

mi_objeto.sacar_asignatura = function(){
    let retorno;
}*/

const miTemperatura={
    temperatura:0,
    get kelvin(){
        return this.temperatura 
    },
    set kelvin(nuevaTemperaturna){
        if (nuevaTemperaturna > 0 && nuevaTemperaturna < 1.4171e32) {
            this.temperatura = nuevaTemperaturna;   
        }
    },
    get celsius(){
        return this.temperatura - 273.15;
    },
    set celsius(nuevaTemperaturna){
        this.temperatura = nuevaTemperaturna + 273.15;   
        
    },
    get farenheit(){
        return (this.temperatura-273)*9/5+32;
    },
    set farenheit(nuevaTemperaturna){
        this.temperatura = (nuevaTemperaturna -32)*5/9+273.15;   
    },
}
console.log(miTemperatura.temperatura)
console.log(miTemperatura.Celsius)