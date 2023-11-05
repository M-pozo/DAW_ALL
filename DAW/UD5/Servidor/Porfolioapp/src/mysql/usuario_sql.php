<?php
//UD5.3.e BEGIN
function get_credenciales_usuario($conn, $email)
{
    $get_usuario_by_email = "SELECT * 
                            FROM usuario
                            WHERE email = :email";
    $consulta = $conn->prepare($get_usuario_by_email);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(':email', $email);
    $isOk = $consulta->execute();
    return $consulta->fetch();
}
//UD5.3.e END