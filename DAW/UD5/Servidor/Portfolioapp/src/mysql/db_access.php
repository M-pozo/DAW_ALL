<?php
//UD5.2.1 BEGIN
function open_connection($servername, $db,$username, $password){
    try {
        $conn = new PDO("mysql:host=$servername;dbname=$db", $username, $password);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $conn;
    } catch (PDOException $e) {
        echo "La conexión ha fallado: " . $e->getMessage();
        return $e;
    }
}
function close_connection($conn){
    $conn = null;
}
//UD5.2.1 END
?>