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
//Separe en 3 funciones de comparación
function ordenarNombreAsc(n1, n2){
    if (n1[0] > n2[0]) {
        return -1;
      } else if (n1[0] < n2[0]) {
        return 1;
      } else {
        return 0;
      }
}
function ordenarEdadDesc(n2, n1){
    return n2[1] - n1[1];
}

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

// personas.sort((n1, n2)=> {
//     if (n1[2] === n2[2]) {
//         if (n1[1] === n2[1]) {
//             return ordenarEdadDesc(n1, n2)
//         }else{
//            return ordenarNombreAsc(n1, n2)
//         }
//     }else{
//         return ordenarCargo(n1, n2)
//     }
// });

personas
    .sort(ordenarNombreAsc)
    .sort(ordenarEdadDesc)
    .sort(ordenarCargo)

console.log(personas);