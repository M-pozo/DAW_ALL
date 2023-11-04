<?php include("templates/header.php");
include("mysql/contacto_sql.php");
$contactosLista = get_contactos_all($conn);
?>
<div class="container mb-5">
    <h1>Lista de contactos</h1>
    <?php if (empty($contactosLista)) { ?>
        <div class="alert alert-info mt-5">
            Aún no ha sido contactado
        </div>
    <?php } else { ?>
        <div class="list-group">
            <?php foreach ($contactosLista as $contacto) : ?>
                <a href="contacto_detalle.php?id=<?php echo $contacto['id'] ?>" class="list-group-item list-group-item-action"><?php echo $contacto['e-mail'] ?> -
                    <?php echo $contacto['telefono'] ?></a>
            <?php endforeach; ?>
        </div>
    <?php } ?>
</div>
<?php include("templates/footer.php"); ?>