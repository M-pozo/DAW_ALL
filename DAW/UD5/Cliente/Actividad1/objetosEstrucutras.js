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
let fecha1 = new Date('2023-01-01');
let fecha2 = new Date('2023-12-31');

const diasPasados = (fecha2 - fecha1);
console.log(diasPasados);

//6. 
const tiempoX = prompt('Ingrese el tiempo en segundos para el temporizador:');
  setInterval(() => {
    console.log('tics');
  }, tiempoX * 1000); // Multiplicar por 1000 para convertir segundos a milisegundos