<?php include("templates/header.php"); ?>
<?php include("mysql/db_credenciales.php");
include("mysql/proyecto_sql.php");
include("mysql/categoria_sql.php");

try {
    $conn = new PDO("mysql:host=$servername;dbname=$db", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo "La conexión ha fallado: " . $e->getMessage();
}


?>

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
        <?php foreach (get_proyectos_all($conn) as $proyecto) : ?>
            <?php
            ?>
            <div class="col-sm-3">
                <!-- UD3.3.d / UD4.2.b BEGIN-->
                <?php if ($_COOKIE['loggedIn'] == 'true') { ?>
                    <a href="/crear_actualizar_proyecto.php?id=<?php echo $proyecto["clave"] ?>" class="m-5">
                    <?php } else { ?>
                        <a href="/proyecto.php?id=<?php echo $proyecto["id"] ?>" class="m-5">
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
                            <a href="#" class="badge bg-secondary"><?php echo utf8_encode($categoria['nombre'])
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
<?php include("templates/footer.php"); ?>
<?php $conn = null; ?>