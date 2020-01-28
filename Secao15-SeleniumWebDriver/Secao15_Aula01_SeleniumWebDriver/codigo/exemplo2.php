<html>
    <head>
        <title>Olá Aluno!!!</title>
        <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
        <script>
            function sleep(time){
                return new Promise((resolve) => setTimeout(resolve, time));
            }

            sleep(5000).then(() => {
                $("form").append("<tr><td><input type='submit' name='enviar' id='enviar' value='Enviar dados'></td></tr>");
            });
        </script>

    </head>
    <body>
    <h1>Curso Python Web Scraping</h1>
		<form action="destino.php" method="POST">
			Informe os dados abaixo:<br><br>
			<table>
				<tr>
					<td>Nome:</td>
					<td><input type="text" name="nome" id="nome" size="50" maxlength="100"></input></td>
				</tr>
				<tr>
					<td>E-mail:</td>
					<td><input type="text" name="email" id="email" size="50" maxlength="100"></input></td>
				</tr>
				<tr>
					<td>Celular:</td>
					<td><input type="text" name="celular" id="celular" size="20" maxlength="14"></input></td>
				</tr>
			</table>
		</form>
    </body>
</html>