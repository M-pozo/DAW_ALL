// ALUMNO: MIGUEL POZO PÉREZ
const diccionario = new DiccionarioDeSinonimos();
function DiccionarioDeSinonimos() {
    this.sinonimos = new Map([]);
    
    this.agregarSinonimo = function (palabra, sinonimo) {
        if (this.sinonimos.has(palabra)) {
            //Obtengo el array de la palabra y agrego un nuevo sinónimo al array
            let sinonimosArray = this.sinonimos.get(palabra);
            sinonimosArray.push(sinonimo);
            this.sinonimos.set(palabra, sinonimosArray);
        } else {
            this.sinonimos.set(palabra, [sinonimo]);
        }
    },

    this.obtenerSinonimos = function (palabraConsultar) {
        //Devuelvo el array de la palabra
        return this.sinonimos.get(palabraConsultar);
    },

    this.eliminarSinonimo = function (palabraEliminarSinonimo, sinonimoAEliminar) {
        if (this.sinonimos.has(palabraEliminarSinonimo)) {
            //Obtengo el array de sinonimos y lo filtro para agregar un nuevo array sin la palabra a eliminar.
            let sinonimosArray = this.sinonimos.get(palabraEliminarSinonimo);
            let nuevoArray = sinonimosArray.filter(valor => valor !== sinonimoAEliminar);
            this.sinonimos.set(palabraEliminarSinonimo, nuevoArray);
        }
    },

    this.eliminarPalabra = function (palabraEliminar) {
        this.sinonimos.delete(palabraEliminar);
    }
}

let condicion = true;
while (condicion) {
    const opcion = prompt(
        "Selecciona una opción:\n1. Agregar sinónimo\n2. Obtener sinónimos\n3. Eliminar sinónimo\n4. Eliminar palabra\n5. Salir"
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
            condicion = false;
            break;
        default:
            alert("Opción no válida. Por favor, elige una opción válida.");
    }
}
console.log(diccionario.sinonimos)