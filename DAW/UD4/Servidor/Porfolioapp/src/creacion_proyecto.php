<?php
include("datos.php");
include("utiles.php");
$claveErr = $tituloErr = $fechaErr = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["clave"])) {
        $claveErr = "Por favor, introduzca una clave";
    } else {
        $clave = test_input($_POST["clave"]);
        /*if (!preg_match("/^[a-zA-Z-' ]*$/", $clave)) {
            $claveErr = "Solo se permiten letras y espacios.";
        }*/
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
        move_uploaded_file($_FILES['imagen']['tmp_name'], "/var/www/html/static/imges/{$nombreImagen}");
        if ($nombreImagen) {
            $pathImagen = "uploads/{$nombreImagen}";
        }
    } else {
        $nombreImagen = "";
    }
    if ($claveErr === "" && $tituloErr === "" && $fechaErr === "") {
        $proyectos = [
            "clave" => $clave,
            "titulo" => $titulo,
            "descripcion" => $descripcion,
            "imagen" => $nombnreImagen,
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
                window.location = "http://localhost:8080/confirma_contacto.php";
            </script>
        <?php
    }
}
?>
<?php include("templates/header.php") ?>
<div class="container">
    <h2 class="mb-5">Actualizar proyecto</h2>
    <div class="row">
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST" enctype="multipart/form-data">
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="claveID" class="form-label">Clave</label>
                    <input type="text" name="clave" value="<?php echo $clave; ?>" class="form-control" id="claveID" placeholder="Sin espacios">
                    <span class="text-danger"> <?php echo $claveErr ?> </span>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="tituloID" class="form-label">Titulo</label>
                    <input type="text" name="titulo" value="<?php echo $titulo; ?>" class="form-control" id="tituloID">
                    <span class="text-danger"> <?php echo $tituloErr ?> </span>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="fechaID" class="form-label">Fecha</label>
                    <input type="date" name="fecha" value="<?php echo $fecha; ?>" class="form-control" id="fechaID">
                    <span class="text-danger"> <?php echo $fechaErr ?> </span>
                </div>
            </div>
            <div class="row mb-4">
                <label for="areaTexto" class="form-label">Descripcion</label>
                <textarea class="form-control" name="descripcion" id="areaTexto" rows="3" placeholder="Escriba su mensaje..."><?php print $descripcion; ?></textarea>
            </div>
            <div class="row mb-4">
                <label for="imagenID" class="form-label">Imagen</label>
                <input class="form-control" type="file" id="imagenID" name="imagen">
            </div>
            <span class="text-danger"> <?php echo $imagenErr ?> </span>
            <br>
            <button type="submit" class="btn btn-success">Actualizar</button>
        </form>
    </div>
<?php include("templates/footer.php") ?>