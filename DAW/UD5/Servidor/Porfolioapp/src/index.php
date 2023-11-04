<?php
include("templates/header.php");
include("mysql/proyecto_sql.php");
include_once("mysql/categoria_sql.php");

$proyectos = get_proyectos_all($conn);
$sort = $_GET['sort'];
$sort_date = $_GET['sort_date'];
$id_categoria = $_GET['categoria'];
$pagina = $_GET['pagina'];
$enlace = '?pagina=';

//UD5.4.c BEGIN
if (isset($sort)&& $sort == "-1") {
    $proyectos = get_proyectos_order_by($conn, "titulo DESC");
    $enlace = '?sort=-1?pagina=';
}else if (isset($sort)&& $sort == "1"){
    $proyectos = get_proyectos_order_by($conn, "titulo ASC");
    $enlace = '?sort=1?pagina=';
}
else if (isset($sort_date)&& $sort_date == "-1"){
    $proyectos = get_proyectos_order_by($conn, "fecha DESC");
    $enlace = '?sort_date=-1?pagina=';
}
else if (isset($sort_date)&& $sort_date == "1"){
    $proyectos = get_proyectos_order_by($conn, "fecha ASC");
    $enlace = '?sort_date=1?pagina=';
}
//UD5.4.c END
//UD5.4.b BEGIN
if (isset($pagina)) {
    $proyectos = get_proyectos_paginados($conn);
}
//UD5.4.b END
if (isset($id_categoria)) {
    $proyectos = get_proyectos_por_categoria($conn, $id_categoria);
    $enlace = '?categoria='.$id_categoria.'?pagina=';
}
?>
<div class="container mb-1">
<!--UD3.2.f BEGIN-->
<ul class="nav nav-pills">
    <li class="nav-item">
        <a class="nav-link dropdown-toggle" id="dropdownMenu1" data-bs-toggle="dropdown" ariahaspopup="true">Ordenar<span class="caret"></span></a>
        <div class="dropdown-menu" aria-labelledby="dropdownMenu1">
            <a href="?sort=-1"><button href="" type="button" class="btn btn-outline-secondary">ProyectoDesc</button></a>
            <a href="?sort=1"><button href="" type="button" class="btn btn-outline-secondary">ProyectosAsc</button></a>
            <a href="?sort_date=-1"><button href="" type="button" class="btn btn-outline-secondary">FechaDesc</button></a>
            <a href="?sort_date=1"><button href="" type="button" class="btn btn-outline-secondary">FechAsc</button></a>
        </div>
        <li class="nav-item">
            <!--UD4.2.a BEGIN-->
            <a href="/crear_actualizar_proyecto.php"><button href="" type="button" class="btn btn-outline-secondary">Crear Proyecto</button></a>
            <!--UD4.2.a END-->
        </div>
    </li>
</ul>
</div>
<!--UD3.2.f END-->
<div class="container mb-5">
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
                            <!--UD5.4.b BEGIN-->
                            <a href="/index.php?categoria=<?php echo $categoria['id'] ?>" class="badge bg-secondary">
                                <?php echo utf8_encode($categoria['nombre'])?>
                            </a>
                            <!--UD5.4.b END-->
                        <?php endforeach; ?>
            </div>
        <?php endforeach; ?>
    </div>
    <hr>
    <a href="<?php echo $enlace.($pagina - 1)?>"><button href="" type="button" class="btn btn-outline-secondary">ANTERIOR</button></a>
    <a href="<?php echo $enlace.($pagina + 1)?>"><button href="" type="button" class="btn btn-outline-secondary">SIGUIENTE</button></a>
</div>
<?php include("templates/footer.php");
close_connection($conn) ?>