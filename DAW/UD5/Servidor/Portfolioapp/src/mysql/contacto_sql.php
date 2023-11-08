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
function get_contacto($conn, $contacto_id){
    $get_contacto = "SELECT * 
                    FROM contacto
                    WHERE id = :con_id";
    $consulta = $conn->prepare($get_contacto);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(':con_id', $contacto_id);
    $isOk = $consulta->execute();
    return $consulta->fetch();
}
?>