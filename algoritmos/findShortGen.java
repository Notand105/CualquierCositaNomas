import java.io.File;
import java.util.Scanner;

public class findShortGen{

    
    public static void Ejecucion(int largo, Scanner datos){
        listaCadenas lista=new listaCadenas();
        //hacemos que nuestro string cadena contenga la informacion del scanner
        String cadena=datos.next();
        String cadenaAgregar;
        int posicion=0;
        //mientras la cadena sea lo suficientemente grande como para ser evaluada se continua la operación
        System.out.println("El programa esta siendo ejecutado, por favor espera un momento...");
        System.out.println();
        while (cadena.length()>=largo){
            cadenaAgregar=cadena.substring(0, largo);
            if(lista.buscar(cadenaAgregar)){
                lista.actualizar(posicion, cadenaAgregar);
            }
            else{
                lista.agregar(posicion, cadenaAgregar);
            }
            cadena=cadena.substring(1);
            posicion+=1;
        }
        lista.imprimirListaMenor();
    }

    
    public static void main(String[] args) throws Exception {
        //El primer argumento es el largo de las cadenas
       int LargoCadena=Integer.parseInt( args[0]);
       //El segundo argumento es el archivo del cual se leera la información
       String archivo=args[1];
       File doc=new File(archivo);
       Scanner sc= new Scanner(doc);
       //pasamos los datos a la función de ejecucion del programa
       Ejecucion(LargoCadena,sc);
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
