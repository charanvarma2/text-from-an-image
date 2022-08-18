import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\LOGISTICSSYSTEM28\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

charan = Image.open('testsec.png')
text = tess.image_to_string(charan)

print(text)