<?php
include("datos.php");
include("utiles.php");
//UD4.2.c BEGIN
$claveErr = $tituloErr = $fechaErr = $descripcionErr = $imagenErr = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["clave"])) {
        $claveErr = "Por favor, introduzca una clave";
    } else {
        $clave = test_input($_POST["clave"]);
        if (preg_match("/[ ]/", $clave)) {
            $claveErr = "Por favor no introduzcas espacios";
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
        if (preg_match("/^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{4}$/", $fecha)) {
            $fechaErr = "Introduzca un formato válido";
        }
    }
    if (empty($_POST["descripcion"])) {
        $descripcionErr = "Por favor, introduzca su descripción.";
    } else {
        $descripcion = test_input($_POST["descripcion"]);
    }
    if (!empty($_FILES['imagen'])) {
        $nombreImagen = $_FILES['imagen']['name'];
        if (!preg_match("/\.(jpg|jpeg|png|gif|bmp|webp)$/", $nombreImagen)) {
            $imagenErr = "Introduzca un formato válido";
        }
        move_uploaded_file($_FILES['imagen']['tmp_name'], "/var/www/html/static/images/{$nombreImagen}");
        if ($nombreImagen) {
            $pathImagen = "static/images/{$nombreImagen}";
        }
    } else {
        $pathImagen = "";
    }
    //UD4.2.c END
    //UD4.2.e BEGIN
    if ($claveErr === "" && $tituloErr === "" && $fechaErr === "" && $descripcionErr === "" && $imagenErr === "") {
        $proyecto = [
            "clave" => $clave,
            "titulo" => $titulo,
            "descripcion" => $descripcion,
            "imagen" => $pathImagen,
            "fecha" => $fecha,
            "categorias" => ['css'],
        ];
        if ($proyectos === NULL) {
            $proyectos = [];
        }
        array_push($proyectos, $proyecto);
        $proyectos_json = json_encode($proyectos);
        file_put_contents('mysql/proyectos.json', $proyectos_json);
        //UD4.2.e END
?>
        <!--UD4.2.f BEGIN-->
        <script type="text/javascript">
            window.location = "/confirmar_proyecto.php";
        </script>
        <!--UD4.2.f END-->
<?php
    }
}
//UD4.2.c END
?>
<?php include("templates/header.php") ?>
<div class="container">
    <h2 class="mb-5">Crear proyecto</h2>
    <div class="row">
        <!--UD4.2.d-->
        <form action="<?php /*UD4.2.d*/ echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST" enctype="multipart/form-data">
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
                <label for="areaTexto" class="form-label">Descripción</label>
                <textarea class="form-control" name="descripcion" id="areaTexto" rows="3" placeholder="Escriba su mensaje..."><?php print $descripcion; ?></textarea>
                <span class="text-danger"> <?php echo $descripcionErr ?> </span>
            </div>
            <div class="row mb-4">
                <label for="imagenID" class="form-label">Imagen</label>
                <input class="form-control" type="file" id="imagenID" name="imagen">
                <span class="text-danger"> <?php echo $imagenErr ?> </span>
            </div>
            <br>
            <button type="submit" class="btn btn-success">Crear</button>
        </form>
    </div>
    <?php include("templates/footer.php") ?>