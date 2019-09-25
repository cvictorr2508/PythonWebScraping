<?php
    if (isset($_COOKIE['cookie_pythonwebscraping_exemplo'])) {
        $login = $_COOKIE['cookie_pythonwebscraping_exemplo'];
        setcookie("cookie_pythonwebscraping_exemplo","",time()-1);
        echo "Você está logado " . $login . "!";
    }else{
        echo "Você não está logado!";
    }
?>