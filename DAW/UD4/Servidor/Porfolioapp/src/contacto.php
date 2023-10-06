<?php include("templates/header.php"); ?>

<?php
$nameErr = $emailErr = $telefonoErr = $tipoErr = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["nombreApellidos"])) {
        $nameErr = "Por favor, introduzca nombre y apellidos";
    } else {
        $name = test_input($_POST["nombreApellidos"]);
        if (!preg_match("/^[a-zA-Z-' ]*$/", $name)) {
            $nameErr = "Solo se permiten letras y espacios.";
        }
    }
}
if (empty($_POST["email"])) {
    $emailErr = "Por favor, introduzca su e-mail.";
} else {
    $email = test_input($_POST["email"]);
    if (!preg_match("/^(([^<>()\[\]\.,;:\s@\”]+(\.[^<>()\[\]\.,;:\s@\”]+)*)|(\”.+\”))@(([^<>()[\]\.,;:\s@\”]+\.)+[^<>()
    [\]\.,;:\s@\”]{2,})$/", $email)) {
        $emailErr = "Introduzca un e-mail válido.";
    }
}
if (empty($_POST["telefono"])) {
    $telefonoErr = "Por favor, introduzca su teléfono.";
} else {
    $telefono = test_input($_POST["telefono"]);
    if (!preg_match("/^[9|6]{1}([\d]{2}[-]*){3}[\d]{2}$/", $telefono)) {
        $telefonoErr = "Introduzca un teĺéfono válido.";
    }
}
if (empty($_POST["tipo"])) {
    $tipoErr = "Por favor, introduzca el tipo de consulta.";
} else {
    $tipo = $_POST["tipo"];
}
if (!empty($_POST["mensaje"])) {
    $mensaje = test_input($_POST["mensaje"]);
}
if (!empty($_FILES['archivo'])) {
    $nombreArchivo = $_FILES['archivo']['name'];
    move_uploaded_file($_FILES['archivo']['tmp_name'], "/var/www/html/uploads/{$nombreArchivo}");
    if ($nombreArchivo) {
        $pathArchivo = "uploads/{$nombreArchivo}";
    }
}
if ($nameErr === "" && $emailErr === "" && $telefonoErr === "" && $tipoErr === "") {
    $contacto = [
        "name" => $name,
        "email" => $email,
        "telefono" => $telefono,
        "tipo" => $tipo,
        "mensaje" => $mensaje,
        "file" => $pathArchivo,
    ];
    $tempArray = json_decode(file_get_contents('mysql/contactos.json'));
    if ($tempArray === NULL) {
        $tempArray = [];
    }
    $contacto['id'] = count($tempArray) + 1;
    array_push($tempArray, $contacto);
    $contactos_json = json_encode($tempArray);
    file_put_contents('mysql/contactos.json', $contactos_json);
?>
    <script type="text/javascript">
        window.location = "http://localhost:8080/confirma_contacto.php";
    </script>
<?php
}
?>
<div class="container">
    <h2 class="mb-5">Contacto</h2>
    <div class="row">
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST" enctype="multipart/form-data">
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="nombreApellidosID" class="form-label">Nombre y apellidos</label>
                    <input type="text" name="nombreApellidos" value="<?php echo $name; ?>" class="form-control" id="nombreApellidosID" placeholder="Su nombre y apellidos">
                    <span class="text-danger"> <?php echo $nameErr ?> </span>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="emailID" class="form-label">e-mail</label>
                    <input type="text" name="email" value="<?php echo $email; ?>" class="form-control" id="emailID" placeholder="Su e-mail">
                    <span class="text-danger"> <?php echo $emailErr ?> </span>
                </div>
                <div class="mb-3 pl-2 col-sm-6 p-0">
                    <label for="telefonoID" class="form-label">Teléfono</label>
                    <input type="text" name="telefono" value="<?php echo $telefono; ?>" class="form-control" id="telefonoID" placeholder="Su telefono">
                    <span class="text-danger"> <?php echo $telefonoErr ?> </span>
                </div>
            </div>
            <div class="row mb-4">
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="tipo" id="particularID" value="particular" <?php
                                                                                                                    if (isset($tipo) && $tipo == "particular") echo "checked"; ?>>
                    <label class="form-check-label" for="particularID">
                        Particular
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="tipo" id="empresaID" value="empresa" <?php
                                                                                                            if (isset($tipo) && $tipo == "empresa") echo "checked"; ?>>
                    <label class="form-check-label" for="empresaID">
                        Empresa
                    </label>
                </div>
                <span class="text-danger"> <?php echo $tipoErr ?> </span>
            </div>
            <div class="row mb-4">
                <textarea class="form-control" name="mensaje" id="areaTexto" rows="3" placeholder="Escriba su mensaje..."><?php print $mensaje; ?></textarea>
                <label for="areaTexto" class="form-label">Mensaje</label>
            </div>
            <!--<div class="row mb-4">
                <label for="archivoID" class="form-label">Adjuntar archivo</label>
                <input class="form-control" type="file" id="archivoID" name="archivo">
            </div>-->
            <span class="text-danger"> <?php echo $archivoErr ?> </span>
            <br>
            <button type="submit" class="btn btn-success">Enviar</button>
        </form>
    </div>
</div>

<?php include("templates/footer.php"); ?>