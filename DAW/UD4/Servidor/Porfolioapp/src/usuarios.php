<?php
include("datos.php");
include("utiles.php");
//UD4.3.b BEGIN
$emailErr = $nombreApellidosErr = $dniErr = $passwordErr = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["email"])) {
        $emailErr = "Por favor, introduzca un e-mail";
    } else {
        $email = test_input($_POST["email"]);
        if (!preg_match("/^(([^<>()\[\]\.,;:\s@\”]+(\.[^<>()\[\]\.,;:\s@\”]+)*)|(\”.+\”))@(([^<>()[\]\.,;:\s@\”]+\.)+[^<>()
        [\]\.,;:\s@\”]{2,})$/", $email)) {
            $emailErr = "Introduzca un e-mail válido.";
        }
    }
    if (empty($_POST["nombreApellidos"])) {
        $nombreApellidosErr = "Por favor, introduzca nombre y apellidos";
    } else {
        $nombreApellidos = test_input($_POST["nombreApellidos"]);
        if (!preg_match("/^[A-Za-zÀ-ÖØ-öø-ÿ\']+ [A-Za-zÀ-ÖØ-öø-ÿ\']+ [A-Za-zÀ-ÖØ-öø-ÿ\']+$/", $nombreApellidos)) {
            $nombreApellidosErr = "Introduzca un nombre y dos apellidos.";
        }
    }
    if (empty($_POST["dni"])) {
        $dniErr = "Por favor, introduzca su dni.";
    } else {
        $dni = test_input($_POST["dni"]);
        if (!preg_match("/^[0-9]{8}[A-Za-z]$/", $dni)) {
            $dniErr = "Introduzca un dni válido.";
        }
    }
    if (empty($_POST["password"])) {
        $passwordErr = "Por favor, introduzca su contraseña.";
    } else {
        $password = test_input($_POST["password"]);
    }
    //UD4.3.c.3 BEGIN
    if ($emailErr === "" && $nombreApellidosErr === "" && $dniErr === "" && $passwordErr === "") {
        //UD4.3.c.2 BEGIN
        setcookie("user_email", $email, time() + 84600, '/');
        //UD4.3.c.2 END
        $usuario = array_values(array_filter($usuarios, 'buscarUsuario'))[0];
        $usuario['email'] = $email;
        $usuario['nombreApellidos'] = $nombreApellidos;
        $usuario['dni'] = $dni;
        $usuario['password'] = $password;

        $usuarios[array_keys(array_filter($usuarios, 'buscarUsuario'))[0]] = $usuario;
        $usuario_json = json_encode($usuarios);
        file_put_contents('mysql/usuarios.json', $usuario_json);
        ?>
            <script type="text/javascript">
                window.location = "http://localhost:8080/confirmar_proyecto.php";
            </script>
        <?php
    }
    //UD4.3.c.3 END
}
?>
<?php include("templates/header.php") ?>
<?php foreach ($usuarios as $usuario) : if ($usuario['email'] == $_COOKIE['user_email']) { ?>
        <div class="container">
            <h2 class="mb-5">Mantenimiento</h2>
            <div class="row">
                <form action="<?php /*UD4.2.d*/ echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST" enctype="multipart/form-data">
                    <div class="row">
                        <div class="mb-3 col-sm-6 p-0">
                            <label for="claveID" class="form-label">email</label>
                            <input type="text" name="email" value="<?php echo $usuario['email']; ?>" class="form-control" id="emailID" placeholder="">
                            <span class="text-danger"> <?php echo $emailErr ?> </span>
                        </div>
                    </div>
                    <div class="row">
                        <div class="mb-3 col-sm-6 p-0">
                            <label for="nombreApellidosID" class="form-label">Nombre y apellidos</label>
                            <input type="text" name="nombreApellidos" value="<?php echo $usuario['nombreApellidos']; ?>" class="form-control" id="nombreApellidosID">
                            <span class="text-danger"> <?php echo $nombreApellidosErr ?> </span>
                        </div>
                    </div>
                    <div class="row">
                        <div class="mb-3 col-sm-6 p-0">
                            <label for="dniID" class="form-label">DNI</label>
                            <input type="text" name="dni" value="<?php echo $usuario['dni']; ?>" class="form-control" id="dniID">
                            <span class="text-danger"> <?php echo $dniErr ?> </span>
                        </div>
                    </div>
                    <div class="row">
                        <div class="mb-3 col-sm-6 p-0">
                            <label for="passwordID" class="form-label">Password</label>
                            <input type="password" name="password" value="<?php echo $usuario['password']; ?>" class="form-control" id="passwordID">
                            <span class="text-danger"> <?php echo $passwordErr ?> </span>
                        </div>
                    </div>
                    <br>
                    <button type="submit" class="btn btn-success">Actualizar</button>
                </form>
            </div>
    <?php };
endforeach; ?>
<!--UD4.3.b END-->
    <?php include("templates/footer.php") ?>