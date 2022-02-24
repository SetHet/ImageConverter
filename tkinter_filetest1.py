import tkinter
import tkinter.filedialog

ventana = tkinter.Tk()
ventana.geometry("300x300")

def BuscarCarpeta():
    file = tkinter.filedialog.askopenfile(mode = 'r')
    print(file)

btn_find = tkinter.Button(ventana, text="Buscar", command=BuscarCarpeta)
btn_find.pack()

tkinter.mainloop()