
import cv2
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image
from pyzbar.pyzbar import decode

with open('DepartC2.png', 'wb') as f:
    EAN13('7251120300271', writer=ImageWriter()).write(f)

img = cv2.imread('barcode.png')
result =  decode(img)


for i in result:
    print(i.data.decode("utf-8"))

print("hello world")


