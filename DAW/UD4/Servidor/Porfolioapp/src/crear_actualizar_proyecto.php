<?php include("datos.php");
include("utiles.php");
$id = $_GET["id"];
$claveErr = $tituloErr = $fechaErr = $descripcionErr = $imagenErr = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    //UD4.2.c BEGIN
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
        if (!empty($nombreImagen)) {
            if (!preg_match("/\.(jpg|jpeg|png|gif|bmp|webp)$/", $nombreImagen)) {
                $imagenErr = "Introduzca un formato válido";
            } else {
                move_uploaded_file($_FILES['imagen']['tmp_name'], "/var/www/html/static/images/{$nombreImagen}");
                if ($nombreImagen) {
                    $pathImagen = "static/images/{$nombreImagen}";
                }
            }
        }else if (!isset($id)){
            $pathImagen = "";
        }
    }
    //UD4.2.c END
    if ($claveErr === "" && $tituloErr === "" && $fechaErr === "" && $descripcionErr === "" && $imagenErr === "") {
        if(!isset($id)){
            $proyecto = [
                "clave" => $clave,
                "titulo" => $titulo,
                "descripcion" => $descripcion,
                "imagen" => $pathImagen,
                "fecha" => $fecha,
                "categorias" => [],
            ];
            if ($proyectos === NULL) {
                $proyectos = [];
            }
            array_push($proyectos, $proyecto);
            $proyectos_json = json_encode($proyectos);
            file_put_contents('mysql/proyectos.json', $proyectos_json);
        } else {
            $proyecto = array_values(array_filter($proyectos, 'buscarProyecto'))[0];

            $proyecto['clave'] = $clave;
            $proyecto['titulo'] = $titulo;
            $proyecto['fecha'] = $fecha;
            $proyecto['descripcion'] = $descripcion;
            if (!empty($nombreImagen)) {
                $proyecto['imagen'] = $pathImagen;
            }

            $proyectos[array_keys(array_filter($proyectos, 'buscarProyecto'))[0]] = $proyecto;
            $proyecto_json = json_encode($proyectos);
            file_put_contents('mysql/proyectos.json', $proyecto_json);
            }
        //UD4.2.e END
        //UD4.2.f BEGIN
        ?><script type="text/javascript">
            window.location = "/confirmar_proyecto.php";
        </script><?php
        //UD4.2.f END
    }
}
include("templates/header.php");
//UD4.2.e BEGIN
if (!isset($id)) { ?>
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
<?php } else { ?>
    <?php foreach ($proyectos as $proyecto) : if ($id == $proyecto['clave']) { ?>
            <div class="container">
                <h2 class="mb-5">Actualizar proyecto</h2>
                <div class="row">
                    <form action="
                        <?php echo /*UD4.2.d*/ htmlspecialchars($_SERVER["PHP_SELF"]). "?id=". $proyecto['clave'];?>
                        " method="POST" enctype="multipart/form-data">
                        <div class="row">
                            <div class="mb-3 col-sm-6 p-0">
                                <label for="claveID" class="form-label">Clave</label>
                                <input type="text" name="clave" value="<?php echo $proyecto['clave']; ?>" class="form-control" id="claveID" placeholder="Sin espacios">
                                <span class="text-danger"> <?php echo $claveErr ?> </span>
                            </div>
                        </div>
                        <div class="row">
                            <div class="mb-3 col-sm-6 p-0">
                                <label for="tituloID" class="form-label">Titulo</label>
                                <input type="text" name="titulo" value="<?php echo $proyecto['titulo']; ?>" class="form-control" id="tituloID">
                                <span class="text-danger"> <?php echo $tituloErr ?> </span>
                            </div>
                        </div>
                        <div class="row">
                            <div class="mb-3 col-sm-6 p-0">
                                <label for="fechaID" class="form-label">Fecha</label>
                                <input type="date" name="fecha" value="<?php echo $proyecto['fecha']; ?>" class="form-control" id="fechaID">
                                <span class="text-danger"> <?php echo $fechaErr ?> </span>
                            </div>
                        </div>
                        <div class="row mb-4">
                            <label for="descripcionID" class="form-label">Descripción</label>
                            <textarea class="form-control" name="descripcion" id="descripcionID" rows="3" placeholder="Escriba su descripción"><?php echo $proyecto['descripcion']; ?></textarea>
                        </div>
                        <div class="row mb-4">
                            <label for="imagenID" class="form-label">Imagen (<?php /*UD4.2.c*/ echo " ".pathinfo($proyecto['imagen'], PATHINFO_BASENAME)." "; ?>)</label>
                            <input class="form-control" type="file" id="imagenID" name="imagen">
                            <span class="text-danger"> <?php echo $imagenErr ?> </span>
                        </div>
                        <span class="text-danger"> <?php echo $archivoErr ?> </span>
                        <br>
                        <button type="submit" class="btn btn-success">Actualizar</button>
                    </form>
                </div>
        <?php }; endforeach;
} //UD4.2.e END?>