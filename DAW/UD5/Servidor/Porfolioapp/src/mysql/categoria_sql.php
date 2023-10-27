<?php
function get_categorias_por_proyecto($conn, $proyecto_id){
    $categorias_por_proyecto = "SELECT c.nombre
                            FROM categoria_proyecto cp,
                                categoria c
                            WHERE c.id = cp.categoria_id
                                AND cp.proyecto_id = :proy_id ";
    $consulta = $conn->prepare($categorias_por_proyecto);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(":proy_id", $proyecto_id);
    $isOk = $consulta->execute();
    return $consulta->fetchAll();
}
//UD5.3.a BEGIN
function get_categorias_all($conn){
    $categoria_select_all = "SELECT * 
                            FROM categoria";
    $consulta = $conn->prepare($categoria_select_all);
    $resultado = $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->execute();
    return $proyectos = $consulta->fetchAll();
}
//UD5.3.a END
