from ast import operator
from cProfile import label
from cgitb import text
from distutils.command.config import config
from tkinter import colorchooser
from tkinter import *
#from PIL import ImageTk, Image
import tkinter
import re #permite uso de expresiones regulares
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
    window.deiconify() # volvemos a mostrar la calculadora una vez se cierre la ventana de inicio.

def on_closing():
    window.destroy()

cadena=[]

def is_number(c):
    return c=="0" or c=="1" or c=="2" or c=="3" or c=="4" or c=="5" or c=="6" or c=="7" or c=="8" or c=="9" or "."

def is_operator(c):
    return c=="*" or c=="/" or  c=="-" or c=="+"

def is_parentesis(c):
    return c=="(" or c==")"

def val_input(c):
    el = entrada.cget("text") # obtener la lista de caracteres de la calculadora.
    if(len(el) >= 1 and el[-1] == "("): return( c != ")" and not is_operator(c) ) or (c == "-")#validacion para no permitir el ingreso de parentesis de cierre y operadores despues de uno de apertura
    if(len(el)>=1 and (el[-1] =="s" or el[-1] =="c" or el[-1] =="t") and c!="(" ):return False
    if(len(el)>=1 and el[-1]=="!" and not (is_number(c)) ):return True
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
    global base
    
        #si quereremos borrar solo eliminamos el ultimo termino de la lista
    if caracter=="<--":         

        base="Binario"
        opciones_menu.entryconfig(4,label=base)
        entrada.config(text=entrada.cget("text")[:-1])
        cadena=cadena[:-1]

    elif caracter=="AC":
        base="Binario"
        opciones_menu.entryconfig(4,label=base)
        entrada.config(text="")
        cadena=""
    elif caracter==")":
        if comprobar() and val_input(caracter):
            entrada.config(text=entrada.cget("text")+caracter)
            cadena+=caracter
    elif caracter=="(":
        entrada.config(text=entrada.cget("text")+caracter)
        cadena+=caracter
    elif caracter=="pass":
        pass
    else:
        if (val_input(caracter)): 
            entrada.config(text=entrada.cget("text")+caracter) #agregamos el boton presionado a la lista de caracteres ingresado
            cadena+=caracter
    #ya sea que eliminemos o agreguemos pasamos nuevamente la entrada a la funcion de dibujar numeros
    cadenaIntegra=entrada.cget("text")
    if base=="Base 10":
        cadena=a_binario(cadena)    
    if base=="Binario":
        cadena=cadenaIntegra
    if(caracter!="^"):
        canvas.delete("all")
        drawnumbers(canvas, cadena,Colores,coordenadas,SizeNumeros) 
        entradaVentana.config(text=EntradaEnInterfaz(cadenaIntegra))
        canvas.configure(scrollregion = canvas.bbox("all"))
        if(caracter=="t" or caracter=="s" or caracter=="c"):add_caracter("(")

def EntradaEnInterfaz(cadena):
    if "s" in cadena:
        cadena=[item.replace("s", "sin") for item in cadena] #remplaza las s por sin, para que se muestre bien en la salida de la interfaz
    if "c" in cadena:
        cadena=[item.replace("c", "cos") for item in cadena] #lo de arriba para coseno
    if "t" in cadena:
        cadena=[item.replace("t", "tan") for item in cadena] #lo de arriba para tangente
    return cadena
    
def comprobar():
    cont=0
    con2=0
    global cadena
    for i in cadena:
        if i =="(":
            cont+=1
        elif i ==")":
            con2+=1
    if cont>con2:
        return True
    else:
        return False
def Resultado():
    global Colores
    global coordenadas
    cadenaResultado=entrada.cget("text")
    try:
        canvas.delete("all")
        res=eval(cadenaResultado)
        drawnumbers(canvas,str(res),Colores,coordenadas,SizeNumeros)
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
    elif(caracter=="(" or caracter==")"):
        Colores.colorpar=colorchooser.askcolor()
    elif(caracter=="t"):
        Colores.colorTan=colorchooser.askcolor()
    elif(caracter=="s"):
        Colores.colorSeno=colorchooser.askcolor()  
    elif(caracter=="c"):
        Colores.colorCos=colorchooser.askcolor()  
    elif(caracter=="!"):
        Colores.colorfact=colorchooser.askcolor()
    
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
    choiceColor.geometry("400x620")
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
    signoFact=Button(choiceColor,text="Color para el signo !: ",command=partial(getColor,"!")).pack()
    signoPar=Button(choiceColor,text="Color para los paréntesis: ",command=partial(getColor,"(")).pack()
    signoSen=Button(choiceColor,text="Color para el seno : ",command=partial(getColor,"s")).pack()
    signoTan=Button(choiceColor,text="Color para la tangente: ",command=partial(getColor,"t")).pack()
    signoCos=Button(choiceColor,text="Color para el coseno : ",command=partial(getColor,"c")).pack()
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

def cambio_base():
    global base
    if base == "Binario":
        base = "Base 10"
    elif base == "Base 10":
       base = "Binario"
    opciones_menu.entryconfig(4,label=base)
    add_caracter("pass")

