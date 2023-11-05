<?php
$proyecto_id = $_GET['id'];
include("templates/header.php");
include("mysql/proyecto_sql.php");

$proyecto = get_proyecto_detail($conn, $proyecto_id);
?>
<div class="container">
    <h2><?php echo utf8_encode($proyecto['titulo']) ?></h2>
    <span>Categorías: </span>
    <?php foreach (get_categorias_por_proyecto($conn, $proyecto['id']) as $categoria) : ?>
        <a href="/index.php?categoria=<?php echo $categoria['id'] ?>" class="badge bg-secondary">
            <?php echo utf8_encode($categoria['nombre'])?>
        </a>
    <?php endforeach; ?>
    <br> <br>
    <div class="row">
        <div class="col-sm">
            <img src="<?php echo $proyecto['imagen'] ?>" alt="
                <?php echo utf8_encode($proyecto['titulo']) ?>" class="img-fluid rounded">
            <br>
        </div>
        <div class="col-sm">
            <?php echo utf8_encode($proyecto['descripcion']) ?>
        </div>
    </div>
</div>
<?php include("templates/footer.php"); ?>
<?php $conn = null; ?>