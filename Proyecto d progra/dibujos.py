from textwrap import fill
from tkinter.ttk import *
from tkinter import *
from turtle import width
from colores import colores #recomiendo modularizar es decir separar por carpetas las graficas de lo fuertes

#Dibujar en el canvas dependiendo del caracter recibido

def draw(canvas,caracter,desplazo,Colores,esDenominador,coordenadas,porte,division,elevado,parsize):
    if caracter=="1":
        
        canvas.create_line(600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color1[1])) #linea derecha arriba
        canvas.create_line(600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*4),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*4),width=3,fill=checkif(Colores.color1[1])) #linea derecha abajo
        if(coordenadas=="ocultar coordenadas"):

                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,40,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,70,600,100)
   
    elif caracter=="2":
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color2[1])) #linea arriba
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color2[1])) #linea derecha arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color2[1])) #linea del medio
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),570-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color2[1])) #linea izquiera abajo
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color2[1])) #linea abajo
            if(coordenadas=="ocultar coordenadas"):

                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,570,40)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,40,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,70,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,70,570,100)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,100,600,100)

    elif caracter=="3":
    
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color3[1])) #linea arriba
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color3[1])) #linea derecha arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color3[1])) #linea del medio
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color3[1])) #linea derecha abajo
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color3[1])) #linea abajo
            if(coordenadas=="ocultar coordenadas"):

                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,600,40)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,40,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,70,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,70,600,100)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,70,600,100)

    elif caracter=="4":     
        
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color4[1])) #linea izquiera arriba
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color4[1])) #linea derecha arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color4[1])) #linea del medio
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color4[1])) #linea derecha abajo
            if(coordenadas=="ocultar coordenadas"):

                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,570,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,40,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,70,600,70)
    elif caracter=="5":
        
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color5[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color5[1])) #linea arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color5[1])) #linea del medio
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color5[1])) #linea derecha abajo
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color5[1])) #linea abajo
            if(coordenadas=="ocultar coordenadas"):

                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,570,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,600,40)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,70,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,70,600,100)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,100,600,100)

    elif caracter=="6":
        
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),570-desplazo- aliniear(division,esDenominador),70+porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color6[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color6[1])) #linea arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color6[1])) #linea del medio
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*3),570-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color6[1])) #linea izquiera abajo
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color6[1])) #linea derecha abajo
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color6[1])) #linea abajo
            if(coordenadas=="ocultar coordenadas"):

                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,570,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,600,40)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,70,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,70,570,100)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,70,600,100)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,100,600,100)
    elif caracter=="7":
        
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color7[1])) #linea arriba
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color7[1])) #linea derecha arriba
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color7[1])) #linea derecha abajo
            if(coordenadas=="ocultar coordenadas"):
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,600,40)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,40,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,70,600,100)
    elif caracter=="8":
            #restar 20 a las de arriba, 40 alas de abajo, 30 al medio  -(elevado*4)
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color8[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color8[1])) #linea arriba
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color8[1])) #linea derecha arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color8[1])) #linea del medio
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*3),570-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*4),width=3,fill=checkif(Colores.color8[1])) #linea izquiera abajo
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*4),width=3,fill=checkif(Colores.color8[1])) #linea derecha abajo
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*4),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*4),width=3,fill=checkif(Colores.color8[1])) #linea abajo
            
            if(coordenadas=="ocultar coordenadas"):

                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,570,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,600,40)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,40,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,70,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,70,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,70,600,100)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,100,600,100)

    elif caracter=="9":
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color9[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color9[1])) #linea arriba
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color9[1])) #linea derecha arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.color9[1])) #linea del medio
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*4),width=3,fill=checkif(Colores.color9[1])) #linea derecha abajo
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*4),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*4),width=3,fill=checkif(Colores.color9[1])) #linea abajo
            if(coordenadas=="ocultar coordenadas"):
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,570,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,600,40)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,40,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,70,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,70,600,100)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,100,600,100)
    elif caracter=="0":
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),570-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color0[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color0[1])) #linea arriba
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*2),600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*2),width=3,fill=checkif(Colores.color0[1])) #linea derecha arriba
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*3),570-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*4),width=3,fill=checkif(Colores.color0[1])) #linea izquiera abajo
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),70-porte+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*4),width=3,fill=checkif(Colores.color0[1])) #linea derecha abajo
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*4),600-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*4),width=3,fill=checkif(Colores.color0[1])) #linea abajo
            if(coordenadas=="ocultar coordenadas"):
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,570,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,40,600,40)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,40,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,70,600,70)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,600,70,600,100)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,100,600,100)
    elif caracter=="-":
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),80-porte+esDenominador-(elevado*4),600-desplazo- aliniear(division,esDenominador),80-porte+esDenominador-(elevado*4),width=3,fill=checkif(Colores.colormenos[1])) #linea del medio
            if(coordenadas=="ocultar coordenadas"):
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,80,600,80)
    elif caracter=="+":
            canvas.create_line(585-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*3),585-desplazo- aliniear(division,esDenominador),100-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colormas[1])) #linea arriba medio
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),70+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colormas[1])) #linea del medio
            if(coordenadas=="ocultar coordenadas"):

                coord(canvas,desplazo,division,esDenominador,porte,elevado,585,40,585,100)
                coord(canvas,desplazo,division,esDenominador,porte,elevado,570,70,600,70)
    elif caracter=="/":
        canvas.create_line(570-desplazo-(60*((division))),110-porte+esDenominador-(elevado*3),610-desplazo,110-porte+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colordiv[1])) #linea diagonal derecha

    elif caracter=="*":
        
            canvas.create_line(570-desplazo- aliniear(division,esDenominador),50+porte//2+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),80+porte//2+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colormul[1]))
            canvas.create_line(600-desplazo- aliniear(division,esDenominador),50+porte//2+esDenominador-(elevado*3),570-desplazo- aliniear(division,esDenominador),80+porte//2+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colormul[1]))
            if(coordenadas=="ocultar coordenadas"):
                coord(canvas,desplazo,division,esDenominador,porte//2,elevado,570,50,600,80)
                coord(canvas,desplazo,division,esDenominador,porte//2,elevado,600,50,570,80)
    elif caracter==".":
            canvas.create_line(580-desplazo- aliniear(division,esDenominador),100-porte+esDenominador,585-desplazo- aliniear(division,esDenominador),100-porte+esDenominador,width=5,fill=checkif(Colores.colorpunt[1])) #linea izquiera arriba

    elif caracter=="(":
        canvas.create_line(590-desplazo- aliniear(division,esDenominador),30+esDenominador-(elevado*3),570-desplazo- aliniear(division,esDenominador),70+esDenominador+parsize-(elevado*3),590-desplazo- aliniear(division,esDenominador),110+esDenominador+(parsize*2)-(elevado*3),smooth="true",width=3,fill=checkif(Colores.colorpar[1]))
    elif caracter==")":
        canvas.create_line(600-desplazo- aliniear(division,esDenominador),30+esDenominador-(elevado*3),620-desplazo- aliniear(division,esDenominador),70+esDenominador+parsize-(elevado*3),600-desplazo- aliniear(division,esDenominador),110+esDenominador+(parsize*2)-(elevado*3),smooth="true",width=3,fill=checkif(Colores.colorpar[1]))
    elif caracter=="!":
        canvas.create_line(600-desplazo- aliniear(division,esDenominador),40+porte+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),85+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorfact[1]))
        canvas.create_line(597-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),width=5,fill=checkif(Colores.colorfact[1]))
    elif caracter=="s":
        #N
        canvas.create_line(630-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),630-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorSeno[1]))
        canvas.create_line(630-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),610-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorSeno[1]))
        canvas.create_line(610-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),610-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorSeno[1]))
        #i
        canvas.create_line(600-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),600-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorSeno[1]))
        #s
        canvas.create_line(590-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),570-desplazo- aliniear(division,esDenominador),75+esDenominador-(elevado*3),590-desplazo- aliniear(division,esDenominador),90+esDenominador-(elevado*3),570-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),smooth="true",width=3,fill=checkif(Colores.colorSeno[1]))
    elif caracter=="c":
        #s
        canvas.create_line(635-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),620-desplazo- aliniear(division,esDenominador),75+esDenominador-(elevado*3),640-desplazo- aliniear(division,esDenominador),90+esDenominador-(elevado*3),620-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),smooth="true",width=3,fill=checkif(Colores.colorCos[1]))
        #o
        canvas.create_line(610-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),590-desplazo- aliniear(division,esDenominador),80+esDenominador-(elevado*3),610-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),620-desplazo- aliniear(division,esDenominador),80+esDenominador-(elevado*3),610-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),smooth="true",width=3,fill=checkif(Colores.colorCos[1]))
        #c
        canvas.create_line(590-desplazo- aliniear(division,esDenominador),61+esDenominador-(elevado*3),570-desplazo- aliniear(division,esDenominador),80+esDenominador-(elevado*3),590-desplazo- aliniear(division,esDenominador),99+esDenominador-(elevado*3),smooth="true",width=3,fill=checkif(Colores.colorCos[1]))
    elif caracter=="t":
        #N
        canvas.create_line(630-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),630-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorTan[1]))
        canvas.create_line(630-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),610-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorTan[1]))
        canvas.create_line(610-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),610-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorTan[1]))
        #a
        canvas.create_line(600-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),610-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorTan[1]))
        canvas.create_line(600-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),590-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorTan[1]))
        canvas.create_line(610-desplazo- aliniear(division,esDenominador),80+esDenominador-(elevado*3),590-desplazo- aliniear(division,esDenominador),80+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorTan[1]))
        #t
        canvas.create_line(570-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),590-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorTan[1]))
        canvas.create_line(580-desplazo- aliniear(division,esDenominador),60+esDenominador-(elevado*3),580-desplazo- aliniear(division,esDenominador),100+esDenominador-(elevado*3),width=3,fill=checkif(Colores.colorTan[1]))
    elif caracter=="°":
        canvas.create_oval(580-desplazo- aliniear(division,esDenominador), 40+esDenominador-(elevado*3), 590-desplazo- aliniear(division,esDenominador), 50+esDenominador-(elevado*3), width=2,outline=checkif(Colores.colorpunt[1]))
    else:

        #canvas.create_text(180,50,text="No implementado aun")
        pass

#si los colores para algun caracter no están definidos, los pinta de color negro
def checkif(Cadena):
    if (len(Cadena)<=3):
        return "#000000"
    else:
        return Cadena

#mueve los numeros ciertos espacios a la izquierda cuando son denominadores
def aliniear(division,esden):
    if esden>0:
        return 40*division
    else:
        return 0

def coord(canvas,desplazo,division,esDenominador,porte,elevado,x1,y1,x2,y2):
    canvas.create_line(x1-5-desplazo- aliniear(division,esDenominador),y1+porte+esDenominador-(elevado*2),x1+5-desplazo- aliniear(division,esDenominador),y1-porte+esDenominador-(elevado*2),width=5) 
    canvas.create_line(x2-5-desplazo- aliniear(division,esDenominador),y2+porte+esDenominador-(elevado*2),x2+5-desplazo- aliniear(division,esDenominador),y2-porte+esDenominador-(elevado*2),width=5) 