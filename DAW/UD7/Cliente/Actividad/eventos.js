//MIGUEL POZO PÉREZ
let nombre = document.createElement("h1");
    nombre.textContent = "MIGUEL POZO PÉREZ";
    document.body.appendChild(nombre);

//----------------------------------------------------------------------------


let tarea1 = document.createElement("h1");
    tarea1.textContent = "Tarea1";
    document.body.appendChild(tarea1);


//UD7 Tarea 1
let contenedor = document.createElement("div");
    contenedor.style.height = "100px";
    contenedor.style.width = "100px";
    contenedor.style.backgroundColor = "black";
    document.body.appendChild(contenedor);

let parrafo = document.createElement("p");
    parrafo.textContent = "Pulsa aquí";
    parrafo.style.color = "white";
    contenedor.appendChild(parrafo);

contenedor.addEventListener("click", function () {
    window.alert("Pulsaste sobre el div");
})


//-------------------------------------------------------------------------------------------


let tarea2 = document.createElement("h1");
    tarea2.textContent = "Tarea2";
    document.body.appendChild(tarea2);


//UD7 Tarea 2
let div1 = document.createElement("div");
    div1.style.height = "100px";
    div1.style.width = "100px";
    document.body.appendChild(div1);

let contenidoDiv1 = document.createElement("p");
    contenidoDiv1.textContent = "Pasa por aqui";
    div1.appendChild(contenidoDiv1);

let div2 = document.createElement("div");
    div2.id = "efecto"
    div2.style.backgroundColor = "red";
    div2.style.height = "100px";
    div2.style.width = "100px";
    document.body.appendChild(div2);

let contenidoDiv2 = document.createElement("p");
    contenidoDiv2.textContent = "Efectos del movimiento";
    div2.appendChild(contenidoDiv2);

div1.addEventListener("mouseenter", function () {
    div2.style.backgroundColor = "green";
})

div1.addEventListener("mouseleave", function () {
    div2.style.backgroundColor = "red";
})


//----------------------------------------------------------------------


let tarea3 = document.createElement("h1");
    tarea3.textContent = "Tarea3";
    document.body.appendChild(tarea3);


//UD7 Tarea 3
let form = document.createElement("form");
    document.body.appendChild(form);

let input = document.createElement("input");
    input.type = "number"
    input.readonly = true;
    input.id = "n1"
    form.appendChild(input);

let input2 = document.createElement("input");
    input2.type = "number"
    input2.readonly = true
    input2.id = "n2"
    form.appendChild(input2);

let text = document.createElement("input");
    text.type = "text"
    text.id = "resultado"
    form.appendChild(text);

let button = document.createElement("button")
    button.textContent = "Enviar"
    button.onclick = function(event) {
        //Evita la recarga de la página
        event.preventDefault();
        let n1 = parseFloat(document.getElementById("n1").value)
        let n2 = parseFloat(document.getElementById("n2").value)
        
        document.getElementById('resultado').value = n1 * n2;
    }
    form.appendChild(button);


//-----------------------------------------------------------------------------


let tarea4 = document.createElement("h1");
    tarea4.textContent = "Tarea4 y 5";
    document.body.appendChild(tarea4);


//UD7 Tarea 4
function generarTablero(event) {
    //Evita la recarga de la página
    event.preventDefault();
    let tamaño = document.getElementById('tamaño').value;

    //verifico que sea un número de 4 a 8
    if (tamaño >= 4 && tamaño <= 8) {
        let tableroDiv = document.getElementById('tablero');
        for (let i = 1; i <= tamaño; i++) {
            let fila = document.createElement('div');
            fila.classList.add('fila')
            tableroDiv.appendChild(fila);
            for (let j = 1; j <= tamaño; j++) {
                let casilla = document.createElement('div');
                fila.appendChild(casilla);
                //sumo la i y la j para pintar bien.
                if ((i + j) % 2 === 0) {
                    casilla.classList.add('blanco');
                } else {
                    casilla.classList.add('negro');
                }

                //UD7 Tares 5 -- Mostrar posición
                casilla.addEventListener('click', function() {
                    alert('Posición: ' + i + ',' + j);
                });

            }
        }
    } else {
        alert("El tamaño debe estar entre 4 y 8.");
    }
}

