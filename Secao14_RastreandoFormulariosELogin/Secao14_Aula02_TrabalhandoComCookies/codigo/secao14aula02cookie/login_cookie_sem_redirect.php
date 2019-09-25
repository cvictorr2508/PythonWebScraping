<?php
    $login = $_POST['login'];
    $senha = $_POST['senha'];
    if ($login == "evaldo" and $senha == "1234"){
        setcookie("cookie_pythonwebscraping_exemplo", $login);
    }else{
        echo "Login ou senha inválidos!!!";
    }
?>