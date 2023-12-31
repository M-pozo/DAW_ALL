<?php
//UD5.5.a BEGIN
function new_sesion($conn, $id_usuario){
    $new_sesion = 'INSERT INTO sesion (usuario_id)
                    VALUES (:id_us)';
    $consulta = $conn->prepare($new_sesion);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(':id_us', $id_usuario);
    $consulta->execute();
}
//UD5.5.a END
//UD5.6.a BEGIN
function delete_sesion($conn, $id_usuario){
    $delete_sesion = 'DELETE FROM sesion WHERE usuario_id = :id_us';
    $consulta = $conn->prepare($delete_sesion);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(':id_us', $id_usuario);
    $consulta->execute();
}
//UD5.6.a END
?>