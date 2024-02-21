from PyPDF2 import PdfFileReader, PdfFileWriter

#open
with open("arquivo_grande.pdf", "rb") as input_pdf:
    # Criando um objeto PdfFileReader
    pdf_reader = PdfFileReader(input_pdf)


    num_pages = pdf_reader.numPages

    #divite
    for page_number in range(num_pages):
        # Criando um objeto PdfFileWriter
        pdf_writer = PdfFileWriter()

        # copy the page to the file
        page = pdf_reader.getPage(page_number)
        pdf_writer.addPage(page)

        # Saving
        with open(f"pagina_{page_number + 1}.pdf", "wb") as output_pdf:
            pdf_writer.write(output_pdf)
