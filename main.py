from ast import operator
from cProfile import label
from cgitb import text
from distutils.command.config import config
from tkinter import colorchooser
from tkinter import *
from PIL import ImageTk, Image
import tkinter
from tkinter.ttk import *
import time
import tkinter.font as tkFont
import tkinter as tk
from functools import partial #permite pasar parametros a las funciones de los bottones
from drawincanvas import drawnumbers #importamos nuestra propia libreria que dibujara los numeros
import os #Permite usar el path para rutas no relativas.
from colores import colores
#funcion para mostrar la barra de progreso en la pantalla de inicio
def iniciar():
    #mueve una barra de progreso
    tasks=10
    x=0
    while x<tasks:
        bar["value"]+=10
        x+=1
        time.sleep(0.02)
        window.update_idletasks()
    new_window.destroy()  
    window.deiconify() # volvemos a mostrar la calculadora una vez se cierre la ventana de inicio

def on_closing():
    window.destroy()

cadena=[]

def is_operator(c):
    return c=="*" or c=="/" or  c=="-" or c=="+"

def val_input(c):
    el = entrada.cget("text") # obtener la lista de caracteres de la calculadora

    if not (is_operator(c)): return True # si la entrada no es un operador, pintalo
    if(len(el) == 1 and is_operator(el[-1])): return False # si hay exatamente un elemento en la calculadora y es un operador, no pinta
    if(len(el) > 1 and is_operator(el[-1]) and is_operator(el[-2])): return False # si hay dos o mas elementos en la calculadora y los dos ultimos son operadores, no pinta
    if(len(el) == 0): return c == "-" # si no hay elementos en la calculadora, pinta solo si la entrada es "-"
    if(is_operator(el[-1])): return c == "-" # si el ultimo caracter es un operador, pinta solo si la entrada es "-"
    if(el[-1] == c ): return  c=="-" # si el ultimo caracter es igual a la entrada, pinta solo si la entrada es "-"
    return True # pinta

def add_caracter(caracter):
    global Colores
    global cadena
    global coordenadas
    canvas.delete("all")
        #si quereremos borrar solo eliminamos el ultimo termino de la lista
    if caracter=="<--":         
        entrada.config(text=entrada.cget("text")[:-1])
        cadena=cadena[:-1]
    elif caracter=="pass":
        pass
    else:
        if (val_input(caracter)): 
            entrada.config(text=entrada.cget("text")+caracter) #agregamos el boton presionado a la lista de caracteres ingresado
            cadena+=caracter
    
    #ya sea que eliminemos o agreguemos pasamos nuevamente la entrada a la funcion de dibujar numeros
    drawnumbers(canvas, cadena,Colores,coordenadas) 
    entradaVentana.config(text=cadena)
    #entrada.cget("text")

def Resultado():
    global Colores
    global coordenadas
    try:
        canvas.delete("all")
        res=eval(entrada.cget("text"))
        drawnumbers(canvas,str(res),Colores,coordenadas)
    except Exception:
        pass

def getColor(caracter):
    global Colores
    global coordenadas
    if(caracter=="1"):
        Colores.color1=colorchooser.askcolor()
    elif(caracter=="2"):
        Colores.color2=colorchooser.askcolor()
    elif(caracter=="3"):
        Colores.color3=colorchooser.askcolor()
    elif(caracter=="4"):
        Colores.color4=colorchooser.askcolor()
    elif(caracter=="5"):
        Colores.color5=colorchooser.askcolor()
    elif(caracter=="6"):
        Colores.color6=colorchooser.askcolor()
    elif(caracter=="7"):
        Colores.color7=colorchooser.askcolor()
    elif(caracter=="8"):
        Colores.color8=colorchooser.askcolor()
    elif(caracter=="9"):
        Colores.color9=colorchooser.askcolor()
    elif(caracter=="0"):
        Colores.color0=colorchooser.askcolor()
    elif(caracter=="-"):
        Colores.colormenos=colorchooser.askcolor()
    elif(caracter=="+"):
        Colores.colormas=colorchooser.askcolor()
    elif(caracter=="*"):
        Colores.colormul=colorchooser.askcolor()
    elif(caracter=="/"):
        Colores.colordiv=colorchooser.askcolor()
    elif(caracter=="."):
        Colores.colorpunt=colorchooser.askcolor()
    add_caracter("pass")
    
