<?php
function delete_categorias_proyecto($conn, $proyecto_id){
    $delete_categorias = 'DELETE FROM categoria_proyecto WHERE proyecto_id = :pr_id';
    $consulta = $conn->prepare($delete_categorias);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(':pr_id', $proyecto_id);
    $consulta->execute();
}
?>