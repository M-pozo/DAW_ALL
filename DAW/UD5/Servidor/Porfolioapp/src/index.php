<?php include("templates/header.php"); ?>



<?php
//UD3.2.f
//UD3.3.f
$proyecto_filtrado = $proyectos;
$sort = $_GET['sort'];
if (isset($sort) && $sort == "-1") {
    usort($proyecto_filtrado, 'ordenaTituloProyectoDesc');
} else if (isset($sort) && $sort == "1") {
    usort($proyecto_filtrado, 'ordenaTituloProyectoAsc');
};
//UD3.3.h
if (isset($_GET['delete']) == "true") {
    array_pop($proyecto_filtrado);
};
//UD3.3.f
if (isset($_GET['categoria'])) {
    $proyecto_filtrado = array_filter($proyecto_filtrado, 'buscadorCategoria');
};
//UD3.5.c
if (isset($_GET['sort_date']) && $_GET['sort_date'] == "-1") {
    usort($proyecto_filtrado, 'ordenaFechaProyectoDesc');
} else if (isset($_GET['sort_date']) && $_GET['sort_date'] == "1") {
    usort($proyecto_filtrado, 'ordenaFechaProyectoAsc');
};
?>
<div class="container mb-5">
    <!--UD3.2.f BEGIN-->
    <a href="?sort=-1"><button href="" type="button" class="btn btn-outline-secondary">ProyectoDesc</button></a>
    <a href="?sort=1"><button href="" type="button" class="btn btn-outline-secondary">ProyectosAsc</button></a>
    <a href="?sort_date=-1"><button href="" type="button" class="btn btn-outline-secondary">FechaDesc</button></a>
    <a href="?sort_date=1"><button href="" type="button" class="btn btn-outline-secondary">FechAsc</button></a>
    <!--UD3.2.f END-->
    <div class="row mt-3">
        <?php foreach ($proyecto_filtrado as $proyecto) : ?>
            <?php
            ?>
            <div class="col-sm-3">
                <!-- UD3.3.d / UD4.2.b BEGIN-->
                <?php if ($_COOKIE['loggedIn'] == 'true') { ?>
                    <a href="/crear_actualizar_proyecto.php?id=<?php echo $proyecto["clave"] ?>" class="m-5">
                    <?php } else { ?>
                        <a href="/proyecto.php?id=<?php echo $proyecto["clave"] ?>" class="m-5">
                        <?php } ?>
                        <!--UD4.2.b END-->
                        <div class="card">
                            <!-- UD3.2.c -->
                            <img class="card-img-top" style="height: 10rem;" src="<?php echo $proyecto['imagen'] == '' ? 'static/images/default.png' : $proyecto['imagen'] ?>" alt="<?php echo $proyecto['titulo'] ?>">
                            <div class="card-body">
                                <h5 class="card-title"><?php echo $proyecto['titulo'] ?></h5>
                                <p class="card-text"><?php /* UD3.3.d*/ echo date('d-m-Y', strtotime($proyecto['fecha'])); ?></p>
                                <!-- UD3.3.c BEGIN-->
                                <div class="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
                                    <div class="btn-group mr-2" role="group" aria-label="First group">
                                        <?php foreach ($proyecto['categorias'] as $categoria) : ?>
                                            <button class="btn btn-outline-info btn-sm">
                                                <?php echo array_key_exists($categoria, $categorias) ? $categorias[$categoria] : ""; ?>
                                            </button>
                                        <?php endforeach; ?>
                                    </div>
                                </div>
                                <!-- UD3.3.c END-->
                            </div>
                        </div>
                        </a>
            </div>
        <?php endforeach; ?>
    </div>
    <!--UD4.2.a BEGIN-->
    <a href="/crear_actualizar_proyecto.php"><button href="" type="button" class="btn btn-outline-secondary">Crear Proyecto</button></a>
    <!--UD4.2.a END-->
</div>
<?php include("templates/footer.php"); ?>