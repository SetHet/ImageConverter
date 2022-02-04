# https://www.tutorialexample.com/convert-png-to-ico-with-pillow-for-python-beginners-python-tutorial/
from PIL import Image

print("File path: ")
filename = input()

img = Image.open(filename)

print("Save in: ")
savename = input()
width = int(input("ancho: "))
heigth = int(input("alto: "))

img.save(savename, format = 'ICO', sizes=[(width, heigth)])
