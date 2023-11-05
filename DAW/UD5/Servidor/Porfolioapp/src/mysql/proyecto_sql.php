<?php
include_once("datos.php");
function get_proyectos_all($conn)
{
    $proyecto_select_all = "SELECT * 
                            FROM proyecto";
    $consulta = $conn->prepare($proyecto_select_all);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->execute();
    return $consulta->fetchAll();
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
    if ($consulta->rowCount() == 0) {
        trigger_error("No se ha encontrado el ID de proyecto");
    }
    if ($consulta->rowCount() > 1) {
        trigger_error("Se ha recuperado más de un registro");
    }
    return $consulta->fetch();
}
//UD5.3.c BEGIN
function get_proyectos_por_categoria($conn, $categoria_id)
{
    $proyectos_por_categoria = "SELECT p.*
                                FROM proyecto p
                                JOIN categoria_proyecto cp ON p.id = cp.proyecto_id
                                WHERE cp.categoria_id = :cat_id";
    $consulta = $conn->prepare($proyectos_por_categoria);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(":cat_id", $categoria_id);
    $isOk = $consulta->execute();
    return $consulta->fetchAll();
}
//UD5.3.c END
function get_proyectos_por_categoria_paginado($conn, $categoria_id)
{
    global $paginacion;
    $proyectos_por_categoria_pg = "SELECT p.*
                                FROM proyecto p
                                JOIN categoria_proyecto cp ON p.id = cp.proyecto_id
                                WHERE cp.categoria_id = :cat_id
                                $paginacion";
    $consulta = $conn->prepare($proyectos_por_categoria_pg);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(":cat_id", $categoria_id);
    $isOk = $consulta->execute();
    return $consulta->fetchAll();
}
//UD5.3.d BEGIN
function get_proyectos_order_by($conn, $order)
{
    global $paginacion;
    $proyecto_select_order = "SELECT *
                                FROM proyecto ORDER BY $order $paginacion";
    $consulta = $conn->prepare($proyecto_select_order);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $isOk = $consulta->execute();
    return $consulta->fetchAll();
}
//UD5.3.d END
//UD5.3.f BEGIN
function get_proyectos_paginados($conn)
{
    global $paginacion;
    $proyectos_paginados = "SELECT * FROM proyecto $paginacion";
    $consulta = $conn->prepare($proyectos_paginados);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->execute();
    return  $consulta->fetchAll();
}
//UD5.3.f END
//UD5.6.b BEGIN
function delete_proyecto( $conn, $id ){
    $delete_proyecto = 'DELETE FROM proyecto WHERE id = :id_pr';
    $consulta = $conn->prepare($delete_proyecto);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(':id_pr', $id);
    $consulta->execute();
}
//UD5.6.b END
function create_proyecto($conn, $proyecto){
    $create_proyecto =  'INSERT INTO proyecto (clave, titulo, fecha, descripcion, imagen)
                        VALUES (:clave, :titulo, :fecha, :descripcion, :imagen ) ';
    $consulta = $conn->prepare($create_proyecto);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(':clave', $proyecto['clave']);
    $consulta->bindParam(':titulo', $proyecto['titulo']);
    $consulta->bindParam(':fecha', $proyecto['fecha']);
    $consulta->bindParam(':descripcion', $proyecto['descripcion']);
    $consulta->bindParam(':imagen', $proyecto['imagen']);
    $consulta->execute();
}
//UD5.6.c BEGIN
function update_proyecto( $conn, $proyecto, $id){
    $update_proyecto = "UPDATE proyecto
                        SET clave = :clave, titulo = :titulo, fecha = :fecha, descripcion = :descripcion, imagen = :imagen
                        WHERE id = $id";
    $consulta = $conn->prepare($update_proyecto);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(':clave', $proyecto['clave']);
    $consulta->bindParam(':titulo', $proyecto['titulo']);
    $consulta->bindParam(':fecha', $proyecto['fecha']);
    $consulta->bindParam(':descripcion', $proyecto['descripcion']);
    $consulta->bindParam(':imagen', $proyecto['imagen']);
    $consulta->execute();
}
//UD5.6.c END
