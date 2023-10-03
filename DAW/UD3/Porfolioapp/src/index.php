<?php include("templates/header.php"); ?>
<?php include("datos.php"); ?>
<?php include("utiles.php"); ?>


<?php
//UD3.2.f
$sort = $_GET['sort'];
if (isset($_GET['sort']) && $_GET['sort'] == "-1") {
    usort($proyectos, 'ordenaTituloProyectoDesc');
} else {
    usort($proyectos, 'ordenaTituloProyectoAsc');
};
//UD3.3.h
if (isset($_GET['delete']) === true) {
    array_pop($categorias);
};
?>
<div class="container mb-5">
    <!--UD3.2.f BEGIN-->
    <a href="?sort=-1"><button href="" type="button" class="btn btn-outline-secondary">Descendente</button></a>
    <a href="?sort=1"><button href="" type="button" class="btn btn-outline-secondary">Ascendente</button></a>
    <!--UD3.2.f END-->
    <div class="row mt-3">
        <?php foreach ($proyectos as $proyecto) : ?>
            <?php
            ?>
            <div class="col-sm-3">
                <!-- UD3.3.d-->
                <!-- Poner // al principio para que se sobrescriba la url-->
                <a href="//localhost:8080/proyecto.php?id=<?php echo $proyecto["clave"] ?>" class="m-5">
                    <div clss="card">
                        <!-- UD3.2.c -->
                        <img class="card-img-top" style="height: 10rem;" src="<?php echo $proyecto['imagen'] == '' ? 'static/images/default.png' : $proyecto['imagen'] ?>" alt="<?php echo $proyecto['titulo'] ?>">
                        <div class="card-body">
                            <h5 class="card-title"><?php echo $proyecto['titulo'] ?></h5>
                            <p class="card-text"><?php /* UD3.3.d*/ echo nl2br($proyecto['descripcion']); ?></p>
                            <p class="card-text"><?php /* UD3.3.d*/ echo nl2br($proyecto['fecha']); ?></p>
                            <!-- UD3.3.c BEGIN-->
                            <p class="card-text">
                                <?php foreach ($proyecto['categorias'] as $categoria) : ?>
                                    <button class="btn btn-outline-secondary">
                                        <?php echo array_key_exists($categoria, $categorias) ? $categorias[$categoria] : ""; ?>
                                    </button>
                                <?php endforeach; ?>
                                <!-- UD3.3.c END-->
                            </p>
                        </div>
                    </div>
                </a>
            </div>
        <?php endforeach; ?>
    </div>
</div>
<?php include("templates/footer.php"); ?>