import tkinter
import tkinter.filedialog


def BuscarArchivo():
    archivo = tkinter.filedialog.askopenfile()
    return archivo


