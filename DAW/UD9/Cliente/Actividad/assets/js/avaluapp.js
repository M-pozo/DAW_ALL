'use strict'
//Miguel Pozo Pérez
document.getElementById('header').style.display = 'none';

function limpiarTablas() {
    const contenedores = document.querySelectorAll('#ra_list, #modulo_list, #ce_list, #modulo_detail');

    contenedores.forEach(contenedor => {
        const tabla = contenedor.querySelector('table');
        const button = contenedor.querySelectorAll('button');
        const form = contenedor.querySelector('form');
        if (tabla) {
            contenedor.removeChild(tabla);
        } if (form) {
            contenedor.removeChild(form);
        } if (button) {
            button.forEach(btn => contenedor.removeChild(btn));
        }
    });
}

//Enviar formulario de Login
document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();
    
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
            //El codigo es >= 200 <= 300 si no me tira un Error
            if (!response.ok) {
                throw new Error('Unauthorized');
            }
            return response.json();
        })
        .then(data => {
            const token = data.access
            localStorage.setItem('token', token)
            document.getElementById('header').style.display = 'flex';
            document.getElementById('register').style.display = 'none';
        })
        .catch(error => {
            if (error.message === 'Unauthorized') {
                alert('Credenciales incorrectas');
            }
        });
});

