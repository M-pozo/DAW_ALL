<?php
function ordenaTituloProyectoDesc($a, $b)
{
    return strcmp($b['titulo'], $a['titulo']);
};
function ordenaTituloProyectoAsc($a, $b)
{
    return strcmp($a['titulo'], $b['titulo']);
};
//ud3.3.f
function buscadorCategoria($proyecto)
{
    return in_array($_GET['categoria'], $proyecto["categorias"]);
};
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
