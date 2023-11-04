<?php 
include_once("datos.php");
include_once("utiles.php");
include_once("mysql/usuario_sql.php");
include("mysql/sesion_sql.php");
$emailErr = "";
$passwordErr = "";
$email = $_POST["email"];
$password = $_POST["password"];
if (!empty($email) && !empty($password)) {
    $user = get_credenciales_usuario($conn, $email);
    if (($user['email'] !== $email)) {
        $emailErr = "Introduce un e-mail válido";
    } else if (!preg_match("/^(([^<>()\[\]\.,;:\s@\”]+(\.[^<>()\[\]\.,;:\s@\”]+)*)|(\”.+\”))@(([^<>()[\]\.,;:\s@\”]+\.)+[^<>()
        [\]\.,;:\s@\”]{2,})$/", $email)) {
        $emailErr = "Introduzca un e-mail válido.";
    }
    if ($email == $user['email'] && $password !== $user['password']) {
        $passwordErr = "Contraseña incorrecta";
    }
    if ($email == $user['email'] && $password == $user['password']) {
        setcookie("loggedIn", "true", time() + 84600);
        setcookie("user_email", $user['email'], time() + 84600);
        //UD5.5.a BEGIN
        new_sesion($conn, $user['id']);
        //UD5.5.a END
        ?>
            <script type="text/javascript">
                window.location = "/contacto_lista.php";
            </script>
        <?php
    }
}
?>
<?php include("templates/header.php"); ?>
<div class="container">
    <h2 class="mb-5">Log in</h2>
    <div class="row">
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST" enctype="multipart/form-data">
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="emailID" class="form-label">e-mail</label>
                    <input type="text" name="email" value="<?php echo $email; ?>" class="form-control" id="emailID" placeholder="Su e-mail">
                    <span class="text-danger"> <?php echo $emailErr ?> </span>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="passwordID" class="form-label">password</label>
                    <input type="password" name="password" value="<?php echo $password; ?>" class="form-control" id="passwordID" placeholder="Su password">
                    <span class="text-danger"> <?php echo $passwordErr ?> </span>
                </div>
            </div>
            <br>
            <button type="submit" class="btn btn-success">Log in</button>
        </form>
    </div>
</div>
<?php include("templates/footer.php"); ?>