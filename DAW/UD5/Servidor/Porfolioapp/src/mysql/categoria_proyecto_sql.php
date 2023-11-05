<?php
function create_categoria_proyecto($conn, $categoria_id, $proyecto_id){
    $create_categoria_proyecto = 'INSERT INTO sesion (categoria_id, proyecto_id)
                                 VALUES (:cat_id, :pr_id)';
    $consulta = $conn->prepare($create_categoria_proyecto);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(':cat_id', $categoria_id);
    $consulta->bindParam(':pr_id', $proyecto_id);
    $consulta->execute();
}
?>