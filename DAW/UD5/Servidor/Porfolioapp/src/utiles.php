<?php
include("mysql/usuario_sql.php");
function anyoActual()
{
    echo date('Y');
}
function actualizarFechas($proyectos)
{
    foreach ($proyectos as  $proyecto) {
        $proyecto['fecha'] = strtotime($proyecto['fecha']);
    }
    return $proyecto;
}
function test_input($data)
{
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
//UD5.3.g BEGIN
function get_user_logged_in($conn, $cookie){
    if (isset($_COOKIE['e-mail'])) {
        $user = get_credenciales_usuario($conn, $cookie);
        if ($user['email'] == $cookie && $user['admin'] == true) {
            return true;
        } else {
            return false;
        }
    }
    return false;
}
//UD5.3.g END
?>
