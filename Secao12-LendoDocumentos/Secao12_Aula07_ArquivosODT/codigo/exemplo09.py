import ezodf

documento = ezodf.opendoc('Newswest_2018b_Submission_Deadlines_and_Publishing_Dates.odt')

for obj in documento.body:
    if type(obj) is ezodf.text.Paragraph and obj.text is not None:
        print(obj.text)
