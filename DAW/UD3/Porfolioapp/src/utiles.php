<?php
    function ordenaTituloProyectoDesc($a, $b) {
        return strcmp($b['titulo'], $a['titulo']);
    }
    function ordenaTituloProyectoAsc($a, $b) {
        return strcmp($a['titulo'], $b['titulo']);
    }
    //UD3.5.a
    function anyoActual() {
        echo date('Y');
    }
?>