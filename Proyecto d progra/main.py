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

def is_operator(c): #devuelve si es operador o no
    return c=="*" or c=="/" or  c=="-" or c=="+" or c=="^"

def is_parentesis(c): #devuelve si es parentesis
    return c=="(" or c==")"

def val_input(c): #valida que la entrada sea coherente
    el = entrada.cget("text") # obtener la lista de caracteres de la calculadora.
    if(len(el) >= 1 and el[-1] == "("): return( c != ")" and not is_operator(c) ) or (c == "-")#validacion para no permitir el ingreso de parentesis de cierre y operadores despues de uno de apertura
    if(len(el)>=1 and el[-1]==")" and c.isnumeric()):return False#no agregar numeros despues de un parentesis de cierre 
    if(len(el)>=1 and el[-1].isnumeric() and c=="("):return False#no agregar numeros antes de un parentesis de apertura
    if(len(el)>=1 and (el[-1] =="s" or el[-1] =="c" or el[-1] =="t") and c!="(" ):return False
    if(len(el)>=1 and el[-1]=="!" and not (c.isnumeric()) ):return True
    if not (is_operator(c)): return True # si la entrada no es un operador, pintalo
    if(len(el) == 1 and is_operator(el[-1])): return False # si hay exatamente un elemento en la calculadora y es un operador, no pinta
    if(len(el) > 1 and is_operator(el[-1]) and is_operator(el[-2])): return False # si hay dos o mas elementos en la calculadora y los dos ultimos son operadores, no pinta
    if(len(el) == 0): return c == "-" # si no hay elementos en la calculadora, pinta solo si la entrada es "-"
    if(is_operator(el[-1])): return c == "-" # si el ultimo caracter es un operador, pinta solo si la entrada es "-"
    if(el[-1] == c ): return  c=="-" # si el ultimo caracter es igual a la entrada, pinta solo si la entrada es "-"
    return True # pinta

def add_caracter(caracter): #Añade los nuevos caracteres a la interfaz
    global Colores
    global cadena
    global coordenadas
    global base
    global nventanaBot
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
    elif caracter=="√":
        if(len(entrada.cget("text"))==0): entrada.config(text=entrada.cget("text")+"(")
        elif(len(entrada.cget("text"))>=1 and entrada.cget("text")[-1]!="("):
            entrada.config(text=entrada.cget("text")+"(")
        entrada.config(text=entrada.cget("text")+caracter)
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
    entradaVentana.config(text=EntradaEnInterfaz(cadenaIntegra))
    if(caracter!="^" and caracter!="P"):
        if(caracter!="^" and caracter!="P"):
            canvas.delete("all")
            drawnumbers(canvas, cadena,Colores,coordenadas,SizeNumeros) 
        canvas.configure(scrollregion = canvas.bbox("all"))
        if(caracter=="t" or caracter=="s" or caracter=="c"):add_caracter("(")

def EntradaEnInterfaz(cadena): #hace reemplazos parar que tenga sentido la salida de texto
    if "s" in cadena:
        cadena=[item.replace("s", "sin") for item in cadena] #remplaza las s por sin, para que se muestre bien en la salida de la interfaz
    if "c" in cadena:
        cadena=[item.replace("c", "cos") for item in cadena] #lo de arriba para coseno
    if "t" in cadena:
        cadena=[item.replace("t", "tan") for item in cadena] #lo de arriba para tangente
    if "P" in cadena:
        cadena=cadena.replace("P","")
    return cadena
    
def comprobar(): #comprueba la logica de parentesis
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
        if(i.isnumeric()): #recorrer cada elemento de la entrada, y los numeros cambiarlos a binario con la funcion que incluye pyhton y los operadores los dejas igual
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
    Numero1=Button(changeSize,text="Muy Grande ",command=partial(getsize,-10)).pack()
    Numero2=Button(changeSize,text="Grande ",command=partial(getsize,-5)).pack()
    Numero3=Button(changeSize,text="Medio ",command=partial(getsize,0)).pack()
    Numero4=Button(changeSize,text="Medio bajo ",command=partial(getsize,5)).pack()
    Numero5=Button(changeSize,text="Pequeño ",command=partial(getsize,10)).pack()
    changeSize.wait_window()
    nventanaSize = False
