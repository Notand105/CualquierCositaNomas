
cadena="3^9+10/2-15+43*32+6^2"

def PartirPor(string, separators):
        lis = []
        current = ""
        for ch in string:
            if ch in separators:
                lis.append(current)
                lis.append(ch)
                current = ""
            else:
                current += ch
        lis.append(current)
        return lis

def Resultado(cadena):
    array=[]
    for i in cadena:
        array.append(i)
    contador=0
    for j in range(0,10):
        contador=0
        for i in array:
            if i.isnumeric() :
                if contador>=1:
                    if array[contador-1].isnumeric():
                        array[contador-1:contador+1]= ["".join(array[contador-1:contador+1])]
            contador+=1
    print()
    Operaciones(ToInt(array))
    print(array)

def ToInt(array):
    for i in array:
        if (array[array.index(i)].isnumeric()):
            array[array.index(i)]=int(array[array.index(i)])
    return array

def Operaciones(array):
    print(array)
    if(len(array)==1):
        return
    
    while ("^" in array):
        aux=array.index("^")
        array[aux-1]=array[aux-1]**array[aux+1]
        array.pop(aux)
        array.pop(aux)
        print(array)
    while ("*" in array or "/" in array):
        if("*" in array and "/" in array):
            if(array.index("*") < array.index("/")):
                aux=array.index("*")          
                array[aux-1]=array[aux-1]*array[aux+1]
                array.pop(aux)
                array.pop(aux)
            else:
                aux=array.index("/")
                array[aux-1]=array[aux-1]/array[aux+1]
                array.pop(aux)
                array.pop(aux)
        else:
            if("*" in array):
                aux=array.index("*")          
                array[aux-1]=array[aux-1]*array[aux+1]
                array.pop(aux)
                array.pop(aux)
            elif("/" in array):
                aux=array.index("/")
                array[aux-1]=array[aux-1]/array[aux+1]
                array.pop(aux)
                array.pop(aux)
        print(array)
    while("+" in array or "-" in array):
        if("+" in array and "-" in array):
                    if(array.index("+") < array.index("-")):
                        aux=array.index("+")          
                        array[aux-1]=array[aux-1]+array[aux+1]
                        array.pop(aux)
                        array.pop(aux)
                    else:
                        aux=array.index("-")
                        array[aux-1]=array[aux-1]-array[aux+1]
                        array.pop(aux)
                        array.pop(aux)
        else:
                    if("+" in array):
                        aux=array.index("+")          
                        array[aux-1]=array[aux-1]+array[aux+1]
                        array.pop(aux)
                        array.pop(aux)
                    elif("-" in array):
                        aux=array.index("-")
                        array[aux-1]=array[aux-1]-array[aux+1]
                        array.pop(aux)
                        array.pop(aux)
                
        print(array) 



Resultado(cadena)