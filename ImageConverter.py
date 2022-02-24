from cgitb import text
from textwrap import fill
from tkinter import ttk
from numpy import size
import funciones
import tkinter
from PIL import Image, ImageTk

#Variables
archivo_origen = False
img_origen = Image.open("./IconImageConverter.png")
muestra = {
    "photo_size":(150, 150),
    "text_value": "valores"
    }
tipos_img = ["PNG", "ICO", "JPG"]


#Ventana
ventana = tkinter.Tk()
ventana.title("Image Converter")
#ventana.iconphoto("./IconImageConverter.png")
ventana.geometry("500x300")

#Open image
labelframe1 = tkinter.LabelFrame(ventana, bg="#EEE", text="Original")
labelframe1.pack(fill=tkinter.X, expand=True, side=tkinter.TOP)

#Archivo origen
frame1_1 = tkinter.Frame(labelframe1)
frame1_1.pack(side=tkinter.TOP, fill=tkinter.X, expand=True)

texto_archivo_origen = ttk.Entry(frame1_1)
texto_archivo_origen.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)

def buscar_archivo_origen():
    #buscar archivo
    archivo_origen = funciones.BuscarArchivo()
    #actualizar direccion de origen
    texto_archivo_origen.delete(0, 'end')
    texto_archivo_origen.insert(0, archivo_origen.name)
    #actualizar imagen origen
    global imagen_origen
    global muestra
    global img_origen
    #imagen_origen = tkinter.PhotoImage(file=archivo_origen.name)
    img_origen = Image.open(archivo_origen.name)
    img = img_origen.resize(muestra["photo_size"], Image.ANTIALIAS)
    imagen_origen= ImageTk.PhotoImage(img)
    global label_imagen_origen
    label_imagen_origen = ttk.Label(frame1_2_1, image=imagen_origen)
    label_imagen_origen.pack(side=tkinter.LEFT)
    #texto imagen origen
    texto = "size: " + str(img_origen.size[0]) + " x " + str(img_origen.size[1])
    global label_muestra_origen
    label_muestra_origen = tkinter.Label(frame1_2_2,justify=tkinter.LEFT, text=texto, bg="#0A0")
    label_muestra_origen.place(anchor="nw")
    #entry folder out
    texto_folder_salida.delete(0, 'end')
    texto_folder_salida.insert(0, archivo_origen.name[0:archivo_origen.name.rfind("/")])
    
    
boton_archivo_origen_buscar = ttk.Button(frame1_1, text="File Input", command= buscar_archivo_origen)
boton_archivo_origen_buscar.pack(side=tkinter.RIGHT)

frame1_2 = tkinter.Frame(labelframe1)
frame1_2.pack(side=tkinter.BOTTOM, fill=tkinter.X, expand=True)

frame1_2_1 = tkinter.Frame(frame1_2)
frame1_2_1.pack(side=tkinter.LEFT)

img = Image.open("./IconImageConverter.png")
img = img.resize(muestra["photo_size"], Image.ANTIALIAS)
imagen_origen = ImageTk.PhotoImage(img)
label_imagen_origen = ttk.Label(frame1_2_1, image=imagen_origen)
label_imagen_origen.pack(side=tkinter.BOTTOM)

frame1_2_2 = tkinter.Frame(frame1_2)
frame1_2_2.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)

label_muestra_origen = tkinter.Label(frame1_2_2,justify=tkinter.LEFT, text=muestra["text_value"], bg="#0A0")
label_muestra_origen.place(anchor="nw")

########################Config Image
labelframe2 = tkinter.LabelFrame(ventana, bg="#DDD", text="Configuration")
labelframe2.pack(fill=tkinter.X, expand=True)

frame2_1 = tkinter.Frame(labelframe2)
frame2_1.pack(fill=tkinter.X, expand=True)

label_width = ttk.Label(frame2_1, text="width: ")
label_width.pack(side=tkinter.LEFT)

entry_width = ttk.Entry(frame2_1)
entry_width.pack(side=tkinter.LEFT)

label_height = ttk.Label(frame2_1, text="  x  heigth: ")
label_height.pack(side=tkinter.LEFT)

entry_height = ttk.Entry(frame2_1)
entry_height.pack(side=tkinter.LEFT)

frame2_2 = tkinter.Frame(labelframe2)
frame2_2.pack(fill=tkinter.X, expand=True)

label_tipo_img = ttk.Label(frame2_2, text="Type Image: ")
label_tipo_img.pack(side=tkinter.LEFT)

lista_tipo_img = ttk.Combobox(frame2_2, values =tipos_img)
lista_tipo_img.pack(side=tkinter.LEFT)

########################Config Salida
labelframe3 = tkinter.LabelFrame(ventana, bg="#EEE", text="Out File")
labelframe3.pack(side=tkinter.TOP, fill=tkinter.X, expand=True)

texto_folder_salida = ttk.Entry(labelframe3)
texto_folder_salida.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)

boton_folder_out = ttk.Button(labelframe3, text = "Folder Output")
boton_folder_out.pack()

labelframe4 = tkinter.Frame(ventana, bg="#EEE")
labelframe4.pack(side=tkinter.TOP, fill=tkinter.X, expand=True)

boton_guardar = ttk.Button(labelframe4, text = "Save")
boton_guardar.pack()



#Loop
ventana.mainloop()



