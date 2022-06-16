from ast import If
from itertools import count
from tkinter import *
from dibujos import draw
from colores import colores

def drawnumbers(canvas,entrada,Colores,coordenadas,porte): #Hace las validaciones necesarias para que se dibuje de manera correcta en el canvas
    
    #----------------------------Declaracion de variables----------------------------------
    j=0
    lastdiv=0
    alturadiv=90
    signos=["+","*","-"]
    aux=""
    inparentesis=False
    esDenominador=False
    inparentesiselevado=False
    division=0
    elevado=0
    parsize=0
    mover=len(entrada)*(60-porte)
    esDenominador=0
    #---------------------------------------------------------------------------------------
    #pseudo limite de caracteres
    if len(entrada)>1000:
        canvas.create_text(180,50,text="Demasiados caracteres :c")
    else:
        for i in entrada:
            #-------------------------------------------------------------------------------------
            #si el caracter que acaba de ser agregado es una division
            if i =="/":
                mover=mover+60*(division)   #movemos la division para que se ponga bajo el numerador
                division=largodiv(j,entrada)    #la variable division ayuda a que el denominador se ponga bajo el numerador
                if(lastdiv!=0):
                    esDenominador=lastdiv
                    if(aux==")"):
                        esDenominador+=2*tamaniopc(entrada,j-1)# da mas espacio a las divisiones 
            #------------------------------------------------------------
            #detecta cuando las operaciones están o no en parentesis
            if aux=="(":
                inparentesis=True
                inparentesiselevado=True
            if aux==")":
                inparentesis=False
                inparentesiselevado=False
            #------------------------------------------------------------
            #detecta cuando el termino anterior es un elevado, por lo tanto, los siguientes caracteres deberan ser escritos como potencias
            if aux=="^":
                elevado=10
                esDenominador2=esDenominador
                #if esDenominador>0:
                #    esDenominador=esDenominador-alturadiv
                #    if(entrada[j-4]=="/"):
                #        esDenominador=esDenominador-alturadiv
            #------------------------------------------------------------
            #determina el fin del elevado
            elif i in signos and not(inparentesiselevado):
                elevado=0
            #------------------------------------------------------------
            #mueve hacia la izquierda
            if j>0:
                    mover=mover-60
            #------------------------------------------------------------
            #determina lo que pasa cuando el caracter anterior fue una devision, es decir, estos son los denominadores
            if aux =="/":
                esDenominador+=alturadiv
                lastdiv=esDenominador
                mover=mover+60
                #elevado=0
            elif i in signos and not(inparentesis): 
                esDenominador=0
                lastdiv=0
            #--------------------------------------------------------------------------------------------------
            #determina el tamaño de los parentesis
            if (i=="("):
                parsize=tamaniopa(entrada,j);
            if (i==")"):
                parsize=tamaniopc(entrada,j);
                esDenominador2=esDenominador
                if esDenominador>0 and parsize>0:
                    esDenominador=esDenominador-alturadiv
            #--------------------------------------------------------------------------------------------------
            #detiene de emergencia el elevado
            if (aux=="P"):
                elevado=0
            #-------------------------------------------------------------------------------------------------
            #despues de todas las condiciones anteriores, manda el caracter y sus datos a la funcion de dibujar
            draw(canvas,i,mover,Colores,esDenominador,coordenadas,porte,division,elevado,parsize)
            j=j+1
            if aux=="^" or i==")":
                esDenominador=esDenominador2
            aux=i #termino anterior 

def largodiv(indice,entrada):  #cuenta el largo de los numeradores 
    signos=["+","*","/","-","(",")"]
    cont=0
    aux=False
    aux2=0
    print(entrada[indice])
    if entrada[indice-1]==")":
        cont+=1
        aux=True
        aux2+=1
        indice-=1
    indice-=1
    while indice>=0:
        if aux:
            if(entrada[indice]=="/"):
                cont+=1
                break
            if entrada[indice]==")":
                aux2+=1
            if entrada[indice]!="(":
                cont+=1  
            else:
                aux2-=1
                if(aux2==0):
                    cont+=1
                    break
                else:
                    cont+=1     
        else:
            if not(entrada[indice] in signos):
                cont+=1
            if entrada[indice] in signos:
                break
                  
        indice-=1
    print(cont)
    return cont
#

#Cuenta que tantas divisiones hay dentro de un parentesis de apertura, esto para hacerlo del tamaño correcto
def tamaniopa(cadena, indice):
    cont=indice
    contador=0
    aux1=0
    while cont<len(cadena):
        if cadena[cont]=="/":
            contador+= 40
        if(cadena[cont]=="("):
            #print("se suma 1 al aux. se encontr ( en la posicion ",cont)
            aux1+=1
        if(cadena[cont]==")"):
            #print("se resta 1 al aux. se encontr ) en la posicion ",cont)
            aux1-=1
            if(aux1==0):
            #    print("se retorna porque es 0 en la posicion ",cont)
                return contador
        cont+=1
    return 0
def tamaniopc(cadena, indice): #lo mismo que el de arriba pero para los parentesis de cierre
   # print()
    cont=indice
    contador=0
    aux1=0
    while cont>=0:
        if cadena[cont]=="/":
           # print("se encontró una division se suman 40")
            contador+= 40
        if(cadena[cont]==")"):
            #print("se suma 1 al aux. se encontr ) en la posicion ",cont)
            aux1+=1
        if(cadena[cont]=="("):
           # print("se resta 1 al aux. se encontr ) en la posicion ",cont)
            aux1-=1
            if(aux1==0):
             #   print("se retorna porque es 0 en la posicion ",cont)
                return contador
        cont-=1
    return 0
