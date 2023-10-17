<?php
include("datos.php");
include("utiles.php");
//UD4.2.c BEGIN
$claveErr = $tituloErr = $fechaErr = $descripcionErr = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["clave"])) {
        $claveErr = "Por favor, introduzca una clave";
    } else {
        $clave = test_input($_POST["clave"]);
        if (preg_match("/[ ]/", $clave)) {
            $claveErr = "Por favor no intriduzcas espacios";
        }
    }
    if (empty($_POST["titulo"])) {
        $tituloErr = "Por favor, introduzca un titulo.";
    } else {
        $titulo = test_input($_POST["titulo"]);
    }
    if (empty($_POST["fecha"])) {
        $fechaErr = "Por favor, introduzca su fecha.";
    } else {
        $fecha = test_input($_POST["fecha"]);
    }
    if (empty($_POST["descripcion"])) {
        $descripcionErr = "Por favor, introduzca su descripción.";
    } else {
        $descripcion = test_input($_POST["descripcion"]);
    }
    if (!empty($_FILES['imagen'])) {
        $nombreImagen = $_FILES['imagen']['name'];
        move_uploaded_file($_FILES['imagen']['tmp_name'], "/var/www/html/static/images/{$nombreImagen}");
        if ($nombreImagen) {
            $pathImagen = "static/images/{$nombreImagen}";
        }
    } else {
        $pathImagen = "";
    }
    if ($claveErr === "" && $tituloErr === "" && $fechaErr === "" && $descripcionErr === "") {
        $proyectos = [
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
<?php
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
                    <input type="text" name="clave" value="<?php echo $clave; ?>" class="form-control" id="claveID" placeholder="Sin espacios">
                    <span class="text-danger"> <?php echo $claveErr ?> </span>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="tituloID" class="form-label">Nombre y apellidos</label>
                    <input type="text" name="titulo" value="<?php echo $titulo; ?>" class="form-control" id="tituloID">
                    <span class="text-danger"> <?php echo $tituloErr ?> </span>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="fechaID" class="form-label">DNI</label>
                    <input type="text" name="fecha" value="<?php echo $fecha; ?>" class="form-control" id="fechaID">
                    <span class="text-danger"> <?php echo $fechaErr ?> </span>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="fechaID" class="form-label">Password</label>
                    <input type="password" name="fecha" value="<?php echo $fecha; ?>" class="form-control" id="fechaID">
                    <span class="text-danger"> <?php echo $fechaErr ?> </span>
                </div>
            </div>
            <span class="text-danger"> <?php echo $imagenErr ?> </span>
            <br>
            <button type="submit" class="btn btn-success">Crear</button>
        </form>
    </div>
    <?php include("templates/footer.php") ?>