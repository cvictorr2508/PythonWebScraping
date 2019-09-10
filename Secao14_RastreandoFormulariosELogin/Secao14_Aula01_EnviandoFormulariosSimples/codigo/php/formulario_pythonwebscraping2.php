<!--
	Página que recebe os dados via GET
-->
<html>
	<head>
		<title>Olá Aluno!!!</title>
	</head>
	<body>
		<?php
			$nome = $_GET['nome'];
			$email = $_GET['email'];
			$celular = $_GET['celular'];

			if (empty($nome) or empty($email) or empty($celular))
			{echo "Favor informar todos os campos.";}
			else{echo "Olá " . $nome. ".<br>Seu e-mail é: " . $email . ".<br>Seu celular é: " . $celular;}
		?>
	</body>
</html>