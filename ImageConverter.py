from enum import auto
from tkinter import ttk
import funciones
import tkinter

#Ventana
ventana = tkinter.Tk()

#Open image
canvas1 = tkinter.Canvas(ventana, bg="#333")
canvas1.pack()

#Archivo origen
texto_archivo_origen = ttk.Entry(canvas1)
texto_archivo_origen.grid(row = 0, column = 0, sticky="ew")
def buscar_archivo_origen():
    archivo_origen = funciones.BuscarArchivo()
    print(archivo_origen)
    texto_archivo_origen.delete(0, 'end')
    texto_archivo_origen.insert(0, archivo_origen.name)
    print(archivo_origen.name)
boton_archivo_origen_buscar = ttk.Button(canvas1, text="buscar", command= buscar_archivo_origen)
boton_archivo_origen_buscar.grid(row=0, column=1, sticky="e")

canvas1.columnconfigure(1, weight=1)
canvas1.rowconfigure(1, weight=1)

#Config Image
canvas2 = tkinter.Canvas(ventana, bg="#444")
canvas2.pack()

ventana.mainloop()



