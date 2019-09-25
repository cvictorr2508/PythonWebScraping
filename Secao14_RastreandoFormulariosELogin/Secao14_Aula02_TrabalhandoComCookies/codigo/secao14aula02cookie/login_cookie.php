<?php
    $login = $_POST['login'];
    $senha = $_POST['senha'];
    if ($login == "evaldo" and $senha == "1234"){
        setcookie("cookie_pythonwebscraping_exemplo", $login);
        header('Location: principal_cookie.php');
        exit();
    }else{
        echo "Login ou senha inválidos!!!";
    }
?>