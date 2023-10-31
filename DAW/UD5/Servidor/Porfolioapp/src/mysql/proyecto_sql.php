<?php 
function get_proyectos_all($conn)
{
    $proyecto_select_all = "SELECT * 
                            FROM proyecto";
    $consulta = $conn->prepare($proyecto_select_all);
    $resultado = $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->execute();
    return $proyectos = $consulta->fetchAll();
}

function get_proyecto_detail($conn, $proyecto_id)
{
    $proyecto_select_all = "SELECT * 
                            FROM proyecto 
                            WHERE id = :proy_id";
    $consulta = $conn->prepare($proyecto_select_all);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(":proy_id", $proyecto_id);
    $isOk = $consulta->execute();
    if ($consulta -> rowCount() == 0){
        trigger_error("No se ha encontrado el ID de proyecto");
    }
    if ($consulta -> rowCount() > 1){
        trigger_error("Se ha recuperado más de un registro");
    }
    return $consulta->fetch();
}
//UD5.3.c BEGIN
function get_proyectos_por_categoria($conn, $categoria_id){
    $proyectos_only_categoria = "SELECT *
                                FROM proyecto p
                                JOIN categoria_proyecto cp ON p.id = cp.proyecto_id
                                WHERE cp.categoria_id = :cat_id";
    $consulta = $conn->prepare($proyectos_only_categoria);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(":cat_id", $categoria_id);
    $isOk = $consulta->execute();
    return $consulta->fetchAll();
}
//UD5.3.c END
//UD5.3.d BEGIN
function get_proyectos_order_by($conn, $order ){
    $proyecto_select_order = "SELECT *
                                FROM Proyecto order by $order";
    $consulta = $conn->prepare($proyecto_select_order);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $isOk = $consulta->execute();
    return $consulta->fetchAll();
}
//UD5.3.d END
