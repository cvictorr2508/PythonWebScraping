<?php
    session_start();
    if (isset($_SESSION['session_pythonwebscraping_exemplo'])) {
        $login = $_SESSION['session_pythonwebscraping_exemplo'];
        unset($_SESSION['session_pythonwebscraping_exemplo']);
        echo "Você está logado " . $login . "!";
    }else{
        echo "Você não está logado!";
    }
?>