import pytesseract as tess
tess.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract'
from PIL import Image

ks = Image.open('text1.png')
text = tess.image_to_string(ks)

print(text)
