from PyPDF2 import PdfFileReader

# open
with open("meu_arquivo.pdf", "rb") as input_pdf:
    # Ccreate object
    pdf_reader = PdfFileReader(input_pdf)

  
    num_pages = pdf_reader.numPages

    # reading the text in which page
    for page_number in range(num_pages):
        page = pdf_reader.getPage(page_number)
        text = page.extractText()
        print("Texto da página", page_number + 1, ":", text)
