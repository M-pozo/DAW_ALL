<?php include("datos.php"); ?>
<?php $id = $_GET['id'] ?>
<?php include("templates/header.php");
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
        print_r(array_values(array_filter($proyectos, 'buscarProyecto'))[0]['clave']);
        
        $proyecto_json = json_encode($proyectos);
        file_put_contents('mysql/proyectos.json', $proyecto_json);
?>
        <script type="text/javascript">
            window.location = "http://localhost:8080/confirmar_proyecto.php";
        </script>
<?php
    }
}

//UD4.2.b
?>
<?php if ($_COOKIE['loggedIn'] === "true") { ?>
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
                    <textarea class="form-control" name="mensaje" id="areaTexto" rows="3" placeholder="Escriba su mensaje..."><?php print $mensaje; ?></textarea>
                </div>
                <div class="row mb-4">
                    <label for="imagenID" class="form-label">Imagen</label>
                    <input class="form-control" type="file" id="imagenID" name="imagen">
                </div>
                <span class="text-danger"> <?php echo $archivoErr ?> </span>
                <br>
                <button type="submit" class="btn btn-success">Actualizar</button>
            </form>
        </div>
    <?php } else { ?>
        <?php foreach ($proyectos as $proyecto) : if ($id == $proyecto['clave']) { ?>
                <div class="container">
                    <h2><?php echo $proyecto['titulo'] ?></h2>
                    <!--UD3.5.b-->
                    <h4><a href="#"><?php echo date('yy-m-d', strtotime($proyecto['fecha'])); ?></a></h4>
                    <span>Categorías: </span>
                    <a href="#">
                        <!-- UD3.3.c BEGIN-->
                        <?php foreach ($proyecto['categorias'] as $categoria) : ?>
                            <button class="btn btn-outline-secondary">
                                <?php echo array_key_exists($categoria, $categorias) ? $categorias[$categoria] : ""; ?>
                            </button>
                        <?php endforeach; ?>
                        <!-- UD3.3.c END-->
                    </a>
                    <br> <br>
                    <div class="row">
                        <div class="col-sm">
                            <!-- UD3.2.c -->
                            <img style="height: 10rem;" src="<?php echo $proyecto['imagen'] == '' ? 'static/images/default.png' : $proyecto['imagen'] ?>" alt="Proyecto 1" class="img-responsive">
                            <br>
                        </div>
                        <div class="col-sm">
                            <?php echo nl2br($proyecto['descripcion']); ?>
                        </div>
                    </div>
                </div>
        <?php };
        endforeach; ?>
    <?php } ?>
    <!--ud3.3.d END-->
    <?php include("templates/footer.php"); ?>