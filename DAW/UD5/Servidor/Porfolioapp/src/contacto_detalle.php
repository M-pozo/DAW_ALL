<?php 
include("templates/header.php"); 
include("mysql/contacto_sql.php");

$contacto_id = $_GET['id'];
$contacto = get_contacto($conn, $contacto_id);
?>
<div class="container">
    <h1 class="mb-5">Detalle del contacto</h1>
    <?php if (!empty($contacto)) { ?>
        <p><?php echo $contacto['nombre y apellidos'] ?></p>
        <p><?php echo $contacto['e-mail'] ?></p>
        <p><?php echo $contacto['telefono'] ?></p>
        <p><?php echo $contacto['particular/empresa'] ?></p>
        <p><?php echo $contacto['mensaje'] ?></p>
        <?php if ($contacto['archivo']) { ?>
            <a href="<?php echo $contacto['archivo'] ?>" class="btn btn-info mb-4"><i class="fa-solid fa-
paperclip"></i> ARCHIVO ADJUNTO</a> <br>
        <?php } ?>
    <?php } else { ?>
        <div class="alert alert-danger mt-5">
            En contacto no existe.
        </div>
    <?php } ?>
    <a href="contacto_lista.php" class="btn btn-secondary"><i class="fa-solid fa-arrow-left mr-2"></i>
        Volver</a>
</div>
<?php include("templates/footer.php"); ?>