<?php
//UD3.3.g
$json = file_get_contents("mysql/proyectos.json");
$proyectos = json_decode($json, true);

//UD3.3.a and UD3.3.b BEGIN 
/* $proyectos = [ 
    [
        "clave" => "proyecto1",
        "titulo" => "Porfolio",
        "descripcion" => "Mostrar todos mis proyectos",
        "imagen" => "",
        "fecha" => "24/09/2022",
        "categorias" => ["css", "javascript"]
    ],
    [
        "clave" => "proyecto2",
        "titulo" => "Torneo",
        "descripcion" => "Utilizar la API de un juego para coguer los datos de los participantes",
        "imagen" => "static/images/torneo.png",
        "fecha" => "14/02/2023",
        "categorias" => ["php", "javascript"]
    ],
    [
        "clave" => "proyecto3",
        "titulo" => "MyFilms",
        "descripcion" => "Almacenar y categorizar peliculas segun mis reseñas",
        "imagen" => "static/images/pelicula.png",
        "fecha" => "12/11/2021",
        "categorias" => ["php", "javascript"]
    ],
    [
        "clave" => "proyecto4",
        "titulo" => "Juego 2D",
        "descripcion" => "Juego web 2D de plataformas",
        "imagen" => "static/images/juego2d.png",
        "fecha" => "29/12/2022",
        "categorias" => ["php", "javascript"]
    ],
    [
        "clave" => "proyecto5",
        "titulo" => "Ropa",
        "descripcion" => "Venta de ropa de segunda mano",
        "imagen" => "static/images/ropa.png",
        "fecha" => "16/04/2020",
        "categorias" => ["php", "javascript"]
    ],
]; */
//UD3.3.a and UD3.3.b END

$categorias = [
    "php" => "PHP",
    "javascript" => "JavaScript",
    "java" => "Java",
    "html" => "HTML",
    "css" => "CSS",
    "python" => "Python"
];

//UD3.2.c
$nombre = [
    "nombre" => "Miguel Pozo"
];

$jsonUsuarios = file_get_contents("./mysql/usuarios.json");
$usuarios = json_decode($jsonUsuarios, true);
?>