def cambiar_color():
    global nventana
    global Colores
    ####################################################
    #evita que se pueda abrir varias veces la ventana cambio de color
    if nventana:
        return 
    nventana=True
    ###################################################
    choiceColor=Toplevel() #ventana para elegir colores
    choiceColor.geometry("400x420")
    Numero1=Button(choiceColor,text="Color para el número 1: ",command=partial(getColor,"1")).pack()
    Numero2=Button(choiceColor,text="Color para el número 2: ",command=partial(getColor,"2")).pack()
    Numero3=Button(choiceColor,text="Color para el número 3: ",command=partial(getColor,"3")).pack()
    Numero4=Button(choiceColor,text="Color para el número 4: ",command=partial(getColor,"4")).pack()
    Numero5=Button(choiceColor,text="Color para el número 5: ",command=partial(getColor,"5")).pack()
    Numero6=Button(choiceColor,text="Color para el número 6: ",command=partial(getColor,"6")).pack()
    Numero7=Button(choiceColor,text="Color para el número 7: ",command=partial(getColor,"7")).pack()
    Numero8=Button(choiceColor,text="Color para el número 8: ",command=partial(getColor,"8")).pack()
    Numero9=Button(choiceColor,text="Color para el número 9: ",command=partial(getColor,"9")).pack()
    Numero0=Button(choiceColor,text="Color para el número 0: ",command=partial(getColor,"0")).pack()
    signomenos=Button(choiceColor,text="Color para el signo -: ",command=partial(getColor,"-")).pack()
    signomas=Button(choiceColor,text="Color para el signo +: ",command=partial(getColor,"+")).pack()
    signomul=Button(choiceColor,text="Color para el signo *: ",command=partial(getColor,"*")).pack()
    signodiv=Button(choiceColor,text="Color para el signo /: ",command=partial(getColor,"/")).pack()
    signopunt=Button(choiceColor,text="Color para el signo .: ",command=partial(getColor,".")).pack()
    choiceColor.wait_window()
    nventana = False

def cambioModo():
    global Modo
    if Modo =="Clasico":
        Modo="Cientifico"
        btnSeno.place_forget()
        btnPot.place_forget()
        btnFact.place_forget()
        btnCoseno.place_forget()
        btnTan.place_forget()
    elif Modo=="Cientifico":
        Modo="Clasico"
        btnPot.place(x=380,y=260)
        btnFact.place(x=460,y=260)
        btnSeno.place(x=380,y=310)
        btnCoseno.place(x=460,y=310)
        btnTan.place(x=380,y=360)
    opciones_menu.entryconfig(2,label=Modo)

def mostrar_coordenadas():
    global coordenadas
    if coordenadas == "mostrar coordenadas":
        coordenadas = "ocultar coordenadas"
    elif coordenadas == "ocultar coordenadas":
        coordenadas = "mostrar coordenadas"
    opciones_menu.entryconfig(3,label=coordenadas)
    add_caracter("pass")


nventana=False
Colores=colores()
window=Tk() 
window.iconbitmap(os.path.join(os.path.dirname(__file__),'Img\FAVICONCOLOR.ico')) #agregamos ico para window con ruta no relativa
window.title("Calculadora Pulenta") #Titulo Pestaña window
window.withdraw() #ocultar la ventana de la calculadora para que no se vea mientras está la ventana de inicio
window.geometry("620x620") # resolucion de la ventana

new_window=Toplevel() #creacion de la ventana de inicio
new_window.geometry("520x420")
new_window.iconbitmap(os.path.join(os.path.dirname(__file__),'Img\FAVICONCOLOR.ico')) #agregamos ico para new_window
new_window.protocol("WM_DELETE_WINDOW", on_closing) #en caso de que cierren el programa en la ventana de incio el programa se cierra completo

