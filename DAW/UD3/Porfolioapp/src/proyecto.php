<?php include("templates/header.php"); ?>
<?php include("datos.php"); ?>


<!--UD3.3.d BEGIN-->
<!---->
<?php $id = $_GET['id'] ?>
<?php foreach ($proyectos as $proyecto) : if ($id == $proyecto['clave']) { ?>
        <div class="container">
            <h2><?php echo $proyecto['titulo'] ?></h2>
            <!--UD3.5.b-->
            <h4><a href="#"><?php echo date('d/m/Y', /*strtotime(&proyecto['fecha'])*/ $proyecto['fecha']) ?></a></h4>
            <span>Categorías: </span>
            <a href="#">
                <!-- UD3.3.c BEGIN-->
                <?php foreach ($proyecto['categorias'] as $categoria) : ?>
                    <button class="btn btn-outline-secondary">
                        <?php echo array_key_exists($categoria, $categorias) ? $categorias[$categoria] : ""; ?>
                    </button>
                <?php endforeach; ?>
                <!-- UD3.3.c END-->
            </a>
            <br> <br>
            <div class="row">
                <div class="col-sm">
                    <!-- UD3.2.c -->
                    <img style="height: 10rem;" src="<?php echo $proyecto['imagen'] == '' ? 'static/images/default.png' : $proyecto['imagen'] ?>" alt="Proyecto 1" class="img-responsive">
                    <br>
                </div>
                <div class="col-sm">
                    <?php echo nl2br($proyecto['descripcion']); ?>
                </div>
            </div>
        </div>
<?php break;
    };
endforeach; ?>
<!--ud3.3.d END-->
<?php include("templates/footer.php"); ?>