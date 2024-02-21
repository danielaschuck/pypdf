from PyPDF2 import PdfFileMerger
#we need to create an object 
pdf_merger = PdfFileMerger()

#  add files on the merge 
pdf_merger.append("arquivo1.pdf")
pdf_merger.append("arquivo2.pdf")

#finish save
with open("arquivo_combinado.pdf", "wb") as output_pdf:
    pdf_merger.write(output_pdf)

