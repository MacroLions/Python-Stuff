import tkinter

#Ventana
ventana=tkinter.Tk()
ventana.geometry("600x600")
ventana.resizable(0,0)
ventana.title("Mai Paint ver. 1.0")


ventana1=tkinter.Tk()
ventana1.geometry("100x500")
ventana1.resizable(0,0)


#Canvas
canvas=tkinter.Canvas(ventana,width=600, height=600,bg="white")
canvas.pack(side="right")


#Global
linea_coord=None
linea_coord1=None
linea_coord2=None
linea_coord3=None
linea_coord4=None
linea_coord5=False
borrador=False
x1=0
y1=0
x2=0
y2=0
x3=0
y3=0
x4=0
y4=0
x5=0
y5=0
x6=0
y6=0
color="black"
width=15

#Colores
def cambio():
    global color
    color="red"
def cambio1():
    global color
    color="blue"
def cambio2():
    global color
    color="lightgreen"
def cambio3():
    global color
    color="yellow"

#Width
def grueso():
    global width
    width=width+1
    print(width)
    grosor_numero.config(text=width)
    
def delgado():
    global width
    if width>1:
        width=width-1
        print(width)
        grosor_numero.config(text=width)
    elif width==1:
        width=1
        print(width)
        grosor_numero.config(text=width)
    

#Funciones
        
#Linea
def coord(event):
    global linea_coord
    global linea_coord5
    global x1
    global y1
    global x2
    global y2
    global color
    global width

    if linea_coord5!=True:
        if linea_coord is None:
            x1,y1=(event.x,event.y)
            print(x1,y1)
            linea_coord=True
        
        else:
            x2,y2=(event.x,event.y)
            print(x1,y1,x2,y2)
            canvas.create_line(x1,y1,x2,y2,fill=color,width=width)
            linea_coord=None
        
#Circulo
def coord1(event):
    global linea_coord1
    global linea_coord5
    global x1
    global y1
    global x2
    global y2
    global color
    global width

    if linea_coord5!=True:
        if linea_coord1 is None:
            x1,y1=(event.x,event.y)
            print(x1,y1)
            linea_coord1=True
        
        else:
            x2,y2=(event.x,event.y)
            print(x1,y1,x2,y2)
            canvas.create_oval(x1,y1,x2,y2,outline=color,width=width)
            linea_coord1=None
        
#Poligono de 4 lados
def coord2(event):
    global linea_coord2
    global linea_coord5
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    global x4
    global y4
    global color
    global width

    if linea_coord5!=True:
        if linea_coord2 is None:
            x1,y1=(event.x,event.y)
            print(x1,y1)
            linea_coord2=True
        
        elif linea_coord2 is True:
            x2,y2=(event.x,event.y)
            print(x1,y1,x2,y2)
            linea_coord2=False
        
        elif linea_coord2 is False:
            x3,y3=(event.x,event.y)
            print(x1,y1,x2,y2,x3,y3)
            linea_coord2=1
        
        else:
            x4,y4=(event.x,event.y)
            print(x1,y1,x2,y2,x3,y3,x4,y4)
            canvas.create_line(x1,y1,x2,y2,x3,y3,x4,y4,x1,y1,fill=color,width=width)
            linea_coord2=None

#Triángulo
def coord3(event):
    global linea_coord3
    global linea_coord5
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    global color
    global width

    if linea_coord5!=True:
        if linea_coord3==None:
            x1,y1=(event.x,event.y)
            print(x1,y1)
            linea_coord3=True
        
        elif linea_coord3==True:
            x2,y2=(event.x,event.y)
            print(x1,y1,x2,y2)
            linea_coord3=False
        
        else:
            x3,y3=(event.x,event.y)
            print(x1,y1,x2,y2,x3,y3)
            canvas.create_line(x1,y1,x2,y2,x3,y3,x1,y1,width=width,fill=color)
            linea_coord3=None

#Rectángulo
def coord4(event):
    global linea_coord4
    global linea_coord5
    global x1
    global y1
    global x2
    global y2
    global color
    global width

    if linea_coord5!=True:
        if linea_coord4==None:
            x1,y1=(event.x,event.y)
            print(x1,y1)
            linea_coord4=True
        
        elif linea_coord4==True:
            x2,y2=(event.x,event.y)
            print(x1,y1,x2,y2)
            canvas.create_rectangle(x1,y1,x2,y2,width=width,outline=color)
            linea_coord4=None

#Pincel
def coord5(event):
    global linea_coord5
    global color
    global width
 
    
    if linea_coord5 is True:
        x1,y1=(event.x+1,event.y+1)
        x2,y2=(event.x-1,event.y-1)
        if borrador==True:
            canvas.create_oval(x1,y1,x2,y2,width=width,fill="white",outline="white")
        else:
            canvas.create_oval(x1,y1,x2,y2,width=width,fill=color,outline=color)
        


