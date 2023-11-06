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
function update_usuario($conn, $usuario, $email){
    $update_usuario = "UPDATE usuario
                        SET email = :email, password = :password, nombreApellidos = :nombreApellidos, dni = :dni
                        WHERE email = :cookie;";
    $consulta = $conn->prepare($update_usuario);
    $consulta->setFetchMode(PDO::FETCH_ASSOC);
    $consulta->bindParam(':email', $usuario['email']);
    $consulta->bindParam(':password', $usuario['password']);
    $consulta->bindParam(':nombreApellidos', $usuario['nombreApellidos']);
    $consulta->bindParam(':dni', $usuario['dni']);
    $consulta->bindParam(':cookie', $email);
    $consulta->execute();
}
//UD5.3.e END