<?php include("templates/header.php"); ?>
<?php include("datos.php"); ?>
<?php include("utiles.php"); ?>

<?php
$sort = $_GET['sort'];
if(isset($_GET['sort']) && $_GET['sort'] == "-1"){
    usort($proyectos, 'ordenaTituloProyectoDesc');
};
?>
<div class="container mb-5">
    <div class="row">
        <?php foreach($proyectos as $proyecto): ?>
            <div class="col-sm-3">
                <a href="#" class="p-5">
                    <div clss="card">
                        <img class="card-img-top" src="<?php echo $proyecto['imagen']?>" alt="<?php echo $proyecto['titulo']?>">
                        <div class="card-body">
                            <h5 class="card-title"><?php echo $proyecto['titulo']?></h5>
                            <p class="card-text"><?php echo $proyecto['descripcion']?></p>
                        </div>
                    </div>
                </a>
            </div>
        <?php endforeach; ?>
    </div>
</div>
<?php include("templates/footer.php"); ?>