<?php
include("mysql/db_credenciales.php");
include("mysql/db_access.php");

$conn = open_connection($servername, $db, $username, $password);

$limit = 2;
if (isset($_GET['pagina'])) {
    $offset = $limit * ($_GET['pagina'] - 1);
    $paginacion = 'LIMIT '.$limit.' OFFSET '.$offset;
}else{
    $paginacion = 'LIMIT '.$limit;
}
?>