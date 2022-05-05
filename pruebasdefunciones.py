from tkinter import *
from functools import partial
def add(caracter):
    global cadena 
    if caracter==")":
        if comprobar():
            cadena+=caracter
    else:
        cadena+=caracter
    entrada.config(text=cadena)

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

window=Tk()
btn1=Button(window,text="(",command=partial(add,"(")).pack()
btn2=Button(window,text=")",command=partial(add,")")).pack()
entrada=Label(window,text=" ")
entrada.pack()
cadena=entrada.cget("text")
window.mainloop()