def getsize(valor):
    global SizeNumeros
    SizeNumeros=valor
    add_caracter("pass")

def mostrar_botones():
    global botones
    if botones == "Ocultar Botones":
        botones = "Mostrar Botones"
        btnDel.place_forget()
        btn13.place_forget()
        btn12.place_forget()
        btn11.place_forget()
        btn10.place_forget()
        btn14.place_forget()
        btn7.place_forget()
        btn8.place_forget()
        btn9.place_forget()
        btn4.place_forget()
        btn5.place_forget()
        btn6.place_forget()
        btn0.place_forget()
        btn1.place_forget()
        btn2.place_forget()
        btn3.place_forget()
        btnRes.place_forget()
        btnParI.place_forget()
        btnParD.place_forget()
        btnPot.place_forget()
        btnFact.place_forget()
        btnSeno.place_forget()
        btnCoseno.place_forget()
        btnTan.place_forget()
        btnGrado.place_forget()
        btnAC.place_forget()
        btnParar.place_forget()
        entradaVentana.place(x=0, y=0)
        global nventanaBot
        global Colores
        ####################################################
        #evita que se pueda abrir varias veces la ventana cambio de color
        if nventanaBot:
            return 
        nventanaBot=True
        ###################################################
        NewBotones=Toplevel() #ventana para elegir colores
        NewBotones.geometry("500x600")
        new_btnParar=tk.Button(NewBotones,text="ES",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"P")).grid(row=3, column=9)

        new_btnDel=tk.Button(NewBotones,text="<--",width=8,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"<--")).grid(row=0, column=9)
        new_btnRes=tk.Button(NewBotones,text="=",width=6,height=1,bg="#B1D0E6",fg="black",command=Resultado).grid(row=3, column=2)
        #new_entradaVentana=Label(NewBotones,text=entrada.cget("text"),font=("consolas",16)).place(x=10,y=400)#contendra la entrada que se mostrará en la pantalla como texto
        new_btnPot=tk.Button(NewBotones,text="^",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"^")).grid(row=1, column=6)
        new_btnParI=tk.Button(NewBotones,text="(",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"(")).grid(row=0, column=5)
        new_btnParD=tk.Button(NewBotones,text=")",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,")")).grid(row=0, column=6)
        new_btnFact=tk.Button(NewBotones,text="!",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"!")).grid(row=1, column=5)
        new_btnSeno=tk.Button(NewBotones,text="sen()",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"s")).grid(row=3, column=4)
        new_btnCoseno=tk.Button(NewBotones,text="cos()",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"c")).grid(row=2, column=4)
        new_btnTan=tk.Button(NewBotones,text="Tan()",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"t")).grid(row=1, column=4)
        new_btnGrado=tk.Button(NewBotones,text="°",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"°")).grid(row=0, column=4)
        new_btn13=tk.Button(NewBotones,text="+",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"+")).grid(row=3, column=3)
        new_btn12=tk.Button(NewBotones,text="-",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"-")).grid(row=2, column=3)
        new_btn11=tk.Button(NewBotones,text="*",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"*")).grid(row=1, column=3)
        new_btn10=tk.Button(NewBotones,text="/",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"/")).grid(row=0, column=3)
        new_btn14=tk.Button(NewBotones,text=".",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,".")).grid(row=3, column=1)
        new_btn9=tk.Button(NewBotones,text="9",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"9")).grid(row=2, column=2)
        new_btn8=tk.Button(NewBotones,text="8",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"8")).grid(row=2, column=1)
        new_btn7=tk.Button(NewBotones,text="7",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"7")).grid(row=2, column=0)
        new_btn6=tk.Button(NewBotones,text="6",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"6")).grid(row=1, column=2)
        new_btn5=tk.Button(NewBotones,text="5",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"5")).grid(row=1, column=1)
        new_btn4=tk.Button(NewBotones,text="4",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"4")).grid(row=1, column=0)
        new_btn3=tk.Button(NewBotones,text="3",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"3")).grid(row=0, column=2)
        new_btn0=tk.Button(NewBotones,text="0",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"0")).grid(row=3, column=0)
        new_btn2=tk.Button(NewBotones,text="2",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"2")).grid(row=0, column=1)
        new_btn1=tk.Button(NewBotones,text="1",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"1")).grid(row=0, column=0)
        new_btnAC=tk.Button(NewBotones,text="AC",width=8,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"AC")).grid(row=1, column=9)
        NewBotones.wait_window()
        nventanaBot = False
    elif botones == "Mostrar Botones":
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
        btnParar.place(x=380,y=460)
        botones = "Ocultar Botones"
    opciones_menu.entryconfig(6,label=botones)
    add_caracter("pass")