imagen = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'Img\logo.png')).resize((320, 210))) #insertamos el logo con ruta no relativa. 
new_window.title("Calculadora Pulenta")# Titulo Pestaña new_window
lbl=Label(new_window,image=imagen) #Insertamos el logo a la new_window
lbl.place(x=5,y=-30) #Posicion Logo
btn=Button(new_window,text="Iniciar calculadora",command=iniciar)
btn.place(x=200,y=200)
bar=Progressbar(new_window,orient=HORIZONTAL,length=300)
bar.place(x=100,y=300)

#-------------------------- elementos de la calculadora (botones, etiquetas, etc...) 

entrada=Label(window,text="") #entrada tendra todos 
Modo="Clasico" #guarda el modo del programa
coordenadas="mostrar coordenadas" 
entradaVentana=Label(window,text="Calculadora Pulenta",font=("consolas",16))#contendra la entrada que se mostrará en la pantalla como texto
mymenu=Menu(window)
window.config(menu=mymenu)
btnRes=tk.Button(window,text="=",width=6,height=8,bg="#B1D0E6",fg="black",command=Resultado)
canvas=Canvas(window,height=200,width=620,bg="#B1D0E6")
btnDel=tk.Button(window,text="<--",width=7,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"<--"))
btnPot=tk.Button(window,text="^",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"pass"))
btnParI=tk.Button(window,text="(",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"pass"))
btnParD=tk.Button(window,text=")",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"pass"))
btnFact=tk.Button(window,text="!",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"pass"))
btnSeno=tk.Button(window,text="sen()",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"pass"))
btnCoseno=tk.Button(window,text="cos()",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"pass"))
btnTan=tk.Button(window,text="Tan()",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"pass"))
btn13=tk.Button(window,text="+",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"+"))
btn12=tk.Button(window,text="-",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"-"))
btn11=tk.Button(window,text="*",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"*"))
btn10=tk.Button(window,text="/",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"/"))
btn14=tk.Button(window,text=".",width=7,height=2,bg="#B1D0E6",fg="black",command=partial(add_caracter,"."))
btn9=tk.Button(window,text="9",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"9"))
btn8=tk.Button(window,text="8",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"8"))
btn7=tk.Button(window,text="7",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"7"))
btn6=tk.Button(window,text="6",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"6"))
btn5=tk.Button(window,text="5",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"5"))
btn4=tk.Button(window,text="4",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"4"))
btn3=tk.Button(window,text="3",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"3"))
btn2=tk.Button(window,text="2",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"2"))
btn1=tk.Button(window,text="1",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"1"))
btn0=tk.Button(window,text="0",width=19,height=2,bg="#B1D0E6",fg="black",command=partial(add_caracter,"0"))
opciones_menu= Menu(mymenu)
mymenu.add_cascade(label="Opciones",menu=opciones_menu)
opcionColores=opciones_menu.add_command(label="Cambiar colores", command=cambiar_color)
opcionModo=opciones_menu.add_command(label=Modo,command=cambioModo)
opciones_menu.add_command(label=coordenadas,command=mostrar_coordenadas)
canvas.pack()
btnDel.place(x=280,y=410)
btn13.place(x=280,y=210)
btn12.place(x=190,y=210)
btn11.place(x=100,y=210)
btn10.place(x=10,y=210)
btn14.place(x=190,y=410)
btn7.place(x=10,y=260)
btn8.place(x=100,y=260)
btn9.place(x=190,y=260)
btn4.place(x=10,y=310)
btn5.place(x=100,y=310)
btn6.place(x=190,y=310)
btn0.place(x=10,y=410)
btn1.place(x=10,y=360)
btn2.place(x=100,y=360)
btn3.place(x=190,y=360)
btnRes.place(x=280,y=260)
btnParI.place(x=380,y=210)
btnParD.place(x=460,y=210)
btnPot.place(x=380,y=260)
btnFact.place(x=460,y=260)
btnSeno.place(x=380,y=310)
btnCoseno.place(x=460,y=310)
btnTan.place(x=380,y=360)

entradaVentana.place(x=20,y=500)
 #--------------------------- Fin elementos de la calculadora-----------------------#   
    

window.mainloop()