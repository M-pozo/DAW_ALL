<?php
//UD5.5.a BEGIN
function new_sesion($conn, $id_usuario){
    $new_sesion = 'INSERT INTO sesion (usuario)
                    VALUES (:id_usr)';
    $consulta = $conn->prepare($new_sesion);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(':id_usr', $id_usuario);
    $consulta->execute();
}
//UD5.5.a END
?>