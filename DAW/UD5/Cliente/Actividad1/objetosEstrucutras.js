//ALUMNO: MIGUEL POZO PÉREZ

//1. Objeto window

//Nombre ventana actual(window.name)
console.log(window.name);
//Elementos en el historial ventana(window.history)
console.log(window.history)


//2. Objetos location

//URL página actual
console.log(window.location)

//servidor, ruta y protocolo
console.log(window.location.hostname)
console.log(window.location.pathname)
console.log(window.location.protocol)

// Recargar página actual
//window.location.reload();

// Redirigir a otra página
//window.location.href = 'https://www.google.com';

//3. Objeto navigator

//Navegador
console.log(navigator.userAgent)

//4. Objeto document

//Establecer cookies
document.cookie = 'Curso=2W'
document.cookie = 'Nombre=MiguelPozo'

console.log(document.cookie)

//URL de cada imagen
let imagenes = document.getElementsByTagName('img');
for (let i = 0; i < imagenes.length; i++) {
    console.log(imagenes[i].src);
}

//5. Fechas
let fecha1 = new Date('2023-09-01');
let fecha2 = new Date('2023-09-06');
let resta = (fecha2 - fecha1)
console.log( resta / 1000 / 60 / 60 / 24);

//6. 
let tics = 1;
const temporizador = prompt('Tiempo en segundos (temporizador):');
  setInterval(() => {
    console.log('tic: '+ tics++);
  }, temporizador * 1000);