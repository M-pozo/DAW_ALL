// ALUMNO: Miguel Pozo Pérez
let personas=[
["Adrián",47, "Profesor"],
["Luisa",60, "Profesor"],
["Ana",20, "Estudiante"],
["Blas",36, "Estudiante"],
["Agustín",50, "Profesor"],
["Felipe",25, "Estudiante"],
["Pedro",19, "Estudiante"],
["Zoraida",36, "Estudiante"],
["Juan",36, "Administrativo"],
["Toñi",48, "Administrativo"],
["Juan",16, "Estudiante"],
["Miriam",15, "Estudiante"],
["Rosa",75, "Estudiante"],
["Pepe",31, "Estudiante"],
["Fermín",64, "Estudiante"],
["Jose",47, "Profesor"]
];
/*Primera función de ordenación compara los nombre
si es mayor devuelve -1
si es menor devuelve 1
y si es igual devuelve 0*/
function ordenarNombreAsc(n1, n2){
    if (n1[0] > n2[0]) {
        return -1;
      } else if (n1[0] < n2[0]) {
        return 1;
      } else {
        return 0;
      }
}
/*Segunda función de ordenación compara la edad
si n1 es menor devuelve un valor positivo
si n1 es mayor devuelve un valor negativo
y si es igual devuelve 0*/
function ordenarEdadDesc(n2, n1){
    return n2[1] - n1[1];
}

/*Tercera función de ordenación compara por cargo
*/
function ordenarCargo(n1, n2){
    if (n1[2] === "Profesor") {
        return -1;
      } else if (n2[2] === "Profesor") {
        return 1;
      } else if (n1[2] === "Administrativo") {
        return -1;
      } else if (n2[2] === "Administrativo") {
        return 1;
      } else if (n1[2] === "Estudiante") {
        return -1;
      } else {
        return 1;
      }
}

//Le pasamos las tren funciones de ordenación creadas para ordenar nuestro array
personas
    .sort(ordenarNombreAsc)
    .sort(ordenarEdadDesc)
    .sort(ordenarCargo)

console.log(personas);