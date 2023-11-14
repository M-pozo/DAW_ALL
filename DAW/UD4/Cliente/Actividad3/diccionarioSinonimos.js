// ALUMNO: MIGUEL POZO PÉREZ
const diccionario = new DiccionarioDeSinonimos();
function DiccionarioDeSinonimos() {
    this.sinonimos = new Map([]);
    
    this.agregarSinonimo = function (palabra, sinonimo) {
        /*
        Primero: TERNARIO
        si existe palabra con el sinonimo hacemos push del nuevo sinonimo al array
        si no existe agregamos el array con el nuevo sinonimo
        Segundo: SET
        Hacemos set de la palabra con el array de sinonimos 
        */
        this.sinonimos.set(palabra, this.sinonimos.has(palabra) ? this.sinonimos.get(palabra).push(sinonimo) : [sinonimo])
    },
    this.obtenerSinonimos = function (palabraConsultar) {
        this.sinonimos.get(palabraConsultar)
    },
    this.eliminarSinonimo = function (palabraEliminarSinonimo, sinonimoAEliminar) {
        /*
        Primero FILTER
        filtro el array de la palabra asociada y elimino el sinonimo del array.
        */
        //this.sinonimos.get(palabraEliminarSinonimo).filter(function(valor){ return valor == sinonimoAEliminar ? true : false;});
        this.sinonimos.delete(palabraEliminarSinonimo, this.sinonimos.get(palabraEliminarSinonimo).filter(function (valor) { return valor == sinonimoAEliminar ? true : false; }))
    },
    this.eliminarPalabra = function (palabraEliminar) {
        this.sinonimos.delete(palabraEliminar)
    }
}
whileSt:
while (true) {
    const opcion = prompt(
        "Selecciona una opción:\n1. Agregar sinónimo\n2. Obtener sinónimos\n3. Eliminarsinónimo\n4. Eliminar palabra\n5. Salir"
    );
    switch (opcion) {
        case "1":
            const palabra = prompt("Ingresa una palabra:");
            const sinonimo = prompt("Ingresa un sinónimo:");
            diccionario.agregarSinonimo(palabra, sinonimo);
            break;
        case "2":
            const palabraConsultar = prompt("Ingresa una palabra a consultar:");
            const sinonimos = diccionario.obtenerSinonimos(palabraConsultar);
            console.log(sinonimos);
            break;
        case "3":
            const palabraEliminarSinonimo = prompt("Ingresa una palabra:");
            const sinonimoAEliminar = prompt("Ingresa el sinónimo a eliminar:");
            diccionario.eliminarSinonimo(palabraEliminarSinonimo, sinonimoAEliminar);
            break;
        case "4":
            const palabraEliminar = prompt("Ingresa una palabra a eliminar:");
            diccionario.eliminarPalabra(palabraEliminar);
            break;
        case "5":
            alert("Saliendo del programa");
            break whileSt;
        default:
            alert("Opción no válida. Por favor, elige una opción válida.");
    }
}
