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
personas.sort((n1, n2)=> {
        if (n1[2] == "Profesor" && n2[2] == "Administrativo") {
            return -1;
        }
        else if (n1[2] == "Profesor" && n2[2] == "Estudiante") {
            return -1;
        }else if (n1[2] == "Administrativo" && n2[2] == "Estudiante"){
            return 1;
        }else if (n1[2] == "Administrativo" && n2[2] == "Profesor"){
            return 1;
        }else if (n1[2] == "Estudiante" && n2[2] == "Administrativo"){
            return 0;
        }else if (n1[2] == "Estudiante" && n2[2] == "Profesor"){
            return 0;
        }else if (n1[2] == n2[2]){
            if (n1[1] > n2[1]) {
                return 1;
            }
            else if (n1[1]<n2[1]) {
                return -1;
            }else{
                if (n1[0] > n2[0]) {
                    return 1;
                }
                else if (n1[0]<n2[0]) {
                    return -1;
                }else{
                    return 0;
                }
            } 
        }
    
});
console.log(personas);