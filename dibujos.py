from tkinter.ttk import *
from tkinter import *
from turtle import width
from colores import colores #recomiendo modularizar es decir separar por carpetas las graficas de lo fuertes
def draw(canvas,caracter,desplazo,Colores,esDenominador,coordenadas,porte):
    if caracter=="1":
        if not esDenominador:
            canvas.create_line(600-desplazo,40+porte,600-desplazo,70-porte,width=3,fill=checkif(Colores.color1[1])) #linea derecha arriba
            canvas.create_line(600-desplazo,70-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color1[1])) #linea derecha abajo
            if coordenadas=="ocultar coordenadas":
                canvas.create_line(595-desplazo,40+porte,605-desplazo,40-porte,width=5,fill=checkif(Colores.color1[1])) #linea derecha arriba
                canvas.create_line(595-desplazo,70-porte,605-desplazo,70-porte,width=5,fill=checkif(Colores.color1[1])) #linea derecha arriba

                canvas.create_line(595-desplazo,70+porte,605-desplazo,70-porte,width=5,fill=checkif(Colores.color1[1]))
                canvas.create_line(595-desplazo,100-porte,605-desplazo,100-porte,width=5,fil=checkif(Colores.color1[1]))

        else:
            canvas.create_line(600-desplazo,120,600-desplazo,140-porte,width=3,fill=checkif(Colores.color1[1])) #linea derecha arriba
            canvas.create_line(600-desplazo,140,600-desplazo,170-porte,width=3,fill=checkif(Colores.color1[1])) #linea derecha abajo
            if coordenadas=="ocultar coordenadas":
                canvas.create_line(600-desplazo,120,600-desplazo,120-porte,width=5,fill=checkif(Colores.color1[1]))
                canvas.create_line(600-desplazo,140,600-desplazo,140-porte,width=5,fill=checkif(Colores.color1[1]))

                canvas.create_line(600-desplazo,140,600-desplazo,140-porte,width=5,fill=checkif(Colores.color1[1]))
                canvas.create_line(600-desplazo,170,600-desplazo,170-porte,width=5,fill=checkif(Colores.color1[1]))

    elif caracter=="2":
        if not esDenominador:
            canvas.create_line(570-desplazo,40+porte,600-desplazo,40+porte,width=3,fill=checkif(Colores.color2[1])) #linea arriba
            canvas.create_line(600-desplazo,40+porte,600-desplazo,70,width=3,fill=checkif(Colores.color2[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,70,600-desplazo,70,width=3,fill=checkif(Colores.color2[1])) #linea del medio
            canvas.create_line(570-desplazo,70,570-desplazo,100-porte,width=3,fill=checkif(Colores.color2[1])) #linea izquiera abajo
            canvas.create_line(570-desplazo,100-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color2[1])) #linea abajo
            if coordenadas=="ocultar coordenadas":
                #coordenadas
                canvas.create_line(565-desplazo,40,575-desplazo,40-porte,width=5,fill=checkif(Colores.color2[1]))
                canvas.create_line(595-desplazo,40,605-desplazo,40-porte,width=5,fill=checkif(Colores.color2[1]))
                canvas.create_line(595-desplazo,40,605-desplazo,40-porte,width=5,fill=checkif(Colores.color2[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70-porte,width=5,fill=checkif(Colores.color2[1]))
                canvas.create_line(565-desplazo,70,575-desplazo,70-porte,width=5,fill=checkif(Colores.color2[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70-porte,width=5,fill=checkif(Colores.color2[1]))
                canvas.create_line(565-desplazo,70,575-desplazo,70-porte,width=5,fill=checkif(Colores.color2[1]))
                canvas.create_line(565-desplazo,100,575-desplazo,100-porte,width=5,fill=checkif(Colores.color2[1]))
                canvas.create_line(565-desplazo,100,575-desplazo,100-porte,width=5,fill=checkif(Colores.color2[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100-porte,width=5,fill=checkif(Colores.color2[1]))
        
        else:
            canvas.create_line(570-desplazo,120,600-desplazo,120-porte-porte,width=3,fill=checkif(Colores.color2[1])) #linea arriba
            canvas.create_line(600-desplazo,120,600-desplazo,150-porte-porte,width=3,fill=checkif(Colores.color2[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,150,600-desplazo,150-porte-porte,width=3,fill=checkif(Colores.color2[1])) #linea del medio
            canvas.create_line(570-desplazo,150,570-desplazo,180-porte-porte,width=3,fill=checkif(Colores.color2[1])) #linea izquiera abajo
            canvas.create_line(570-desplazo,180,600-desplazo,180-porte-porte,width=3,fill=checkif(Colores.color2[1])) #linea abajo   
    elif caracter=="3":
        if not esDenominador:
            canvas.create_line(570-desplazo,40+porte,600-desplazo,40+porte,width=3,fill=checkif(Colores.color3[1])) #linea arriba
            canvas.create_line(600-desplazo,40+porte,600-desplazo,70-porte,width=3,fill=checkif(Colores.color3[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,70,600-desplazo,70,width=3,fill=checkif(Colores.color3[1])) #linea del medio
            canvas.create_line(600-desplazo,70-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color3[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,100-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color3[1])) #linea abajo
            if coordenadas=="ocultar coordenadas":
                #coordenadas
                canvas.create_line(565-desplazo,40,575-desplazo,40-porte,width=5,fill=checkif(Colores.color3[1]))
                canvas.create_line(595-desplazo,40,605-desplazo,40-porte,width=5,fill=checkif(Colores.color3[1]))

                canvas.create_line(595-desplazo,40,605-desplazo,40-porte,width=5,fill=checkif(Colores.color3[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70-porte,width=5,fill=checkif(Colores.color3[1]))

                canvas.create_line(565-desplazo,70,575-desplazo,70-porte,width=5,fill=checkif(Colores.color3[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70-porte,width=5,fill=checkif(Colores.color3[1]))

                canvas.create_line(595-desplazo,70,605-desplazo,70-porte,width=5,fill=checkif(Colores.color3[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100-porte,width=5,fill=checkif(Colores.color3[1]))

                canvas.create_line(565-desplazo,100,575-desplazo,100-porte,width=5,fill=checkif(Colores.color3[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100-porte,width=5,fill=checkif(Colores.color3[1]))
        else:
            canvas.create_line(570-desplazo,120,600-desplazo,120-porte,width=3,fill=checkif(Colores.color3[1])) #linea arriba
            canvas.create_line(600-desplazo,120,600-desplazo,150-porte,width=3,fill=checkif(Colores.color3[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,150,600-desplazo,150-porte,width=3,fill=checkif(Colores.color3[1])) #linea del medio
            canvas.create_line(600-desplazo,150,600-desplazo,180-porte,width=3,fill=checkif(Colores.color3[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,180,600-desplazo,180-porte,width=3,fill=checkif(Colores.color3[1])) #linea abajo    
    elif caracter=="4":     
        if not esDenominador:  
            canvas.create_line(570-desplazo,40+porte,570-desplazo,70,width=3,fill=checkif(Colores.color4[1])) #linea izquiera arriba
            canvas.create_line(600-desplazo,40+porte,600-desplazo,70,width=3,fill=checkif(Colores.color4[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,70,600-desplazo,70,width=3,fill=checkif(Colores.color4[1])) #linea del medio
            canvas.create_line(600-desplazo,70-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color4[1])) #linea derecha abajo
            if coordenadas=="ocultar coordenadas":
                #coordenadas
                canvas.create_line(565-desplazo,40,575-desplazo,40,width=5,fill=checkif(Colores.color4[1]))
                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color4[1]))

                canvas.create_line(595-desplazo,40,605-desplazo,40,width=5,fill=checkif(Colores.color4[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color4[1]))

                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color4[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color4[1]))

                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color4[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color4[1]))
        else:
            canvas.create_line(570-desplazo,120,570-desplazo,150-porte,width=3,fill=checkif(Colores.color4[1])) #linea izquiera arriba
            canvas.create_line(600-desplazo,120,600-desplazo,150-porte,width=3,fill=checkif(Colores.color4[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,150,600-desplazo,150-porte,width=3,fill=checkif(Colores.color4[1])) #linea del medio
            canvas.create_line(600-desplazo,150,600-desplazo,180-porte,width=3,fill=checkif(Colores.color4[1])) #linea derecha abajo    
    elif caracter=="5":
        if not esDenominador:
            canvas.create_line(570-desplazo,40+porte,570-desplazo,70,width=3,fill=checkif(Colores.color5[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,40+porte,600-desplazo,40+porte,width=3,fill=checkif(Colores.color5[1])) #linea arriba
            canvas.create_line(570-desplazo,70,600-desplazo,70,width=3,fill=checkif(Colores.color5[1])) #linea del medio
            canvas.create_line(600-desplazo,70,600-desplazo,100-porte,width=3,fill=checkif(Colores.color5[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,100-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color5[1])) #linea abajo
            if coordenadas=="ocultar coordenadas":
                #coordenadas
                canvas.create_line(565-desplazo,40,575-desplazo,40,width=5,fill=checkif(Colores.color5[1]))
                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color5[1]))

                canvas.create_line(565-desplazo,40,575-desplazo,40,width=5,fill=checkif(Colores.color5[1]))
                canvas.create_line(595-desplazo,40,605-desplazo,40,width=5,fill=checkif(Colores.color5[1]))

                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color5[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color5[1]))

                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color5[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color5[1]))
            
                canvas.create_line(565-desplazo,100,575-desplazo,100,width=5,fill=checkif(Colores.color5[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color5[1]))
        else:
            canvas.create_line(570-desplazo,120,570-desplazo,150-porte,width=3,fill=checkif(Colores.color5[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,120,600-desplazo,120-porte,width=3,fill=checkif(Colores.color5[1])) #linea arriba
            canvas.create_line(570-desplazo,150,600-desplazo,150-porte,width=3,fill=checkif(Colores.color5[1])) #linea del medio
            canvas.create_line(600-desplazo,150,600-desplazo,180-porte,width=3,fill=checkif(Colores.color5[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,180,600-desplazo,180-porte,width=3,fill=checkif(Colores.color5[1])) #linea abajo 
    elif caracter=="6":
        if not esDenominador:
            canvas.create_line(570-desplazo,40+porte,570-desplazo,70+porte,width=3,fill=checkif(Colores.color6[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,40+porte,600-desplazo,40+porte,width=3,fill=checkif(Colores.color6[1])) #linea arriba
            canvas.create_line(570-desplazo,70,600-desplazo,70,width=3,fill=checkif(Colores.color6[1])) #linea del medio
            canvas.create_line(570-desplazo,70-porte,570-desplazo,100-porte,width=3,fill=checkif(Colores.color6[1])) #linea izquiera abajo
            canvas.create_line(600-desplazo,70,600-desplazo,100-porte,width=3,fill=checkif(Colores.color6[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,100-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color6[1])) #linea abajo
            if coordenadas=="ocultar coordenadas":
                #coordenadas
                canvas.create_line(565-desplazo,40,575-desplazo,40,width=5,fill=checkif(Colores.color6[1]))
                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color6[1]))

                canvas.create_line(565-desplazo,40,575-desplazo,40,width=5,fill=checkif(Colores.color6[1]))
                canvas.create_line(595-desplazo,40,605-desplazo,40,width=5,fill=checkif(Colores.color6[1]))

                canvas.create_line(565-desplazo,70,575-desplazo,70,width=3,fill=checkif(Colores.color6[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70,width=3,fill=checkif(Colores.color6[1]))

                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color6[1]))
                canvas.create_line(565-desplazo,100,575-desplazo,100,width=5,fill=checkif(Colores.color6[1]))

                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color6[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color6[1]))

                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color6[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color6[1]))
        else:
            canvas.create_line(570-desplazo,120,570-desplazo,150-porte,width=3,fill=checkif(Colores.color6[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,120,600-desplazo,120-porte,width=3,fill=checkif(Colores.color6[1])) #linea arriba
            canvas.create_line(570-desplazo,150,600-desplazo,150-porte,width=3,fill=checkif(Colores.color6[1])) #linea del medio
            canvas.create_line(570-desplazo,150,570-desplazo,180-porte,width=3,fill=checkif(Colores.color6[1])) #linea izquiera abajo
            canvas.create_line(600-desplazo,150,600-desplazo,180-porte,width=3,fill=checkif(Colores.color6[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,180,600-desplazo,180-porte,width=3,fill=checkif(Colores.color6[1])) #linea abajo
    elif caracter=="7":
        if not esDenominador:
            canvas.create_line(570-desplazo,40+porte,600-desplazo,40+porte,width=3,fill=checkif(Colores.color7[1])) #linea arriba
            canvas.create_line(600-desplazo,40+porte,600-desplazo,70-porte,width=3,fill=checkif(Colores.color7[1])) #linea derecha arriba
            canvas.create_line(600-desplazo,70-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color7[1])) #linea derecha abajo
            if coordenadas=="ocultar coordenadas":
                #coordenadas
                canvas.create_line(565-desplazo,40,575-desplazo,40,width=5,fill=checkif(Colores.color7[1]))
                canvas.create_line(595-desplazo,40,605-desplazo,40,width=5,fill=checkif(Colores.color7[1]))

                canvas.create_line(595-desplazo,40,605-desplazo,40,width=5,fill=checkif(Colores.color7[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color7[1]))

                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color7[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color7[1]))

        else:
            canvas.create_line(570-desplazo,120,600-desplazo,120,width=3,fill=checkif(Colores.color7[1])) #linea arriba
            canvas.create_line(600-desplazo,120,600-desplazo,150,width=3,fill=checkif(Colores.color7[1])) #linea derecha arriba
            canvas.create_line(600-desplazo,150,600-desplazo,180,width=3,fill=checkif(Colores.color7[1])) #linea derecha abajo
    elif caracter=="8":
        if not esDenominador:
            canvas.create_line(570-desplazo,40+porte,570-desplazo,70-porte,width=3,fill=checkif(Colores.color8[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,40+porte,600-desplazo,40+porte,width=3,fill=checkif(Colores.color8[1])) #linea arriba
            canvas.create_line(600-desplazo,40+porte,600-desplazo,70-porte,width=3,fill=checkif(Colores.color8[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,70,600-desplazo,70,width=3,fill=checkif(Colores.color8[1])) #linea del medio
            canvas.create_line(570-desplazo,70-porte,570-desplazo,100-porte,width=3,fill=checkif(Colores.color8[1])) #linea izquiera abajo
            canvas.create_line(600-desplazo,70-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color8[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,100-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color8[1])) #linea abajo
            if coordenadas=="ocultar coordenadas":
                #coordenadas
                canvas.create_line(565-desplazo,40,575-desplazo,40,width=5,fill=checkif(Colores.color8[1]))
                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color8[1]))

                canvas.create_line(565-desplazo,40,575-desplazo,40,width=5,fill=checkif(Colores.color8[1]))
                canvas.create_line(595-desplazo,40,605-desplazo,40,width=5,fill=checkif(Colores.color8[1]))

                canvas.create_line(595-desplazo,40,605-desplazo,40,width=5,fill=checkif(Colores.color8[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color8[1]))

                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color8[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color8[1]))

                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color8[1]))
                canvas.create_line(565-desplazo,100,575-desplazo,100,width=5,fill=checkif(Colores.color8[1]))

                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color8[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color8[1]))

                canvas.create_line(565-desplazo,100,575-desplazo,100,width=5,fill=checkif(Colores.color8[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color8[1]))

        else:
            canvas.create_line(570-desplazo,120,570-desplazo,150,width=3,fill=checkif(Colores.color8[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,120,600-desplazo,120,width=3,fill=checkif(Colores.color8[1])) #linea arriba
            canvas.create_line(600-desplazo,120,600-desplazo,150,width=3,fill=checkif(Colores.color8[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,150,600-desplazo,150,width=3,fill=checkif(Colores.color8[1])) #linea del medio
            canvas.create_line(570-desplazo,150,570-desplazo,180,width=3,fill=checkif(Colores.color8[1])) #linea izquiera abajo
            canvas.create_line(600-desplazo,150,600-desplazo,180,width=3,fill=checkif(Colores.color8[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,180,600-desplazo,180,width=3,fill=checkif(Colores.color8[1])) #linea abajo
    elif caracter=="9":
        if not esDenominador:
            canvas.create_line(570-desplazo,40+porte,570-desplazo,70,width=3,fill=checkif(Colores.color9[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,40+porte,600-desplazo,40+porte,width=3,fill=checkif(Colores.color9[1])) #linea arriba
            canvas.create_line(600-desplazo,40+porte,600-desplazo,70-porte,width=3,fill=checkif(Colores.color9[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,70,600-desplazo,70,width=3,fill=checkif(Colores.color9[1])) #linea del medio
            canvas.create_line(600-desplazo,70-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color9[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,100-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color9[1])) #linea abajo
            if coordenadas=="ocultar coordenadas":
                #coordenadas
                canvas.create_line(565-desplazo,40,575-desplazo,40,width=5,fill=checkif(Colores.color9[1]))
                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color9[1]))

                canvas.create_line(565-desplazo,40,575-desplazo,40,width=5,fill=checkif(Colores.color9[1]))
                canvas.create_line(595-desplazo,40,605-desplazo,40,width=5,fill=checkif(Colores.color9[1]))

                canvas.create_line(595-desplazo,40,605-desplazo,40,width=5,fill=checkif(Colores.color9[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color9[1]))

                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color9[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color9[1]))

                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color9[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color9[1]))

                canvas.create_line(565-desplazo,100,575-desplazo,100,width=5,fill=checkif(Colores.color9[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color9[1]))
        else:
            canvas.create_line(570-desplazo,120,570-desplazo,150,width=3,fill=checkif(Colores.color9[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,120,600-desplazo,120,width=3,fill=checkif(Colores.color9[1])) #linea arriba
            canvas.create_line(600-desplazo,120,600-desplazo,150,width=3,fill=checkif(Colores.color9[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,150,600-desplazo,150,width=3,fill=checkif(Colores.color9[1])) #linea del medio
            canvas.create_line(600-desplazo,150,600-desplazo,180,width=3,fill=checkif(Colores.color9[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,180,600-desplazo,180,width=3,fill=checkif(Colores.color9[1])) #linea abajo
    elif caracter=="0":
        if not esDenominador:
            canvas.create_line(570-desplazo,40+porte,570-desplazo,70-porte,width=3,fill=checkif(Colores.color0[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,40+porte,600-desplazo,40+porte,width=3,fill=checkif(Colores.color0[1])) #linea arriba
            canvas.create_line(600-desplazo,40+porte,600-desplazo,70-porte,width=3,fill=checkif(Colores.color0[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,70-porte,570-desplazo,100-porte,width=3,fill=checkif(Colores.color0[1])) #linea izquiera abajo
            canvas.create_line(600-desplazo,70-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color0[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,100-porte,600-desplazo,100-porte,width=3,fill=checkif(Colores.color0[1])) #linea abajo
            if coordenadas=="ocultar coordenadas":
                #coordenadas
                canvas.create_line(565-desplazo,40,575-desplazo,40,width=5,fill=checkif(Colores.color0[1]))
                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color0[1]))

                canvas.create_line(565-desplazo,40,575-desplazo,40,width=5,fill=checkif(Colores.color0[1]))
                canvas.create_line(595-desplazo,40,605-desplazo,40,width=5,fill=checkif(Colores.color0[1]))

                canvas.create_line(595-desplazo,40,605-desplazo,40,width=5,fill=checkif(Colores.color0[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color0[1]))
                
                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.color0[1]))
                canvas.create_line(565-desplazo,100,575-desplazo,100,width=5,fill=checkif(Colores.color0[1]))

                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.color0[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color0[1]))

                canvas.create_line(565-desplazo,100,575-desplazo,100,width=5,fill=checkif(Colores.color0[1]))
                canvas.create_line(595-desplazo,100,605-desplazo,100,width=5,fill=checkif(Colores.color0[1]))
        else:
            canvas.create_line(570-desplazo,120,570-desplazo,150,width=3,fill=checkif(Colores.color0[1])) #linea izquiera arriba
            canvas.create_line(570-desplazo,120,600-desplazo,120,width=3,fill=checkif(Colores.color0[1])) #linea arriba
            canvas.create_line(600-desplazo,120,600-desplazo,150,width=3,fill=checkif(Colores.color0[1])) #linea derecha arriba
            canvas.create_line(570-desplazo,150,570-desplazo,180,width=3,fill=checkif(Colores.color0[1])) #linea izquiera abajo
            canvas.create_line(600-desplazo,150,600-desplazo,180,width=3,fill=checkif(Colores.color0[1])) #linea derecha abajo
            canvas.create_line(570-desplazo,180,600-desplazo,180,width=3,fill=checkif(Colores.color0[1])) #linea abajo
    elif caracter=="-":
        if not esDenominador:
            canvas.create_line(570-desplazo,80-porte,600-desplazo,80-porte,width=3,fill=checkif(Colores.colormenos[1])) #linea del medio
            if coordenadas=="ocultar coordenadas":
                #coordenadas
                canvas.create_line(565-desplazo,80,575-desplazo,80,width=5,fill=checkif(Colores.colormenos[1]))
                canvas.create_line(595-desplazo,80,605-desplazo,80,width=5,fill=checkif(Colores.colormenos[1]))
        else:
            canvas.create_line(570-desplazo,150,600-desplazo,150,width=3,fill=checkif(Colores.colormenos[1]))
    elif caracter=="+":
        if not esDenominador:
            canvas.create_line(585-desplazo,40+porte,585-desplazo,100-porte,width=3,fill=checkif(Colores.colormas[1])) #linea arriba medio
            canvas.create_line(570-desplazo,70,600-desplazo,70,width=3,fill=checkif(Colores.colormas[1])) #linea del medio
            if coordenadas=="ocultar coordenadas":
                #coordenadas
                canvas.create_line(580-desplazo,40,590-desplazo,40,width=5,fill=checkif(Colores.colormas[1]))
                canvas.create_line(580-desplazo,100,590-desplazo,100,width=5,fill=checkif(Colores.colormas[1]))

                canvas.create_line(565-desplazo,70,575-desplazo,70,width=5,fill=checkif(Colores.colormas[1]))
                canvas.create_line(595-desplazo,70,605-desplazo,70,width=5,fill=checkif(Colores.colormas[1]))
        else:
            canvas.create_line(585-desplazo,120,585-desplazo,180,width=3,fill=checkif(Colores.colormas[1])) #linea arriba medio
            canvas.create_line(570-desplazo,150,600-desplazo,150,width=3,fill=checkif(Colores.colormas[1]))
    elif caracter=="/":
        canvas.create_line(560-desplazo,110-porte,610-desplazo,110-porte,width=3,fill=checkif(Colores.colordiv[1])) #linea diagonal derecha
        if coordenadas=="ocultar coordenadas":
            #coordenadas
            canvas.create_line(555-desplazo,110,565-desplazo,110,width=5,fill=checkif(Colores.colordiv[1]))
            canvas.create_line(605-desplazo,110,615-desplazo,110,width=5,fill=checkif(Colores.colordiv[1]))

    elif caracter=="*":
        if not esDenominador:
            canvas.create_line(570-desplazo,50+porte//2,600-desplazo,80+porte//2,width=3,fill=checkif(Colores.colormul[1]))
            canvas.create_line(600-desplazo,50+porte//2,570-desplazo,80+porte//2,width=3,fill=checkif(Colores.colormul[1]))
            if coordenadas=="ocultar coordenadas":
                #coordenadas
                canvas.create_line(565-desplazo,50,575-desplazo,50,width=5,fill=checkif(Colores.colormul[1]))
                canvas.create_line(595-desplazo,80,605-desplazo,80,width=5,fill=checkif(Colores.colormul[1]))
                canvas.create_line(595-desplazo,50,605-desplazo,50,width=5,fill=checkif(Colores.colormul[1]))
                canvas.create_line(565-desplazo,80,575-desplazo,80,width=5,fill=checkif(Colores.colormul[1]))
                

        else:
            canvas.create_line(570-desplazo,130,600-desplazo,160,width=3,fill=checkif(Colores.colormul[1]))
            canvas.create_line(600-desplazo,130,570-desplazo,160,width=3,fill=checkif(Colores.colormul[1]))
    elif caracter==".":
        if not esDenominador:
            canvas.create_line(580-desplazo,100-porte,585-desplazo,100-porte,width=5,fill=checkif(Colores.colorpunt[1])) #linea izquiera arriba
        else:
            canvas.create_line(580-desplazo,180,585-desplazo,180,width=5,fill=checkif(Colores.colorpunt[1]))
    elif caracter=="(":
        canvas.create_line(590-desplazo,30,570-desplazo,70,590-desplazo,110,smooth="true",width=3,fill=checkif(Colores.colorpunt[1]))
    elif caracter==")":
        canvas.create_line(590-desplazo,30,610-desplazo,70,590-desplazo,110,smooth="true",width=3,fill=checkif(Colores.colorpunt[1]))
    elif caracter=="!":
        canvas.create_line(600-desplazo,40+porte,600-desplazo,85,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(597-desplazo,100,600-desplazo,100,width=5,fill=checkif(Colores.colorpunt[1]))
    elif caracter=="s":
        #N
        canvas.create_text(640-desplazo,0,text="")
        canvas.create_line(630-desplazo,60,630-desplazo,100,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(630-desplazo,100,610-desplazo,60,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(610-desplazo,60,610-desplazo,100,width=3,fill=checkif(Colores.colorpunt[1]))
        #i
        canvas.create_line(600-desplazo,100,600-desplazo,60,width=3,fill=checkif(Colores.colorpunt[1]))
        #s
        canvas.create_line(590-desplazo,60,570-desplazo,75,590-desplazo,90,570-desplazo,100,smooth="true",width=3,fill=checkif(Colores.colorpunt[1]))
    elif caracter=="c":
        #s
        canvas.create_line(635-desplazo,60,620-desplazo,75,640-desplazo,90,620-desplazo,100,smooth="true",width=3,fill=checkif(Colores.colorpunt[1]))
        #o
        canvas.create_line(610-desplazo,60,590-desplazo,80,610-desplazo,100,620-desplazo,80,610-desplazo,60,smooth="true",width=3,fill=checkif(Colores.colorpunt[1]))
        #c
        canvas.create_line(590-desplazo,61,570-desplazo,80,590-desplazo,99,smooth="true",width=3,fill=checkif(Colores.colorpunt[1]))
    elif caracter=="t":
        #N
        canvas.create_line(630-desplazo,60,630-desplazo,100,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(630-desplazo,100,610-desplazo,60,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(610-desplazo,60,610-desplazo,100,width=3,fill=checkif(Colores.colorpunt[1]))
        #a
        canvas.create_line(600-desplazo,60,610-desplazo,100,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(600-desplazo,60,590-desplazo,100,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(610-desplazo,80,590-desplazo,80,width=3,fill=checkif(Colores.colorpunt[1]))
        #t
        canvas.create_line(570-desplazo,60,590-desplazo,60,width=3,fill=checkif(Colores.colorpunt[1]))
        canvas.create_line(580-desplazo,60,580-desplazo,100,width=3,fill=checkif(Colores.colorpunt[1]))
    else:

        #canvas.create_text(180,50,text="No implementado aun")
        pass

def checkif(Cadena):
    if (len(Cadena)<=3):
        return "#000000"
    else:
        return Cadena