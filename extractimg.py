import fitz
import io
from PIL import Image
file_path = "randomfile.pdf"
open_file = fitz.open(file_path)

for page_number in range(len(open_file)):
    page = pdf_file[page_number]
    list_image = page.getImageList()

    if list_image:
        print(f"{len(list_image)} images found on page {page_number}")
    else:
        print("No images found on page", page_number)
      for image_number, img in enumerate(page.getImageList(), start=1):

            xref = img[0]

            image_base = pdf_file.extractImage(xref)
            bytes_image = image_base["image"]

            ext_image = base_image["ext"]
