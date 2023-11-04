<?php
function get_contactos_all($conn)
{
    $contacto_select_all = "SELECT * 
                            FROM contacto";
    $consulta = $conn->prepare($contacto_select_all);
    $resultado = $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->execute();
    return $proyectos = $consulta->fetchAll();
}
?>