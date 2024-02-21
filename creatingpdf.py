from PyPDF2 import PdfWriter

# Criando um objeto PdfWriter
pdf_writer = PdfWriter()

# Adicionando uma página ao arquivo PDF
pdf_writer.add_page()

# Salvando o arquivo PDF no disco
with open("meu_arquivo.pdf", "wb") as output_pdf:
    pdf_writer.write(output_pdf)
