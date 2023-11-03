<?php
include("templates/header.php");
include("mysql/proyecto_sql.php");
include_once("mysql/categoria_sql.php");

$proyectos = get_proyectos_all($conn);
$sort = $_GET['sort'];
$sort_date = $_GET['sort_date'];
$id_categoria = $_GET['categoria'];

if (isset($sort)) {
    get_proyectos_order_by($conn, $sort);
}
if (isset($sort_date)) {
    get_proyectos_order_by($conn, $sort_date);
}
if (isset($id_categoria)) {
    $proyectos = get_proyectos_por_categoria($conn, $id_categoria);
}
?>
<div class="container mb-5">
    <!--UD3.2.f BEGIN-->
    <a href="?sort=-1"><button href="" type="button" class="btn btn-outline-secondary">ProyectoDesc</button></a>
    <a href="?sort=1"><button href="" type="button" class="btn btn-outline-secondary">ProyectosAsc</button></a>
    <a href="?sort_date=-1"><button href="" type="button" class="btn btn-outline-secondary">FechaDesc</button></a>
    <a href="?sort_date=1"><button href="" type="button" class="btn btn-outline-secondary">FechAsc</button></a>
    <!--UD3.2.f END-->
    <div class="row mt-3">
        <?php foreach ($proyectos as $proyecto) : ?>
            <?php
            ?>
            <div class="col-sm-3">
                <!-- UD3.3.d / UD4.2.b BEGIN-->
                <?php if ($_COOKIE['loggedIn'] == 'true') { ?>
                    <a href="/crear_actualizar_proyecto.php?id=<?php echo $proyecto["id"] ?>" class="m-5">
                    <?php } else { ?>
                        <a href="/proyecto.php?id=<?php echo $proyecto["id"] ?>" class="m-1">
                        <?php } ?>
                        <!--UD4.2.b END-->
                        <div class="">
                            <!-- UD3.2.c -->
                            <img class="card-img-top" style="height: 10rem;" src="<?php echo $proyecto['imagen'] == '' ? 'static/images/default.png' : $proyecto['imagen'] ?>" alt="<?php echo $proyecto['titulo'] ?>">
                            <div class="card-body">
                                <h5 class="card-title"><?php echo $proyecto['titulo'] ?></h5>
                                <p class="card-text"><?php /* UD3.3.d*/ echo date('d-m-Y', strtotime($proyecto['fecha'])); ?></p>
                            </div>
                        </div>
                        </a>
                        <?php foreach (get_categorias_por_proyecto($conn, $proyecto['id']) as $categoria) : ?>
                            <a href="/index.php?categoria=<?php echo $categoria['id'] ?>" class="badge bg-secondary"><?php echo utf8_encode($categoria['nombre'])
                                                                                                                    ?></a>
                        <?php endforeach; ?>
            </div>
        <?php endforeach; ?>
    </div>
    <hr>
    <!--UD4.2.a BEGIN-->
    <a href="/crear_actualizar_proyecto.php"><button href="" type="button" class="btn btn-outline-secondary">Crear Proyecto</button></a>
    <!--UD4.2.a END-->
</div>
<?php include("templates/footer.php");
close_connection($conn) ?>