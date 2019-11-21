<?php
    $login = $_POST['login'];
    $senha = $_POST['senha'];
    if ($login == "evaldo" and $senha == "1234"){
        session_start();
        $_SESSION['session_pythonwebscraping_exemplo'] = $login;
        header('Location: principal_session.php');
        exit();
    }else{
        echo "Login ou senha inválidos!!!";
    }
?>