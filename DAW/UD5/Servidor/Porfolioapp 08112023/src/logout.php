<?php
include('mysql/sesion_sql.php');
include('mysql/usuario_sql.php');
include('datos.php');
//UD5.6.a BEGIN
$user = get_credenciales_usuario($conn, $_COOKIE['user_email']);
delete_sesion($conn, $user['id']);
setcookie("loggedIn", "false", time() + 84600);
setcookie("user_email", $email, time() - 84600);
//UD5.6.a END
?>
<script type="text/javascript">
    window.location = "/index.php";
</script>