def is_num(c):
    return c.isnumeric()
def cambio(cadena):
    ## a lo que quiero llegar es a una cadena de la forma cadenax=["15","+","1","-","2"]
    # Necesito saber el indice donde empieza el numero y uno despues de donde termina
    cadena2=[]
    num=["0","1","2","3","4","5","6","7","8","9"]
    contador=0
    print(cadena)
    for j in range(0,10):
        contador=0
        for i in cadena:
            if i.isnumeric() :
                if contador>=1:
                    if cadena[contador-1].isnumeric():
                        cadena[contador-1:contador+1]= ["".join(cadena[contador-1:contador+1])]
            contador+=1
    print(cadena)
    #todos los numeros de la cadena están en una lista llamada cadena 2, todos los no numeros de la lista estan en una lista llamada cadena3
    for i in cadena:
        if(i.isnumeric()):
            cadena2+=format(int(i),"b")
        else:
            cadena2+=i
    print(cadena2)
    #for i in cadena3:
    
    #    print(i)

cadena=["1","5","+","1","-","2","2"]
cambio(cadena)