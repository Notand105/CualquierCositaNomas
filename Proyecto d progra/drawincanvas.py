from ast import If
from itertools import count
from tkinter import *
from dibujos import draw
from colores import colores

def drawnumbers(canvas,entrada,Colores,coordenadas,porte):
    j=0
    signos=["+","*","/","-"]
    aux=""
    inparentesis=False
    esDenominador=False
    inparentesiselevado=False
    division=0
    elevado=0
    mover=len(entrada)*(60-porte)
    if len(entrada)>1000:
        canvas.create_text(180,50,text="Demasiados caracteres :c")
    else:
        for i in entrada:
            if i =="/":
                mover=mover+60
                division=largodiv(j,entrada)
            if aux=="(":
                inparentesis=True
            if aux==")":
                inparentesis=False
            if aux=="^":
                elevado=50
            elif i in signos and not(inparentesiselevado):
                elevado=0
            if j>0:
                mover=mover-60
            if aux =="/":
                esDenominador+=80
                mover=mover+60
            elif i in signos and not(inparentesis):
                esDenominador=0

            draw(canvas,i,mover,Colores,esDenominador,coordenadas,porte,division,elevado)
            j=j+1
            aux=i #termino anterior 

def largodiv(indice,entrada):
    signos=["+","*","/","-"]
    cont=0
    aux=False
    print(entrada[indice])
    if entrada[indice-1]==")":
        cont+=1
        aux=True
    indice-=1
    while indice>=0:
        if aux:
            if entrada[indice]!="(":
                cont+=1  
            else:
                cont+=1
                break     
        else:
            if not(entrada[indice] in signos):
                cont+=1
            if entrada[indice] in signos:
                break
                  
        indice-=1
    #print(cont)
    return cont