let form2 = document.createElement("form");
    document.body.appendChild(form2);

let input3 = document.createElement("input");
    input3.id = "tamaño"
    form2.appendChild(input3);

let button2 = document.createElement("button");
    button2.textContent = "Generar tablero";
    button2.onclick = generarTablero;
    form2.appendChild(button2);

let tableroDiv = document.createElement("div");
    tableroDiv.id = "tablero";
    tableroDiv.classList.add("tablero");
    document.body.appendChild(tableroDiv);

let style = document.createElement('style');
style.textContent = `
    .tablero{
        display: block;
    }
    .fila{
        display: block;

    }
    .negro, .blanco{
        display: inline-block;
        width: 50px;
        height: 50px;
    }

    .negro{
        background-color: black;
    }
`;
document.head.appendChild(style);


//-------------------------------------------------------


let tarea6 = document.createElement("h1");
    tarea6.textContent = "Tarea6";
    document.body.appendChild(tarea6);


//UD7 Tarea 6
let input4 = document.createElement('input');
    input4.type = 'text';
    input4.id = 'email';
    input4.placeholder = 'Introducir email';
    document.body.appendChild(input4);

let button3= document.createElement('button');
    button3.textContent = 'Comprobar email';
    button3.addEventListener('click', comprobarEmail);
    document.body.appendChild(button3);

//Función para comprobar el correo electrónico
function comprobarEmail() {
    // Expresión regular
    let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    let emailValue = document.getElementById('email').value;

    //Método test comprueba si la expresión coincide
    if (emailRegex.test(emailValue)) {
    alert('Válido');
    } else {
    alert('Incorrecto');
    }
}


//---------------------------------------------------------------------------------


let tarea7 = document.createElement("h1");
    tarea7.textContent = "Tarea7";
    document.body.appendChild(tarea7);

//UD7 Tarea7



//-----------------------------------------------------------------------------------------------


let tarea8 = document.createElement("h1");
    tarea8.textContent = "Tarea8";
    document.body.appendChild(tarea8);

//UD7 Tarea 8
let buscador = document.createElement('input');
    buscador.type = 'text';
    buscador.id = 'buscador';
    document.body.appendChild(buscador);

let divAnimal = document.createElement('div');
    divAnimal.classList.add('divAnimal');
    document.body.appendChild(divAnimal);

// Array de animales
let animalList = ['perro', 'gato', 'pollo', 'pelícano', 'grulla', 'león', 'liebre', 'lince'];

// Crear los divs de animales
for (let i = 0; i < animalList.length; i++) {
    let div = document.createElement('div');
    div.classList.add('animal');
    div.textContent = animalList[i];
    divAnimal.appendChild(div);
}

// Añadir evento de entrada al campo de texto
buscador.addEventListener('input', function() {
    let resultado = buscador.value.toLowerCase();
    //Encuentra todas las coincidencias con el class="animal" y lo almacena en un array
    let divs = document.querySelectorAll('.animal');
    //Creo una instancia para comparar el resultado con la búsqueda la "i" significa que dará true con las letras independiente 
    let regex = new RegExp(resultado, 'i');
    let coincidencias = false;

    //Recorro las coincidencias, guardo su valor en una variable y utilizo la función test de la instancia Regex para determinar las coincidencias
    divs.forEach(div => {
        let animalNombre = div.textContent.toLowerCase();

        if (regex.test(animalNombre)) {
            div.classList.remove('red');
            div.classList.add('green');
            coincidencias = true;
        } else {
            div.classList.remove('green');
            div.classList.add('red');
        }
    });

    if (!coincidencias) {
        alert('No hay coincidencias');
    }
});

let style2 = document.createElement('style');
style2.textContent = ` 
    .divAnimal {
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }
    
    .animal {
        display: inline-block;
        width: 100px;
        height: 50px;
        border: 1px solid black;
        margin: 5px;
    }
    
    .green {
        background-color: green;
    }
    
    .red {
        background-color: red;
    }
`;
document.head.appendChild(style2);


