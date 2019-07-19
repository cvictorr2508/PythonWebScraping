from odf.opendocument import load

# Abrindo um documento
doc = load("Newswest_2018b_Submission_Deadlines_and_Publishing_Dates.odt")
# Salvando um documento
doc.save("Copia.odt")