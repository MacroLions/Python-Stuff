import tkinter as kindred
valor=0
ventana1=kindred.Tk()

def agregar():
    global valor
    valor=valor+1
    contador.config(text=valor)
    
    

botontest=kindred.Button(text="Soy una prueba c:", command=agregar)
botontest.pack()

contador=kindred.Label(text=valor)
contador.pack()



#Este es el final (?)
ventana1.mainloop()

