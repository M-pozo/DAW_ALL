<?php include_once("datos.php");
include_once("utiles.php");
include_once("mysql/categoria_sql.php");
?>
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
            <span class="fs-4">Portfolio <?php anyoActual() ?></span>
        </a>

        <ul class="nav nav-pills">
            <li class="nav-item">
                <a href="./index.php" class="nav-link
                        <?php echo ($_SERVER['SCRIPT_NAME'] == "/index.php") && !isset($_GET['categoria']) ? "active" : "" ?>
                    " aria-current="page">INICIO
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link dropdown-toggle
                    <?php echo ($_SERVER['SCRIPT_NAME'] == "/index.php") && isset($_GET['categoria']) ? "active" : "" ?>
                " id="dropdownMenu1" data-bs-toggle="dropdown" ariahaspopup="true">
                    CATEGORÍAS
                    <span class="caret"></span>
                </a>
                <div class="dropdown-menu" aria-labelledby="dropdownMenu1">
                    <!--UD5.4.a BEGIN-->
                    <?php foreach (get_categorias_all($conn) as $categoria) :
                        //UD5.4.b BEGIN
                        echo '<a class="dropdown-item" href="/index.php?categoria=' . $categoria['id'] . '">' . $categoria['nombre'] . '</a>';
                        //UD5.4.b END
                    endforeach; ?>
                    <!--UD5.4.a END-->
                </div>
            </li>
            <li class="nav-item">
                <a href="./sobre_mi.php" class="nav-link
                        <?php echo ($_SERVER['SCRIPT_NAME'] == "/sobre_mi.php") ? "active" : "" ?>
                    ">SOBRE MÍ
                </a>
            </li>
            <!--UD5.6.a BEGIN-->
            <?php if (get_user_logged_in($conn, $_COOKIE['user_email'])) { ?>
                <li class="nav-item">
                    <a class="nav-link dropdown-toggle 
                    <?php echo ($_SERVER['SCRIPT_NAME'] == "/usuarios.php" || $_SERVER['SCRIPT_NAME'] == "/contacto_lista.php") ? "active" : "" ?>" id="dropdownMenu1" data-bs-toggle="dropdown" ariahaspopup="true">ADMINISTRACION
                        <span class="caret"></span>
                    </a>
                    <div class="dropdown-menu" aria-labelledby="dropdownMenu1">
                        <a class="dropdown-item" href="/contacto_lista.php">Lista de contactos</a>
                        <a class="dropdown-item" href="/usuarios.php">Usuarios</a>
                    </div>
                </li>
                <li class="nav-item">
                    <a href="/logout.php" class="nav-link
                            <?php echo ($_SERVER['SCRIPT_NAME'] == "/logout.php") ? "active" : "" ?>
                        ">LOG OUT</a>
                    </a>
                </li>
            <?php } else { ?>
                <li class="nav-item">
                    <a href="/login.php" class="nav-link
                            <?php echo ($_SERVER['SCRIPT_NAME'] == "/login.php") ? "active" : "" ?>
                        ">LOG IN</a>
                    </a>
                </li>
            <?php } ?>
            <!--UD5.6.a END-->
        </ul>
    </header>