public class algoritmosTarea2{
    
    //Implemetar estructura de tipo arbol
    public static void Arbol(){
        Arbol tree=new Arbol();
        Lista lista=new Lista();
        lista.agregar(0, "ACGT");
        tree.add("ACGT");
        
        //tree.add("CATG"); 
        tree.imprimirArbol(tree.getInicio());
    }

    
    public static void main(String[] args) {
       Arbol();
    }

}
/*
#implemetar una estructura de dato de tipo arbol de cadenas
#implementar una estructura de dato de tipo lista de enteros
#recibir la cadena larga introducida por el usuario en el documento, usar args para eso 
#ademas recibir el entero en args que dira la longitud de cada cadena
#leer los n primeros caracteres de la cadena y procesarlos en el arbol y guardar su posicion como 1
#leer los n primeros caracteres de la cadena despues del primer caracter y procearlos en el arbol y guarar su posicion como 2 etc...
#repetir hasta que ya no hayan suficientes datos en la cadena

*/
