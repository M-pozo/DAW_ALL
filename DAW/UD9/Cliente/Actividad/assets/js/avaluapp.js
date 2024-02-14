'use strict'
const data = {
    email: 'admin@example.com',
    password: 'gordita2002',
};
const user = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data),
};
let unavariable = fetch('http://localhost:8000/api/auth/jwt/create/', user)
        .await(respuesta => respuesta.json())
        .await(dato => dato['access'])

const get = {
    method: 'GET',
    headers: {
        Authorization: 'Bearer ' + unavariable
    }
}
console.log(get)
fetch('http://localhost:8000/api/modulo_list/', get)
    .then(respuesta => respuesta.json())
        
    