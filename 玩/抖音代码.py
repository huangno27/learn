import pytesseract
from PIL import Image

image = Image.open(r'C:\Users\13436\PycharmProjects\learnpy\venv\源码.jpg')
code = pytesseract.image_to_string(image)
print(code.rstrip())