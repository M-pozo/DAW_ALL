<?php
include("datos.php");
include("utiles.php");
//UD4.2.c BEGIN
$user = array_filter($usuarios, 'buscarUsuario');
$user = array_values($user)[0];
$emailErr = $nombreApellidosErr = $dniErr = $passwordErr = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (is_null($user)) {
        $emailErr = "Introduce un e-mail válido";
    } else if (!preg_match("/^(([^<>()\[\]\.,;:\s@\”]+(\.[^<>()\[\]\.,;:\s@\”]+)*)|(\”.+\”))@(([^<>()[\]\.,;:\s@\”]+\.)+[^<>()
        [\]\.,;:\s@\”]{2,})$/", $email)) {
        $emailErr = "Introduzca un e-mail válido.";
    }
    var_dump($user);
    die();
    if ($email == $user['email'] && $password !== $user['password']) {
        $passwordErr = "Contraseña incorrecta";
    }
    if ($emailErr === "" && $nombreApellidosErr === "" && $dniErr === "" && $passwrodErr === "") {
        /*$proyectos = [
            "clave" => $clave,
            "titulo" => $titulo,
            "descripcion" => $descripcion,
            "imagen" => $pathImagen,
            "fecha" => $fecha,
            "categorias" => ['css'],
        ];
        $tempArray = json_decode(file_get_contents('mysql/proyectos.json'), true);
        if ($tempArray === NULL) {
            $tempArray = [];
        }
        array_push($tempArray, $proyectos);
        $proyectos_json = json_encode($tempArray);
        file_put_contents('mysql/proyectos.json', $proyectos_json);
?>
        <script type="text/javascript">
            window.location = "http://localhost:8080/confirmar_proyecto.php";
        </script>
<?php*/
    }
}
//UD4.2.c END
?>
<?php include("templates/header.php") ?>
<div class="container">
    <h2 class="mb-5">Mantenimiento</h2>
    <div class="row">
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST" enctype="multipart/form-data">
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="claveID" class="form-label">email</label>
                    <input type="text" name="email" value="<?php echo $email; ?>" class="form-control" id="emailID" placeholder="">
                    <span class="text-danger"> <?php echo $emailErr ?> </span>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="nombreApellidosID" class="form-label">Nombre y apellidos</label>
                    <input type="text" name="nombreApellidosID" value="<?php echo $nombreApellidos; ?>" class="form-control" id="nombreApellidosID">
                    <span class="text-danger"> <?php echo $nombreApellidosErr ?> </span>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="dniID" class="form-label">DNI</label>
                    <input type="text" name="dni" value="<?php echo $dni; ?>" class="form-control" id="dniID">
                    <span class="text-danger"> <?php echo $dniErr ?> </span>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="passwordID" class="form-label">Password</label>
                    <input type="password" name="password" value="<?php echo $password; ?>" class="form-control" id="passwordID">
                    <span class="text-danger"> <?php echo $passwordErr ?> </span>
                </div>
            </div>
            <br>
            <button type="submit" class="btn btn-success">Crear</button>
        </form>
    </div>
    <?php include("templates/footer.php") ?>