def submit():
    signos=["+","*","/","!","^"]
    global cadena
    inp = inputtxt.get(1.0, "end-1c")   #toma el texto ingresado en el textbox
    if(len(cadena)==0 and inp[0] in signos):
        return
    inpxd= entrada.cget("text")+inp #agrega el texto del textbox con el texto anterior
    #if(len(cadena)>=1):
    #    print(cadena[-1] in signos)
    #    print(inp[0])
    if(len(cadena)>=1 and cadena[-1] in signos and inp[0] in signos ):  
        return
    if(not valsub(inp)):
        return
    entrada.config(text=inpxd)
    cadena=inpxd
    add_caracter("pass")
    inputtxt.delete("1.0","end")

def valsub(cad):
    signos=["+","*","/","!","^"]
    axu=True
    cont=0
    for i in cad:
        print(i)
        if(cont>=1):
            print(cad[cont]," ",cad[cont-1] )
            if(cad[cont] in signos and cad[cont-1] in signos):
                axu=False
        cont+=1
    return axu


new_entradaVentana=Label
SizeNumeros=0
nventanaSize=False
nventana=False
nventanaBot=False
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
entradaSafe=Label(window,text="")#copia de seguridad
Modo="Clasico" #guarda el modo del programa
coordenadas="mostrar coordenadas" 
base="Binario"
size="Cambiar tamaño"
botones="Ocultar Botones"
orden_bool=False

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

inputtxt = tk.Text(window,height = 1,width = 30) #textbox para recibir los parametros de entrada
btnRes=tk.Button(window,text="=",width=6,height=8,bg="#B1D0E6",fg="black",command=Resultado)
entradaVentana=Label(window,text="Calculadora Pulenta",font=("consolas",16))#contendra la entrada que se mostrará en la pantalla como texto
btnDel=tk.Button(window,text="<--",width=7,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"<--"))
btnParar=tk.Button(window,text="ES",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"P"))
btnPot=tk.Button(window,text="^",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"^"))
btnParI=tk.Button(window,text="(",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"("))
btnParD=tk.Button(window,text=")",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,")"))
btnFact=tk.Button(window,text="!",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"!"))
btnSeno=tk.Button(window,text="sen()",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"s"))
btnCoseno=tk.Button(window,text="cos()",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"c"))
btnTan=tk.Button(window,text="Tan()",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"t"))
btnGrado=tk.Button(window,text="°",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"°"))
btnRaiz=tk.Button(window,text="√",width=6,height=1,bg="#B1D0E6",fg="black",command=partial(add_caracter,"√"))
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
btnSubmit=tk.Button(window,text="Agregar",width=6,height=1,bg="#B1D0E6",fg="black",command=submit)
opciones_menu= Menu(mymenu)
mymenu.add_cascade(label="Opciones",menu=opciones_menu)
opcionColores=opciones_menu.add_command(label="Cambiar colores", command=cambiar_color)
opcionModo=opciones_menu.add_command(label=Modo,command=cambioModo)
opciones_menu.add_command(label=coordenadas,command=mostrar_coordenadas)
opciones_menu.add_command(label=base,command=cambio_base)
opciones_menu.add_command(label=size,command=cambioSize)
opciones_menu.add_command(label=botones,command=mostrar_botones)

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
btnRaiz.place(x=460,y=410)
btnParar.place(x=380,y=460)
inputtxt.place(x=100,y=560)
btnSubmit.place(x=450,y=560)

entradaVentana.place(x=100,y=520)
 #--------------------------- Fin elementos de la calculadora-----------------------#   
    

window.mainloop()