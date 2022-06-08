from ast import If
from itertools import count
from tkinter import *
from dibujos import draw
from colores import colores

def drawnumbers(canvas,entrada,Colores,coordenadas,porte):
    j=0
    lastdiv=0
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
    if len(entrada)>1000:
        canvas.create_text(180,50,text="Demasiados caracteres :c")
    else:
        
        for i in entrada:
            if i =="/":
                if lastdiv>0:
                    mover=mover+60*(division-1)
                else:
                    mover=mover+60*(division)
                division=largodiv(j,entrada)
                if(lastdiv!=0):
                    esDenominador=lastdiv
                    #mover2=mover
                   # mover=mover+(60*4)
            if aux=="(":
                inparentesis=True
                inparentesiselevado=True
            if aux==")":
                inparentesis=False
                inparentesiselevado=False
            if aux=="^":
                elevado=10
                esDenominador2=esDenominador
                if esDenominador>0:
                    esDenominador=esDenominador-80
            elif i in signos and not(inparentesiselevado):
                elevado=0
            if j>0:
                #if i !="/":
                    mover=mover-60
            if aux =="/":
                esDenominador+=80
                lastdiv=esDenominador
                mover=mover+60
                elevado=0
            elif i in signos and not(inparentesis): 
                esDenominador=0
                lastdiv=0
            if (i=="("):
                parsize=tamaniopa(entrada,j);
            if (i==")"):
                
                parsize=tamaniopc(entrada,j);
                esDenominador2=esDenominador
                if esDenominador>0 and parsize>0:
                    esDenominador=esDenominador-80
            draw(canvas,i,mover,Colores,esDenominador,coordenadas,porte,division,elevado,parsize)
            j=j+1
            if aux=="^" or i==")":
                esDenominador=esDenominador2
            aux=i #termino anterior 

def largodiv(indice,entrada):
    signos=["+","*","/","-","(",")"]
    cont=0
    aux=False
    #print(entrada[indice])
    if entrada[indice-1]==")":
        cont+=1
        aux=True
    indice-=1
    while indice>=0:
        if aux:
            if entrada[indice]!="(":
                cont+=1  
            else:
                #cont+=1
                break     
        else:
            if not(entrada[indice] in signos):
                cont+=1
            if entrada[indice] in signos:
                break
                  
        indice-=1
    #print(cont)
    return cont
#

#Se puede hacer general si al ir hacia atras aumentas un contador cada que aparezca uno extra de cierre y se resta cada vez que aparezca otro
#de apertura, una vez que el contador sea 0, corresponde al de cada uno
def tamaniopa(cadena, indice):
    cont=indice
    while cont<len(cadena):
        if cadena[cont]=="/":
            return 40
        cont+=1
    return 0
def tamaniopc(cadena, indice):
    cont=indice
    while cont>=0:
        if cadena[cont]=="/":
            return 40
        cont-=1
        if cadena[cont]=="(":
            break;
    return 0

#def bigpar(cadena):
    #con el primer parentesis de apertura encontrar el ultimo parentesis de cierre que le corresponda, contar cuantas divisiones hay dentro 
    #aumentar en 40 la altura por cada uno
#    contapertura=0
#    contcierre=0
#    contap=[]
#    contci=[]
#    recorrido=0
#    cont=0
#    while recorrido<=len(cadena):
#        if cadena[recorrido]=="(":
#            contap.append([recorrido,contapertura+1])
#        elif cadena[recorrido]==")":
#            contci.append([recorrido,contcierre+1])
#    for i in cadena:
#        if i=="/":
#            cont+=1
#    return cont*40
    