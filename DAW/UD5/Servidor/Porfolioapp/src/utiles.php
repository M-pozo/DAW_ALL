<?php
function ordenaTituloProyectoDesc($a, $b)
{
    return strcmp($b['titulo'], $a['titulo']);
}
function ordenaTituloProyectoAsc($a, $b)
{
    return strcmp($a['titulo'], $b['titulo']);
}
//ud3.3.f
function buscadorCategoria($proyecto)
{
    return in_array($_GET['categoria'], $proyecto["categorias"]);
}
//UD4.1.b BEGIN
function buscarUsuario($usuario)
{
    return $_POST['email'] == $usuario["email"];
}
//UD4.1.b END
//UD3.5.a
function anyoActual()
{
    echo date('Y');
}
//UD3.5.b
function actualizarFechas($proyectos)
{
    foreach ($proyectos as  $proyecto) {
        $proyecto['fecha'] = strtotime($proyecto['fecha']);
    }
    return $proyecto;
}
//UD2.5.c
function ordenaFechaProyectoDesc($a, $b)
{
    return strtotime(trim($a['fecha'])) > strtotime(trim($b['fecha']));
}
function ordenaFechaProyectoAsc($a, $b)
{
    return strtotime(trim($b['fecha'])) > strtotime(trim($a['fecha']));
}
function test_input($data)
{
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
function buscarProyecto($proyecto)
{ 
    return $_GET['id'] == $proyecto['clave'];
}
function get_user_logged_in(){
    
}
?>
