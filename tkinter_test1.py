#https://docs.python.org/3/library/tk.html

import tkinter

#funciones

def Boton_Buscar():
    print("Buscando....")
    
def Saludar(nombre):
    print("Hola " + nombre)

#crear ventana
ventana = tkinter.Tk()

#configurar ventana
ventana.geometry("600x300")

#widgets

#Etiquetas
etiqueta = tkinter.Label(ventana, text = "Hola mundo", bg = "green")
#etiqueta.pack(side= tkinter.BOTTOM, fill = tkinter.X)

etiqueta2 = tkinter.Label(ventana, text = "Columna izquierda", bg = "red")
#etiqueta2.pack(side=tkinter.LEFT, fill = tkinter.Y, expand= True)

etiqueta3 = tkinter.Label(ventana, text = "Todo", bg = "blue")
#etiqueta3.pack(fill = tkinter.BOTH, expand = True)

#botones
boton1 = tkinter.Button(ventana, text="buscar", padx=100, pady = 30, command=Boton_Buscar)
#boton1.pack()

boton2 = tkinter.Button(ventana, text="Saludar", padx=100, pady = 30, command= lambda: Saludar("Pepe"))
#boton2.pack()

boton2 = tkinter.Button(ventana, text="Saludar 2", padx=100, pady = 30, command= lambda: print("Saludos pepe grillo"))
#boton2.pack()

#cajas de texto

#caja 1
def CT1_func():
    CT1_valor = cajaTexto1.get()
    print(CT1_valor)
    etiquetaCT1["text"] = "Salida: " + CT1_valor
cajaTexto1 = tkinter.Entry(ventana, font="Helvetica 30")
#cajaTexto1.pack()
botonCT1 = tkinter.Button(ventana, text = "Click", command=CT1_func)
#botonCT1.pack()
etiquetaCT1 = tkinter.Label(ventana)
#etiquetaCT1.pack()

#grid
etiquetaGrid1 = tkinter.Label(ventana, text="1", bg="blue", width=10, height= 5)
etiquetaGrid2 = tkinter.Label(ventana, text="2", bg="red", width=10, height= 5)
etiquetaGrid3 = tkinter.Label(ventana, text="3", bg="green", width=10, height= 5)
etiquetaGrid4 = tkinter.Label(ventana, text="4", bg="yellow", width=10, height= 5)

etiquetaGrid1.grid(row = 0, column = 0)
etiquetaGrid2.grid(row = 1, column = 1)
etiquetaGrid3.grid(row = 2, column = 1)
etiquetaGrid4.grid(row = 1, column = 2)




#activar loop
ventana.mainloop()

