<?php
//UD3.3.g
$jsonProyectos = file_get_contents("mysql/proyectos.json");
$proyectos = json_decode($jsonProyectos, true);

$jsonUsuarios = file_get_contents("mysql/usuarios.json");
$usuarios = json_decode($jsonUsuarios, true);

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