def a_binario(cadena):
    cadena=entrada.cget("text")
    print(cadena)
    cadena2=[]
    cadena3=[]
    #transformar la cadena en lista
    for i in cadena:
        cadena3+=i
    cadena=cadena3
    print(cadena)
    #uniremos los numeros que esten juntos
    contador=0
    for j in range(0,10):
        contador=0
        for i in cadena:
            if i.isnumeric() :
                if contador>=1:
                    if cadena[contador-1].isnumeric():
                        cadena[contador-1:contador+1]= ["".join(cadena[contador-1:contador+1])]
            contador+=1

    #cadena2 contiene la cadena original pero transformada a binario
    for i in cadena:
        if(i.isnumeric()):
            cadena2+=format(int(i),"b")
        else:
            cadena2+=i
    return cadena2


def cambioSize():
    global nventanaSize
    global Colores
    ####################################################
    #evita que se pueda abrir varias veces la ventana cambio de color
    if nventanaSize:
        return 
    nventanaSize=True
    ###################################################
    changeSize=Toplevel() #ventana para elegir colores
    changeSize.geometry("400x420")
    Numero1=Button(changeSize,text="Muy Grande ",command=partial(getsize,-5)).pack()
    Numero2=Button(changeSize,text="Grande ",command=partial(getsize,0)).pack()
    Numero3=Button(changeSize,text="Medio ",command=partial(getsize,5)).pack()
    Numero4=Button(changeSize,text="Medio bajo ",command=partial(getsize,10)).pack()
    Numero5=Button(changeSize,text="Pequeño ",command=partial(getsize,15)).pack()
    changeSize.wait_window()
    nventanaSize = False
def getsize(valor):
    global SizeNumeros
    SizeNumeros=valor
    add_caracter("pass")

SizeNumeros=0
nventanaSize=False
nventana=False
Colores=colores()
window=Tk() 
#window.iconbitmap(os.path.join(os.path.dirname(__file__),'Img\FAVICONCOLOR.ico')) #agregamos ico para window con ruta no relativa
window.title("Calculadora Pulenta") #Titulo Pestaña window
window.withdraw() #ocultar la ventana de la calculadora para que no se vea mientras está la ventana de inicio
window.geometry("620x620") # resolucion de la ventana

new_window=Toplevel() #creacion de la ventana de inicio
new_window.geometry("520x420")
#new_window.iconbitmap(os.path.join(os.path.dirname(__file__),'Img\FAVICONCOLOR.ico')) #agregamos ico para new_window
new_window.protocol("WM_DELETE_WINDOW", on_closing) #en caso de que cierren el programa en la ventana de incio el programa se cierra completo

#imagen = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'Img\logo.png')).resize((320, 210))) #insertamos el logo con ruta no relativa. 
new_window.title("Calculadora Pulenta")# Titulo Pestaña new_window
#lbl=Label(new_window,image=imagen) #Insertamos el logo a la new_window
#lbl.place(x=5,y=-30) #Posicion Logo
btn=Button(new_window,text="Iniciar calculadora",command=iniciar)
btn.place(x=200,y=200)
bar=Progressbar(new_window,orient=HORIZONTAL,length=300)
bar.place(x=100,y=300)

#-------------------------- elementos de la calculadora (botones, etiquetas, etc...) 

entrada=Label(window,text="") #entrada tendra todos 
Modo="Clasico" #guarda el modo del programa
coordenadas="mostrar coordenadas" 
base="Binario"
size="Cambiar tamaño"

mymenu=Menu(window)
window.config(menu=mymenu)



frame=Frame(window,width=1000,height=100)
frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
canvas=Canvas(frame,height=200,width=650,bg="#B1D0E6",scrollregion=(0,0,1000,1000))
hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=650,height=200)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

btnRes=tk.Button(window,text="=",width=6,height=8,bg="#B1D0E6",fg="black",command=Resultado)
entradaVentana=Label(window,text="Calculadora Pulenta",font=("consolas",16))#contendra la entrada que se mostrará en la pantalla como texto
btnDel=tk.Button(window,text="<--",width=7,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"<--"))
btnPot=tk.Button(window,text="^",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"^"))
btnParI=tk.Button(window,text="(",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"("))
btnParD=tk.Button(window,text=")",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,")"))
btnFact=tk.Button(window,text="!",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"!"))
btnSeno=tk.Button(window,text="sen()",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"s"))
btnCoseno=tk.Button(window,text="cos()",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"c"))
btnTan=tk.Button(window,text="Tan()",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"t"))
btnGrado=tk.Button(window,text="°",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"°"))
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
btnAC=tk.Button(window,text="AC",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"AC"))
opciones_menu= Menu(mymenu)
mymenu.add_cascade(label="Opciones",menu=opciones_menu)
opcionColores=opciones_menu.add_command(label="Cambiar colores", command=cambiar_color)
opcionModo=opciones_menu.add_command(label=Modo,command=cambioModo)
opciones_menu.add_command(label=coordenadas,command=mostrar_coordenadas)
opciones_menu.add_command(label=base,command=cambio_base)
opciones_menu.add_command(label=size,command=cambioSize)
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
btnGrado.place(x=460,y=360)
btnAC.place(x=380,y=410)

entradaVentana.place(x=100,y=520)
 #--------------------------- Fin elementos de la calculadora-----------------------#   
    

window.mainloop()