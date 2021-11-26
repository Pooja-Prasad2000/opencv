import cv2
import csv
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image
from pyzbar.pyzbar import decode
dep = []
A = []
barcodes = ['DepartA1.png','DepartA2.png']

with open('Department 1.txt', 'a') as file:
	file.write('DEPARTMENT A')
	file.write('\n')

for j in range(len(barcodes)):
	img = cv2.imread(barcodes[j])
	result =  decode(img)
	for i in result:
		bar = i.data.decode("utf-8")
		dep.append(bar)

		

#print(dep)

for i in range(len(dep)):
	if(dep[i] == '5901231512339' or dep[i]=='5904575622450'):
			A.append(i)


print(A)

for i in range(len(A)):
	file.write('%s\n'%i)



