<?php include_once("datos.php"); ?>
<?php include_once("utiles.php"); ?>
<?php
//UD4.1.a BEGIN
$emailErr = "";
$passwordErr = "";
$email = $_POST["email"];
$password = $_POST["password"];
//UD4.1.b BEGIN
$user = array_filter($usuarios, 'buscarUsuario');
$user = array_values($user)[0];
//UD4.1.d BEGIN
if (!empty($email) && !empty($password)) {
    if (is_null($user)) {
        $emailErr = "Introduce un e-mail válido";
    }
    if ($email == $user['email'] && $password !== $user['password']) {
        $passwordErr = "Contraseña incorrecta";
    }
    if ($email == $user['email'] && $password == $user['password']) {
        //UD4.1.c UD4.1.e
        setcookie("loggedIn", "true", time() + 84600);
        setcookie("user_email", $email, time() + 84600);
        header('Location: index.php');
        exit;
    }
}
//UD4.1.d END
//UD4.1.b END
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
<!--UD4.1.a END-->

<?php include("templates/footer.php"); ?>