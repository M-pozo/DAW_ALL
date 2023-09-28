<?php include("datos.php"); ?>
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
            <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"></use></svg>
            <span class="fs-4">Portfolio</span>
        </a>

        <ul class="nav nav-pills">
            <li class="nav-item">
                <!-- UD3.2.a BEGIN-->
                <a href="./index.php" 
                    class="nav-link
                        <?php echo ($_SERVER['SCRIPT_NAME']=="/index.php") ? "active" : "" ?>
                    "
                    aria-current="page">INICIO    
                </a>
                <!-- UD3.2.a END-->
            </li>
            <li class="nav-item">
                    <!-- UD3.2.b BEGIN-->
                    <a class="nav-link dropdown-toggle"id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true">
                        CATEGORÍAS
                        <span class="caret"></span>
                    </a>
                    <!-- UD3.2.b END-->     
            </li>
            <li class="nav-item">
                <a href="./contacto.php" 
                    class="nav-link
                        <?php echo ($_SERVER['SCRIPT_NAME']=="/contacto.php") ? "active" : "" ?>
                    "
                    >CONTACTO
                </a>
            </li>
            <!-- UD3.2.e BEGIN -->
                <li class="nav-item">
                    <a href="#" class="nav-link"><?php if($loggedln = true) echo "ADMINISTRACION" ;?></a>
                </li>
            <!-- UD3.2.e END -->
        </ul>
    </header>