
cadena="((15+3)+3)+(2+6)^2"

def toArray(cadena):
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
    return array

def Resultado(array):
    print(array)
    #array=ToInt(array)
    while("(" in array):
        array=cleanPar(array)
    print(array)
    array=ToInt(array)
    Operaciones(array)
    if(len(array)==1):
        return array[0]
    else :return array

def cleanPar(array):
    cont=0
    first=0
    last=0
    j=0
    r=0
    if("(" in array):
        #totalidad de los parentesis
        for i in array:
            if i=="(":
                cont=+1
                if(cont==1):first=j
            if i==")":
                cont-=1
                if(cont==0):last=j
            j+=1
        array[first]=str(cleanPar(array[first+1:last]))
        while(r<last-first):
            array.pop(first+1)
            r+=1
    else:
        return Resultado(array)
    return array

def ToInt(array):
    for i in array:
        if (array[array.index(i)].isnumeric() or is_Number(array[array.index(i)])):
            array[array.index(i)]=float(array[array.index(i)])
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

def is_Number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

cadena=toArray(cadena)
print(Resultado(cadena))