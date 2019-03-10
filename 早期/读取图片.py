import pytesseract
from PIL import Image

image = Image.open(r'C:\Users\13436\PycharmProjects\learnpy\venv1\py.jpg')
code = pytesseract.image_to_string(image)
print(code.rstrip())


import pytesseract
from PIL import Image

image = Image.open(r'C:\Users\13436\PycharmProjects\learnpy\venv\qq聊天截图.png')
code = pytesseract.image_to_string(image)
print(code.rstrip())

import skimage.io as io                              #3.7没找到解决办法
from skimage import data_dir
str = data_dir + (r'C:\Users\13436\PycharmProjects\learnpy\venv\qq聊天截图.png')
coll = io.ImageCollection(str)
print(coll)


message = "I Really like dogs".replace('dog','cat')
#message.replace('dogs','cats')
print(message)