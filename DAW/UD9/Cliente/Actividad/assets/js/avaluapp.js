'use strict'
function limpiarTablas() {
    const contenedores = document.querySelectorAll('#ra_list, #modulo_list, #ce_list, #modulo_detail');
    
    contenedores.forEach(contenedor => {
        const tabla = contenedor.querySelector('table');
        if (tabla) {
            contenedor.removeChild(tabla);
        }
    });
}
//Funciones para esconder y mostrar contenedores
function ocultarContenedor(className) {
    const contendor = document.getElementsByClassName(className);
    for (let i = 0; i < contendor.length; i++) {
        contendor[i].style.display = 'none';
    }
}
function mostrarContenedor(className) {
    const contendor = document.getElementsByClassName(className);
    for (let i = 0; i < contendor.length; i++) {
        contendor[i].style.display = 'flex';
    }
}

ocultarContenedor('header')

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar que se envíe el formulario de forma tradicional

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const data = {
        email: email,
        password: password,
    };
    
    const user = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    };
    
    fetch('http://localhost:8000/api/auth/jwt/create/', user)
        .then(response => {
            if (!response.ok) {
                throw new Error('Unauthorized');
            }
            return response.json();
        })
        .then(data => {
            const token = data.access
            localStorage.setItem('token', token)
            mostrarContenedor('header');
            ocultarContenedor('register');
        })
        .catch(error => {
            if (error.message === 'Unauthorized') {
                console.error('Error de autenticación: Credenciales incorrectas');
                alert('Credenciales incorrectas');
            } else {
                console.error('Error al autenticar usuario:', error);
            }
            mostrarContenedor('register');
            ocultarContenedor('header');
        });
});

function crearTabla(list) {
    limpiarTablas()
    var token = localStorage.getItem("token");
    const get = {
        method: 'GET',
        headers: {
            Authorization: 'Bearer ' + token
        }
    };
    fetch('http://localhost:8000/api/'+list+'/', get)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        const ra = data.results; // Obtener la lista de módulos de los resultados
        console.log(ra)
        // Crear una tabla HTML
        const tabla = document.createElement('table');
        
        // Crear la fila de encabezado de la tabla
        const encabezado = tabla.createTHead();
        const filaEncabezado = encabezado.insertRow();
        const encabezados = ['ID', 'Descripción Corta']; // Encabezados de la tabla
        encabezados.forEach(encabezado => {
            const th = document.createElement('th');
            th.textContent = encabezado;
            filaEncabezado.appendChild(th);
        });
        
        // Crear filas de datos para cada módulo
        const cuerpoTabla = tabla.createTBody();
        ra.forEach(valor => {
            const fila = cuerpoTabla.insertRow();
            const celdaId = fila.insertCell();
            celdaId.textContent = valor.id;
            const celdaDescripcion = fila.insertCell();
            celdaDescripcion.textContent = valor.descripcion_short;

            fila.addEventListener('click', () => {
                mostrarDetalles(list, valor.id);
            });
        });
        
        // Agregar la tabla al elemento contenedor en el HTML
        if (list == 'ra_list') {
            ra_list.appendChild(tabla);
        }else if (list == 'modulo_list'){
            modulo_list.appendChild(tabla);
        }else if (list == 'ce_list'){
            ce_list.appendChild(tabla);
        }
        
        
    })
    .catch(error => {
        console.error('Error al obtener la lista de módulos:', error);
    });
}

document.getElementById('ra').addEventListener('click', function(event) {
    event.preventDefault();
    crearTabla('ra_list')
})
document.getElementById('modulo').addEventListener('click', function(event) {
    event.preventDefault();
    crearTabla('modulo_list')
})
document.getElementById('ce').addEventListener('click', function(event) {
    event.preventDefault();
    crearTabla('ce_list')
})

function mostrarDetalles(list, valorId) {
    limpiarTablas();
    var token = localStorage.getItem("token");
    const get = {
        method: 'GET',
        headers: {
            Authorization: 'Bearer ' + token
        }
    };
    let detail
    if (list == 'ra_list') {
        detail = 'ra_detail'
    }else if (list == 'modulo_list'){
        detail = 'modulo_detail'
    }else if (list == 'ce_list'){
        detail = 'ce_detail'
    }
    fetch('http://localhost:8000/api/'+detail+'/'+valorId+'/', get)
    .then(response => response.json())
    .then(data => {
        console.log(data);

        // Crear una tabla HTML
        const tabla = document.createElement('table');
        
        // Crear la fila de encabezado de la tabla
        const encabezado = tabla.createTHead();
        const filaEncabezado = encabezado.insertRow();
        let encabezados
        if (list == 'ra_list') {
            encabezados = ['ID', 'Código', 'Descripción' ,'Módulo'];
        }else if (list == 'modulo_list'){
            encabezados = ['Codigo', 'ID', 'Nombre'];
        }else if (list == 'ce_list'){
            encabezados = ['ID', 'Código', 'Descripción' ,'Mínimo', 'Resultado de Aprendizaje'];
        }
        encabezados.forEach(encabezado => {
            const th = document.createElement('th');
            th.textContent = encabezado;
            filaEncabezado.appendChild(th);
        });
        
        // Crear fila de datos para el módulo
        if (list == 'modulo_list') {
            const fila = tabla.insertRow();
            const celdaCodigo = fila.insertCell();
            celdaCodigo.textContent = data.codigo;
            const celdaId = fila.insertCell();
            celdaId.textContent = data.id;
            const celdaNombre = fila.insertCell();
            celdaNombre.textContent = data.nombre;

        }else if (list == 'ra_list'){
            const fila = tabla.insertRow();
            const celdaId = fila.insertCell();
            celdaId.textContent = data.id;
            const celdaCodigo = fila.insertCell();
            celdaCodigo.textContent = data.codigo;
            const celdaDescripcion = fila.insertCell();
            celdaDescripcion.textContent = data.descripcion;
            const celdaModulo = fila.insertCell();
            celdaModulo.textContent = data.modulo;

        }else if (list == 'ce_list'){
            const fila = tabla.insertRow();
            const celdaId = fila.insertCell();
            celdaId.textContent = data.id;
            const celdaCodigo = fila.insertCell();
            celdaCodigo.textContent = data.codigo;
            const celdaDescripcion = fila.insertCell();
            celdaDescripcion.textContent = data.descripcion;
            const celdaMinimo = fila.insertCell();
            celdaMinimo.textContent = data.minimo;
            const celdaRA = fila.insertCell();
            celdaRA.textContent = data.resultado_aprendizaje;
        }
        

        // Agregar la tabla al elemento contenedor en el HTML
        modulo_detail.appendChild(tabla);
    })
    .catch(error => {
        console.error('Error al obtener los detalles del módulo:', error);
    });
}


