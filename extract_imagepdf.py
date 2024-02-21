from pikepdf import Pdf, PdfImage

arquivo = Pdf.open("ResultadoVale.pdf")

for pagina in arquivo.pages:
    for nome, imagem in pagina.images.items():
        imagem_salvar = PdfImage(imagem)
        imagem_salvar.extract_to(fileprefix=f"imagens/{nome}")

how can we fill this images?next steps
