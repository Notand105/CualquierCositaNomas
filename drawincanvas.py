from ast import If
from tkinter import *
from dibujos import draw
from colores import colores

def drawnumbers(canvas,entrada,Colores,coordenadas,porte):
    j=0
    aux=""
    esDenominador=False
    mover=len(entrada)*(60-porte//4)
    if len(entrada)>1000:
        canvas.create_text(180,50,text="Demasiados caracteres :c")
    else:
        for i in entrada:
            if i =="/":
                mover=mover+60
            if j>0:
                mover=mover-60
            if aux =="/":
                esDenominador=True
                mover=mover+60
            draw(canvas,i,mover,Colores,esDenominador,coordenadas,porte)
            esDenominador=False
            j=j+1
            aux=i #termino anterior 
