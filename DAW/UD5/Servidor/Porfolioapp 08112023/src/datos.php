<?php
include("mysql/db_credenciales.php");
include("mysql/db_access.php");

$conn = open_connection($servername, $db, $username, $password);
$limit = 2;

if (isset($_GET['pagina'])) {
    if ($_GET['pagina'] <= 0) {
        ?><script type="text/javascript">
            window.location = "/index.php";
        </script><?php
    }
    $offset = $limit * ($_GET['pagina'] - 1);
    $paginacion = 'LIMIT '.$limit.' OFFSET '.$offset;
}else{
    $paginacion = 'LIMIT '.$limit;
}
?>