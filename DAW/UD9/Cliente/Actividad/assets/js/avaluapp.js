'use strict'
function limpiarTablas() {
    const contenedores = document.querySelectorAll('#ra_list, #modulo_list, #ce_list, #modulo_detail');
    
    contenedores.forEach(contenedor => {
        const tabla = contenedor.querySelector('table');
        const button = contenedor.querySelector('button');
        const form = contenedor.querySelector('form');
        if (tabla) {
            contenedor.removeChild(tabla);
        }if (form) {
            contenedor.removeChild(form);
            contenedor.removeChild(button);
        }if (button) {
            contenedor.removeChild(button);
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
        const ra = data.results; // Obtener la lista de módulos de los resultados
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
                
        const button = document.createElement('button')
        button.textContent = 'Crear'
        button.addEventListener('click', () => {
            createForm(list);
        });
        
        if (list == 'ra_list') {
            ra_list.appendChild(tabla);
            ra_list.appendChild(button);
        }else if (list == 'modulo_list'){
            modulo_list.appendChild(tabla);
            modulo_list.appendChild(button);
        }else if (list == 'ce_list'){
            ce_list.appendChild(tabla);
            ce_list.appendChild(button);
        }
    })
    .catch(error => {
        console.error('Error al obtener la lista de módulos:', error);
    });
}

document.getElementById('ra').addEventListener('click', function(event) {
    crearTabla('ra_list')
})
document.getElementById('modulo').addEventListener('click', function(event) {
    crearTabla('modulo_list')
})
document.getElementById('ce').addEventListener('click', function(event) {
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
        const button = document.createElement('button')
        button.textContent = 'Eliminar'
        button.id = 'delete'
        button.addEventListener('click', () => {
            eliminarRegistro(list, valorId);
        });

        const button2 = document.createElement('button')
        button2.textContent = 'Actualizar'
        button2.id = 'actualizar'
        button2.addEventListener('click', () => {
            actualizarRegistro(list, valorId);
        });

        modulo_detail.appendChild(tabla);
        modulo_detail.appendChild(button);
        modulo_detail.appendChild(button2);
    })
    .catch(error => {
        console.error('Error al obtener los detalles del módulo:', error);
    });
}

function createForm(list) {
    limpiarTablas()
    let data;
    let formFields = [];

    if (list === 'modulo_list') {
        data = {
            codigo: 'email',
            nombre: 'password',
        };
    } else if (list === 'ra_list') {
        data = {
            codigo: 'email',
            descripcion: 'password',
            modulo: 'password',
        };
    } else if (list === 'ce_list') {
        data = {
            codigo: 'email',
            descripcion: 'password',
            minimo: 'email',
            resultado_aprendizaje: 'password',
        };
    }

    // Crear un array de campos de formulario
    for (let key in data) {
        formFields.push({ name: key, type: 'text'});
    }

    // Crear el formulario
    const form = document.createElement('form');
    form.setAttribute('id', `${list}_form`);

    // Crear los campos de formulario
    formFields.forEach(field => {
        const label = document.createElement('label');
        label.textContent = `${field.name}: `;
        const input = document.createElement('input');
        input.setAttribute('type', field.type);
        input.setAttribute('name', field.name);
        input.setAttribute('required', true); // Marcar como requerido
        form.appendChild(label);
        form.appendChild(input);
        form.appendChild(document.createElement('br'));
    });

    // Agregar un botón de envío
    const submitButton = document.createElement('button');
    submitButton.textContent = 'Enviar';
    form.appendChild(submitButton);

    // Agregar el formulario al documento
    if (list == 'ra_list') {
        ra_list.appendChild(form);
    }else if (list == 'modulo_list'){
        modulo_list.appendChild(form);
    }else if (list == 'ce_list'){
        ce_list.appendChild(form);
    }

    document.getElementById(`${list}_form`).addEventListener('submit', function(event) {
        event.preventDefault(); // Evitar que se envíe el formulario de forma tradicional
    
        // Obtener los valores de los campos del formulario
        const formData = new FormData(this);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });
        console.log(data)
        // Construir la solicitud POST
        const token = localStorage.getItem("token");
        const post = {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        };
    
        // Enviar la solicitud POST al endpoint correspondiente
        let detail
        if (list == 'ra_list') {
            detail = 'ra_detail'
        }else if (list == 'modulo_list'){
            detail = 'modulo_detail'
        }else if (list == 'ce_list'){
            detail = 'ce_detail'
        }
        fetch('http://localhost:8000/api/'+detail+'/', post)
        limpiarTablas()
    });
    
}

function eliminarRegistro(list, valorId) {
    limpiarTablas();
    var token = localStorage.getItem("token");
    const eliminar = {
        method: 'DELETE',
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
    fetch('http://localhost:8000/api/'+detail+'/'+valorId+'/', eliminar)
}

/*function actualizarRegistro(list, valorId) {
    limpiarTablas()
    let data;
    let formFields = [];

    if (list === 'modulo_list') {
        data = {
            codigo: 'email',
            nombre: 'password',
        };
    } else if (list === 'ra_list') {
        data = {
            codigo: 'email',
            descripcion: 'password',
            modulo: 'password',
        };
    } else if (list === 'ce_list') {
        data = {
            codigo: 'email',
            descripcion: 'password',
            minimo: 'email',
            resultado_aprendizaje: 'password',
        };
    }

    // Crear un array de campos de formulario
    for (let key in data) {
        formFields.push({ name: key, type: 'text'});
    }

    // Crear el formulario
    const form = document.createElement('form');
    form.setAttribute('id', `${list}_form`);

    // Crear los campos de formulario
    formFields.forEach(field => {
        const label = document.createElement('label');
        label.textContent = `${field.name}: `;
        const input = document.createElement('input');
        input.setAttribute('type', field.type);
        input.setAttribute('name', field.name);
        input.setAttribute('required', true); // Marcar como requerido
        form.appendChild(label);
        form.appendChild(input);
        form.appendChild(document.createElement('br'));
    });

    // Agregar un botón de envío
    const submitButton = document.createElement('button');
    submitButton.textContent = 'Enviar';
    form.appendChild(submitButton);

    // Agregar el formulario al documento
    if (list == 'ra_list') {
        ra_list.appendChild(form);
    }else if (list == 'modulo_list'){
        modulo_list.appendChild(form);
    }else if (list == 'ce_list'){
        ce_list.appendChild(form);
    }

    document.getElementById(`${list}_form`).addEventListener('submit', function(event) {
        event.preventDefault(); // Evitar que se envíe el formulario de forma tradicional
        const formData = new FormData(this);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });
    
        console.log(data)
        // Construir la solicitud PUT o PATCH
        const token = localStorage.getItem("token");
        const update = {
            method: 'PUT', // O 'PATCH' dependiendo de tu API
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        };
    
        // Enviar la solicitud PUT o PATCH al endpoint correspondiente
        fetch(`http://localhost:8000/api/${list}/${valorId}/`, update)
    });
}*/