function crearTabla(list) {
    limpiarTablas()
    let token = localStorage.getItem("token");
    const get = {
        method: 'GET',
        headers: {
            Authorization: 'Bearer ' + token
        }
    };
    fetch('http://localhost:8000/api/'+list+'/', get)
        .then(response => response.json())
        .then(data => {
            // Obtener la lista de módulos de los resultados
            const registro = data.results;
            //Crear encabezado
            const tabla = document.createElement('table');
            const encabezado = tabla.createTHead();
            const filaEncabezado = encabezado.insertRow();
            const encabezados = ['ID', 'Descripción Corta'];
            encabezados.forEach(encabezado => {
                const th = document.createElement('th');
                th.textContent = encabezado;
                filaEncabezado.appendChild(th);
            });
            // Crear filas
            const cuerpoTabla = tabla.createTBody();
            registro.forEach(valor => {
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
            } else if (list == 'modulo_list') {
                modulo_list.appendChild(tabla);
                modulo_list.appendChild(button);
            } else if (list == 'ce_list') {
                ce_list.appendChild(tabla);
                ce_list.appendChild(button);
            }
        })
        .catch(error => {
            console.error('Error al obtener la lista de módulos:', error);
        });
}

document.getElementById('ra').addEventListener('click', function (event) {
    crearTabla('ra_list')
})
document.getElementById('modulo').addEventListener('click', function (event) {
    crearTabla('modulo_list')
})
document.getElementById('ce').addEventListener('click', function (event) {
    crearTabla('ce_list')
})

function mostrarDetalles(list, valorId) {
    limpiarTablas();
    let token = localStorage.getItem("token");
    const get = {
        method: 'GET',
        headers: {
            Authorization: 'Bearer ' + token
        }
    };
    let detail
    if (list == 'ra_list') {
        detail = 'ra_detail'
    } else if (list == 'modulo_list') {
        detail = 'modulo_detail'
    } else if (list == 'ce_list') {
        detail = 'ce_detail'
    }
    fetch('http://localhost:8000/api/' + detail + '/' + valorId + '/', get)
        .then(response => response.json())
        .then(data => {

            const tabla = document.createElement('table');
            const encabezado = tabla.createTHead();
            const filaEncabezado = encabezado.insertRow();
            let encabezados
            if (list == 'ra_list') {
                encabezados = ['ID', 'Código', 'Descripción', 'Módulo'];
            } else if (list == 'modulo_list') {
                encabezados = ['Codigo', 'ID', 'Nombre'];
            } else if (list == 'ce_list') {
                encabezados = ['ID', 'Código', 'Descripción', 'Mínimo', 'Resultado de Aprendizaje'];
            }
            encabezados.forEach(encabezado => {
                const th = document.createElement('th');
                th.textContent = encabezado;
                filaEncabezado.appendChild(th);
            });

            // Crear Filas segun un parametro (list)
            if (list == 'modulo_list') {
                const fila = tabla.insertRow();
                const celdaCodigo = fila.insertCell();
                celdaCodigo.textContent = data.codigo;
                const celdaId = fila.insertCell();
                celdaId.textContent = data.id;
                const celdaNombre = fila.insertCell();
                celdaNombre.textContent = data.nombre;

            } else if (list == 'ra_list') {
                const fila = tabla.insertRow();
                const celdaId = fila.insertCell();
                celdaId.textContent = data.id;
                const celdaCodigo = fila.insertCell();
                celdaCodigo.textContent = data.codigo;
                const celdaDescripcion = fila.insertCell();
                celdaDescripcion.textContent = data.descripcion;
                const celdaModulo = fila.insertCell();
                celdaModulo.textContent = data.modulo;

            } else if (list == 'ce_list') {
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
            //Agregat Boton Eliminar
            const button = document.createElement('button')
            button.textContent = 'Eliminar'
            button.id = 'delete'
            button.addEventListener('click', () => {
                eliminarRegistro(list, valorId);
            });
            //Agregat Boton Actualizar
            const button2 = document.createElement('button')
            button2.textContent = 'Actualizar'
            button2.id = 'actualizar'
            button2.addEventListener('click', () => {
                actualizarRegistro(list, valorId, data);
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
        formFields.push({ name: key, type: 'text' });
    }

    // Crear el formulario
    const form = document.createElement('form');
    form.id = list+'_form';

    // Crear los campos de formulario
    formFields.forEach(field => {
        const label = document.createElement('label');
        label.textContent = field.name;
        const input = document.createElement('input');
        input.type = field.type;
        input.name = field.name;
        input.required = true
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
    } else if (list == 'modulo_list') {
        modulo_list.appendChild(form);
    } else if (list == 'ce_list') {
        ce_list.appendChild(form);
    }

    document.getElementById(list+'_form').addEventListener('submit', function (event) {
        event.preventDefault();

        // Obtener los valores de los campos del formulario
        const formData = new FormData(this);
        const data = {};
        //Recorre todos el formulario sacando el value de los imputs
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
        } else if (list == 'modulo_list') {
            detail = 'modulo_detail'
        } else if (list == 'ce_list') {
            detail = 'ce_detail'
        }
        fetch('http://localhost:8000/api/'+detail+'/', post).then(limpiarTablas())
    });

}

function eliminarRegistro(list, valorId) {
    limpiarTablas();
    let token = localStorage.getItem("token");
    const eliminar = {
        method: 'DELETE',
        headers: {
            Authorization: 'Bearer ' + token
        }
    };
    let detail
    if (list == 'ra_list') {
        detail = 'ra_detail'
    } else if (list == 'modulo_list') {
        detail = 'modulo_detail'
    } else if (list == 'ce_list') {
        detail = 'ce_detail'
    }
    fetch('http://localhost:8000/api/'+detail+'/'+valorId+'/', eliminar)
}

function actualizarRegistro(list, valorId, valores) {
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
        formFields.push({ name: key, type: 'text' });
    }

    // Crear el formulario
    const form = document.createElement('form');
    form.id = list+'_form';

    // Crear los campos de formulario
    formFields.forEach(field => {
        const label = document.createElement('label');
        label.textContent = field.name;
        const input = document.createElement('input');
        input.type = field.type;
        input.value = valores[field.name];
        input.name = field.name
        input.required = true;
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
    } else if (list == 'modulo_list') {
        modulo_list.appendChild(form);
    } else if (list == 'ce_list') {
        ce_list.appendChild(form);
    }

    document.getElementById(list+'_form').addEventListener('submit', function (event) {
        event.preventDefault();
        //Recoger todos los datos del formulario en pares clave/valor
        const formData = new FormData(this);
        const data = {};
        //Recorre todos el formulario sacando el value de los imputs
        formData.forEach((value, key) => {
            data[key] = value;
        });

        console.log(data)
        const token = localStorage.getItem("token");
        const update = {
            method: 'PUT',
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        };

        let detail
        if (list == 'ra_list') {
            detail = 'ra_detail'
        } else if (list == 'modulo_list') {
            detail = 'modulo_detail'
        } else if (list == 'ce_list') {
            detail = 'ce_detail'
        }
        
        fetch('http://localhost:8000/api/'+detail+'/'+valorId+'/', update).then(limpiarTablas())
        
    });
}