#Funciones de retorno   
def linea():
    global linea_coord5
    linea_coord5=False
    canvas.bind("<Button-1>",coord)
    
def circulo():
    global linea_coord5
    linea_coord5=False
    canvas.bind("<Button-1>",coord1)
    
def poligono_4():
    global linea_coord5
    linea_coord5=False
    canvas.bind("<Button-1>",coord2)
    
def triangulo():
    global linea_coord5
    linea_coord5=False
    canvas.bind("<Button-1>",coord3)
    
def rectangulo():
    global linea_coord5
    linea_coord5=False
    canvas.bind("<Button-1>",coord4)

def pincel():
    global linea_coord5
    global borrador
    linea_coord5=False
    if linea_coord5 is False:
        canvas.bind("<B1-Motion>",coord5)
        linea_coord5=True
        borrador=False

def borrador():
    global linea_coord5
    global borrador
    linea_coord5=False
    if linea_coord5 is False:
        canvas.bind("<B1-Motion>",coord5)
        borrador=True
        linea_coord5=True
  


    
def borrar_todo():
    canvas.delete("all")
    
def personalizado():
    global color
    obtenible=color_personal.get()
    if obtenible!=None:
        color="black"
    else:
        color=color_personal.get()


#Herramientas
herramientas=tkinter.Label(ventana1,bg="white",text="Herramientas:")
boton_linea=tkinter.Button(ventana1,text="Linea",command=linea)
boton_circulo=tkinter.Button(ventana1,text="Circulo",command=circulo)
boton_poligono=tkinter.Button(ventana1,text="Poligono de\n4 lados",command=poligono_4)
boton_rectangulo=tkinter.Button(ventana1,text="Rectángulo",command=rectangulo)
boton_triangulo=tkinter.Button(ventana1,text="Triángulo",command=triangulo)
boton_pincel=tkinter.Button(ventana1,text="Pincel",command=pincel)
boton_borrador=tkinter.Button(ventana1,text="Borrador",command=borrador)

boton_borrar_todo=tkinter.Button(ventana1,text="¡BORRAR TODO!",command=borrar_todo)

herramientas.pack()
boton_linea.pack()
boton_circulo.pack()
boton_poligono.pack()
boton_rectangulo.pack()
boton_triangulo.pack()
boton_pincel.pack()
boton_borrador.pack()

boton_borrar_todo.pack()
boton_borrar_todo.place(relx=0.5,rely=0.96,anchor="center")


#Colores
colores=tkinter.Label(ventana1,bg="white",text="Colores:")

rojo=tkinter.Button(ventana1,width=5,bg="red",command=cambio)
azul=tkinter.Button(ventana1,width=5,bg="blue",command=cambio1)
verde=tkinter.Button(ventana1,width=5,bg="lightgreen",command=cambio2)
amarillo=tkinter.Button(ventana1,width=5,bg="yellow",command=cambio3)
color_personal=tkinter.Entry(ventana1,text="#000000",width=8)
boton_personal=tkinter.Button(ventana1,text="GO!",command=personalizado)

colores.pack()
colores.place(anchor="center",relx=0.5,rely=0.5)

rojo.pack()
rojo.place(anchor="center",relx=0.25,rely=0.56)

azul.pack()
azul.place(anchor="center",relx=0.73,rely=0.56)

verde.pack()
verde.place(anchor="center",relx=0.25,rely=0.62)

amarillo.pack()
amarillo.place(anchor="center",relx=0.73,rely=0.62)

color_personal.pack()
color_personal.place(anchor="center",relx=0.3,rely=0.70)
color_personal.insert(0, "#000000")

boton_personal.pack()
boton_personal.place(anchor="center",relx=0.75,rely=0.7)

#Width
grosor=tkinter.Label(ventana1,text="Grosor:",bg="white")
grosor_numero=tkinter.Label(ventana1,text=width,bg="white")

grueso=tkinter.Button(ventana1,font=("Arial",12,"bold"),text="+",command=grueso)
delgado=tkinter.Button(ventana1,font=("Arial",13,"bold"),text="-",command=delgado)

grosor.pack()
grosor.place(anchor="center",relx=0.26,rely=0.77)

grosor_numero.pack()
grosor_numero.place(anchor="center",relx=0.24,rely=0.81)

grueso.pack()
grueso.place(anchor="center",relx=0.65,rely=0.79)

delgado.pack()
delgado.place(anchor="center",relx=0.88,rely=0.79)

#Fin
ventana.mainloop()
