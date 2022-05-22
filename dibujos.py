from tkinter.ttk import *
from tkinter import *
from turtle import width
from colores import colores #recomiendo modularizar es decir separar por carpetas las graficas de lo fuertes
def draw(canvas,caracter,desplazo,Colores,esDenominador,coordenadas,porte,division,elevado):
    if caracter=="1":
        
        canvas.create_line(600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado/3),600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado),width=3,fill=checkif(Colores.color1[1])) #linea derecha arriba
        canvas.create_line(600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado),width=3,fill=checkif(Colores.color1[1])) #linea derecha abajo
            
    elif caracter=="2":
            canvas.create_line(570-desplazo,40+porte+esDenominador-(elevado/3),600-desplazo,40+porte+esDenominador-(elevado/3),width=3,fill=checkif(Colores.color2[1])) #linea arriba
            canvas.create_line(600-desplazo,40+porte+esDenominador-(elevado/3),600-desplazo,70+esDenominador-(elevado),width=3,fill=checkif(Colores.color2[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,70+esDenominador-(elevado),600-desplazo,70+esDenominador-(elevado),width=3,fill=checkif(Colores.color2[1])) #linea del medio
            canvas.create_line(570-desplazo,70+esDenominador-(elevado),570-desplazo,100-porte+esDenominador-(elevado),width=3,fill=checkif(Colores.color2[1])) #linea izquiera abajo
            canvas.create_line(570-desplazo,100-porte+esDenominador-(elevado),600-desplazo,100-porte+esDenominador-(elevado),width=3,fill=checkif(Colores.color2[1])) #linea abajo
           
    elif caracter=="3":
    
            canvas.create_line(570-desplazo,40+porte+esDenominador,600-desplazo,40+porte+esDenominador,width=3,fill=checkif(Colores.color3[1])) #linea arriba
            canvas.create_line(600-desplazo,40+porte+esDenominador,600-desplazo,70-porte+esDenominador,width=3,fill=checkif(Colores.color3[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,70+esDenominador,600-desplazo,70+esDenominador,width=3,fill=checkif(Colores.color3[1])) #linea del medio
            canvas.create_line(600-desplazo,70-porte+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color3[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,100-porte+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color3[1])) #linea abajo
       
    elif caracter=="4":     
        
            canvas.create_line(570-desplazo,40+porte+esDenominador,570-desplazo,70+esDenominador,width=3,fill=checkif(Colores.color4[1])) #linea izquiera arriba
            canvas.create_line(600-desplazo,40+porte+esDenominador,600-desplazo,70+esDenominador,width=3,fill=checkif(Colores.color4[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,70+esDenominador,600-desplazo,70+esDenominador,width=3,fill=checkif(Colores.color4[1])) #linea del medio
            canvas.create_line(600-desplazo,70-porte+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color4[1])) #linea derecha abajo
            
    elif caracter=="5":
        
            canvas.create_line(570-desplazo,40+porte+esDenominador,570-desplazo,70+esDenominador,width=3,fill=checkif(Colores.color5[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,40+porte+esDenominador,600-desplazo,40+porte+esDenominador,width=3,fill=checkif(Colores.color5[1])) #linea arriba
            canvas.create_line(570-desplazo,70+esDenominador,600-desplazo,70+esDenominador,width=3,fill=checkif(Colores.color5[1])) #linea del medio
            canvas.create_line(600-desplazo,70+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color5[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,100-porte+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color5[1])) #linea abajo

    elif caracter=="6":
        
            canvas.create_line(570-desplazo,40+porte+esDenominador,570-desplazo,70+porte+esDenominador,width=3,fill=checkif(Colores.color6[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,40+porte+esDenominador,600-desplazo,40+porte+esDenominador,width=3,fill=checkif(Colores.color6[1])) #linea arriba
            canvas.create_line(570-desplazo,70+esDenominador,600-desplazo,70+esDenominador,width=3,fill=checkif(Colores.color6[1])) #linea del medio
            canvas.create_line(570-desplazo,70-porte+esDenominador,570-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color6[1])) #linea izquiera abajo
            canvas.create_line(600-desplazo,70+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color6[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,100-porte+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color6[1])) #linea abajo
    elif caracter=="7":
        
            canvas.create_line(570-desplazo,40+porte+esDenominador,600-desplazo,40+porte+esDenominador,width=3,fill=checkif(Colores.color7[1])) #linea arriba
            canvas.create_line(600-desplazo,40+porte+esDenominador,600-desplazo,70-porte+esDenominador,width=3,fill=checkif(Colores.color7[1])) #linea derecha arriba
            canvas.create_line(600-desplazo,70-porte+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color7[1])) #linea derecha abajo

    elif caracter=="8":
        
            canvas.create_line(570-desplazo,40+porte+esDenominador,570-desplazo,70-porte+esDenominador,width=3,fill=checkif(Colores.color8[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,40+porte+esDenominador,600-desplazo,40+porte+esDenominador,width=3,fill=checkif(Colores.color8[1])) #linea arriba
            canvas.create_line(600-desplazo,40+porte+esDenominador,600-desplazo,70-porte+esDenominador,width=3,fill=checkif(Colores.color8[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,70+esDenominador,600-desplazo,70+esDenominador,width=3,fill=checkif(Colores.color8[1])) #linea del medio
            canvas.create_line(570-desplazo,70-porte+esDenominador,570-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color8[1])) #linea izquiera abajo
            canvas.create_line(600-desplazo,70-porte+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color8[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,100-porte+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color8[1])) #linea abajo

    elif caracter=="9":
       
            canvas.create_line(570-desplazo,40+porte+esDenominador,570-desplazo,70+esDenominador,width=3,fill=checkif(Colores.color9[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,40+porte+esDenominador,600-desplazo,40+porte+esDenominador,width=3,fill=checkif(Colores.color9[1])) #linea arriba
            canvas.create_line(600-desplazo,40+porte+esDenominador,600-desplazo,70-porte+esDenominador,width=3,fill=checkif(Colores.color9[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,70+esDenominador,600-desplazo,70+esDenominador,width=3,fill=checkif(Colores.color9[1])) #linea del medio
            canvas.create_line(600-desplazo,70-porte+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color9[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,100-porte+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color9[1])) #linea abajo

    elif caracter=="0":
        
            canvas.create_line(570-desplazo,40+porte+esDenominador,570-desplazo,70-porte+esDenominador,width=3,fill=checkif(Colores.color0[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,40+porte+esDenominador,600-desplazo,40+porte+esDenominador,width=3,fill=checkif(Colores.color0[1])) #linea arriba
            canvas.create_line(600-desplazo,40+porte+esDenominador,600-desplazo,70-porte+esDenominador,width=3,fill=checkif(Colores.color0[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,70-porte+esDenominador,570-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color0[1])) #linea izquiera abajo
            canvas.create_line(600-desplazo,70-porte+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color0[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,100-porte+esDenominador,600-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.color0[1])) #linea abajo

    elif caracter=="-":
        
            canvas.create_line(570-desplazo,80-porte+esDenominador,600-desplazo,80-porte+esDenominador,width=3,fill=checkif(Colores.colormenos[1])) #linea del medio

    elif caracter=="+":
        
            canvas.create_line(585-desplazo,40+porte+esDenominador,585-desplazo,100-porte+esDenominador,width=3,fill=checkif(Colores.colormas[1])) #linea arriba medio
            canvas.create_line(570-desplazo,70+esDenominador,600-desplazo,70+esDenominador,width=3,fill=checkif(Colores.colormas[1])) #linea del medio

    elif caracter=="/":
        canvas.create_line(560-desplazo-(40*((division))),110-porte+esDenominador,610-desplazo,110-porte+esDenominador,width=3,fill=checkif(Colores.colordiv[1])) #linea diagonal derecha

    elif caracter=="*":
        
            canvas.create_line(570-desplazo,50+porte//2+esDenominador,600-desplazo,80+porte//2+esDenominador,width=3,fill=checkif(Colores.colormul[1]))
            canvas.create_line(600-desplazo,50+porte//2+esDenominador,570-desplazo,80+porte//2+esDenominador,width=3,fill=checkif(Colores.colormul[1]))

    elif caracter==".":
            canvas.create_line(580-desplazo,100-porte+esDenominador,585-desplazo,100-porte+esDenominador,width=5,fill=checkif(Colores.colorpunt[1])) #linea izquiera arriba

    elif caracter=="(":
        canvas.create_line(590-desplazo,30+esDenominador,570-desplazo,70+esDenominador,590-desplazo,110+esDenominador,smooth="true",width=3,fill=checkif(Colores.colorpunt[1]))
    elif caracter==")":
        canvas.create_line(590-desplazo,30+esDenominador,610-desplazo,70+esDenominador,590-desplazo,110+esDenominador,smooth="true",width=3,fill=checkif(Colores.colorpunt[1]))
    elif caracter=="!":
        canvas.create_line(600-desplazo,40+porte+esDenominador,600-desplazo,85+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(597-desplazo,100+esDenominador,600-desplazo,100+esDenominador,width=5,fill=checkif(Colores.colorpunt[1]))
    elif caracter=="s":
        #N
        canvas.create_line(630-desplazo,60+esDenominador,630-desplazo,100+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(630-desplazo,100+esDenominador,610-desplazo,60+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(610-desplazo,60+esDenominador,610-desplazo,100+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
        #i
        canvas.create_line(600-desplazo,100+esDenominador,600-desplazo,60+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
        #s
        canvas.create_line(590-desplazo,60+esDenominador,570-desplazo,75+esDenominador,590-desplazo,90+esDenominador,570-desplazo,100+esDenominador,smooth="true",width=3,fill=checkif(Colores.colorpunt[1]))
    elif caracter=="c":
        #s
        canvas.create_line(635-desplazo,60+esDenominador,620-desplazo,75+esDenominador,640-desplazo,90+esDenominador,620-desplazo,100+esDenominador,smooth="true",width=3,fill=checkif(Colores.colorpunt[1]))
        #o
        canvas.create_line(610-desplazo,60+esDenominador,590-desplazo,80+esDenominador,610-desplazo,100+esDenominador,620-desplazo,80+esDenominador,610-desplazo,60+esDenominador,smooth="true",width=3,fill=checkif(Colores.colorpunt[1]))
        #c
        canvas.create_line(590-desplazo,61+esDenominador,570-desplazo,80+esDenominador,590-desplazo,99+esDenominador,smooth="true",width=3,fill=checkif(Colores.colorpunt[1]))
    elif caracter=="t":
        #N
        canvas.create_line(630-desplazo,60+esDenominador,630-desplazo,100+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(630-desplazo,100+esDenominador,610-desplazo,60+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(610-desplazo,60+esDenominador,610-desplazo,100+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
        #a
        canvas.create_line(600-desplazo,60+esDenominador,610-desplazo,100+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(600-desplazo,60+esDenominador,590-desplazo,100+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(610-desplazo,80+esDenominador,590-desplazo,80+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
        #t
        canvas.create_line(570-desplazo,60+esDenominador,590-desplazo,60+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(580-desplazo,60+esDenominador,580-desplazo,100+esDenominador,width=3,fill=checkif(Colores.colorpunt[1]))
    else:

        #canvas.create_text(180,50,text="No implementado aun")
        pass

def checkif(Cadena):
    if (len(Cadena)<=3):
        return "#000000"
    else:
        return Cadena

def aliniear(division,esden):
    if esden>0:
        return 40*division
    else:
        return 0