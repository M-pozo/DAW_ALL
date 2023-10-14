<?php include_once("datos.php"); ?>
<?php include_once("utiles.php"); ?>
<!--DOCTYPE html -->
<html>

<head>
    <title>Portfolio de proyectos</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <!-- Optional theme -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/flatly/bootstrap.min.css" integrity="sha384-qF/QmIAj5ZaYFAeQcrQ6bfVMAh4zZlrGwTPY7T/M+iTTLJqJBJjwwnsE5Y0mV7QK" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<!-- https://radu.link/make-footer-stay-bottom-page-bootstrap/ -->

<body class="d-flex flex-column min-vh-100">

    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
        <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
            <svg class="bi me-2" width="40" height="32">
                <use xlink:href="#bootstrap"></use>
            </svg>
            <!--UD3.5.a-->
            <span class="fs-4">Portfolio <?php anyoActual() ?></span>
        </a>

        <ul class="nav nav-pills">
            <li class="nav-item">
                <!-- UD3.2.a-->
                <a href="./index.php" class="nav-link
                        <?php echo ($_SERVER['SCRIPT_NAME'] == "/index.php") && !isset($_GET['categoria']) ? "active" : "" ?>
                    " aria-current="page">INICIO
                </a>
            </li>
            <!-- UD3.3.e BEGIN-->
            <li class="nav-item">
                <a class="nav-link dropdown-toggle
                    <?php echo ($_SERVER['SCRIPT_NAME'] == "/index.php") && isset($_GET['categoria']) ? "active" : "" ?>
                " id="dropdownMenu1" data-bs-toggle="dropdown" ariahaspopup="true">
                    CATEGORÍAS
                    <span class="caret"></span>
                </a>
                <div class="dropdown-menu" aria-labelledby="dropdownMenu1">
                    <?php foreach ($categorias as $key => $value) :
                        echo '<a class="dropdown-item" href="//localhost:8080/index.php?categoria=' . $key . '">' . $value . '</a>';
                    endforeach; ?>
                </div>
            </li>
            <li class="nav-item">
                <!--UD3.2.b-->
                <a href="./sobre_mi.php" class="nav-link
                        <?php echo ($_SERVER['SCRIPT_NAME'] == "/sobre_mi.php") ? "active" : "" ?>
                    ">SOBRE MÍ
                </a>
            </li>
            <!-- UD3.3.e END-->
            <?php 
            //UD4.1.e BEGIN
            if ($_COOKIE['loggedIn'] === "true") { ?>
                <!-- UD3.2.e BEGIN -->
                <li class="nav-item">
                    <a href="./contacto_lista.php" class="nav-link 
                    <?php echo ($_SERVER['SCRIPT_NAME'] == "/contacto_lista.php") ? "active" : "" ?> ">
                        <!--UD4.1.c-->
                        <?php if ($_COOKIE['loggedIn'] === "true") echo "ADMINISTRACION"; ?></a>
                </li>
                <!-- UD3.2.e END -->
                <li class="nav-item">
                    <a href="/logout.php" class="nav-link
                            <?php echo ($_SERVER['SCRIPT_NAME'] == "/logout.php" ) ? "active" : "" ?>
                        "><?php if ($_COOKIE['loggedIn'] === "true") echo "LOG OUT"; ?></a>
                    </a>
                </li>
            <?php } else { ?>
                <!--UD4.1.a BEGIN-->
                <li class="nav-item">
                    <a href="/login.php" class="nav-link
                            <?php echo ($_SERVER['SCRIPT_NAME'] == "/login.php" ) ? "active" : "" ?>
                        "><?php if ($_COOKIE['loggedIn'] === "false") echo "LOG IN"; ?></a>
                    </a>
                </li>
                <!--UD4.1.a END-->
            <?php } //UD4.1.e END?>
        </ul>
    </header>