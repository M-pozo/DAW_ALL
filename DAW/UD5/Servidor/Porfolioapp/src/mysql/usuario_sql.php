<?php
//UD5.2.e BEGIN
function get_credenciales_usuario($conn, $email)
{
    $get_usuario_by_email = "SELECT * 
                            FROM usuario
                            WHERE email = :email";
    $consulta = $conn->prepare($get_usuario_by_email);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(':email', $email);
    $isOk = $consulta->execute();
    if ($consulta -> rowCount() == 0){
        trigger_error('No se ha encontrado el ID de proyecto');
    }
    if ($consulta -> rowCount() > 1){
        trigger_error('Se ha recuperado más de un registro');
    }
    return $consulta->fetch();
}
//UD5.2.e END