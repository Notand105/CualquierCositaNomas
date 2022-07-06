package tarea4;
import java.io.IOException;
import java.util.Random;
public class Tarea4
{

    public static void main(String[] args) throws IOException
    {       
		long tiempoIni, tiempoFin;
		

        //creamos arbol binario normal    
		ArbolBinario arbol = new ArbolBinario();
        //creamos arbol binario con mediana de 3
		ArbolBinarioMediana arbolM3 = new ArbolBinarioMediana();//arbol binario con mediana de 3
			
		int num = Integer.parseInt(args[0]);//cantidad de numeros a agregar al arbol
        if(num<500000){
            num=500001;
        } //hace que el minimo de numeros a agregar sean 500.001
		
        int[] entrada = new int[num];// tendrá los n elementos a agregar
        //llena la entrada de elementos inapares entre 1 y 2*num
        for (int i=0;i<entrada.length;i++){
            entrada[i]=2*(i+1)-1;
        }

        Random rand = new Random();
		
        //desordenamos el arreglo de entrada para que no quede un arbol desbalanceado
		for (int i = 0; i < entrada.length; i++) {
			int randomIndexToSwap = rand.nextInt(entrada.length);
			int temp = entrada[randomIndexToSwap];
			entrada[randomIndexToSwap] = entrada[i];
			entrada[i] = temp;
		}

        //llenamos con numeros impares, entre 1 y 1 millon, 1 millon será siempre menor a 2*num por lo tanto todos estos existiran en la entrada
		int[] NumerosDentro = new int[500000];
        for (int i=0;i<NumerosDentro.length;i++){
            NumerosDentro[i]=2*(i+1)-1;
        }
        //llenamos con numeros pares entre 1 y 1 millon , al ser pares estos no existen en el arbol
        int[] NumerosFuera = new int[500000];
        for (int i=0;i<NumerosFuera.length;i++){
            NumerosFuera[i]=2*(i);
        }
        
        System.out.println("\n>>> Tiempo de insercion de "+num+ " llaves");

        tiempoIni = System.currentTimeMillis();
        for(int i = 0; i < entrada.length; i++)
        {
            arbol.insertar(entrada[i]);
        }
        tiempoFin = System.currentTimeMillis();

        System.out.println("ABB Normal: "+(tiempoFin-tiempoIni)+ "ms");


        tiempoIni = System.currentTimeMillis();
        for(int i = 0; i < entrada.length; i++)
        {
            arbolM3.insertar(entrada[i]);
        }
        tiempoFin = System.currentTimeMillis();

        System.out.println("ABB M3: "+(tiempoFin-tiempoIni)+ "ms");

        System.out.println("\n>>> Altura del arbol");

        System.out.println("ABB Normal: "+arbol.altura());
        System.out.println("ABB M3: "+arbolM3.altura());

        System.out.println("\n>>> Tiempo de busqueda de 500000 llaves que pertenecen al arbol");

        tiempoIni = System.currentTimeMillis();
        for(int i = 0; i<NumerosDentro.length; i++)
        {
            arbol.buscar(NumerosDentro[i]);
        }
        tiempoFin = System.currentTimeMillis();

        System.out.println("ABB Normal: "+(tiempoFin-tiempoIni)+ "ms");

        tiempoIni = System.currentTimeMillis();
        for(int i = 0; i<NumerosDentro.length; i++)
        {
            arbolM3.buscar(NumerosDentro[i]);
        }
        tiempoFin = System.currentTimeMillis();

        System.out.println("ABB M3: "+(tiempoFin-tiempoIni)+ "ms");			

        System.out.println("\n>>> Tiempo de busqueda de 500000 llaves que no pertenecen al arbol");

        tiempoIni = System.currentTimeMillis();
        for(int i = 0; i < NumerosFuera.length; i++)
        {
            arbol.buscar(NumerosFuera[i]);
        }
        tiempoFin = System.currentTimeMillis();

        System.out.println("ABB Normal: "+(tiempoFin-tiempoIni)+ "ms");

        tiempoIni = System.currentTimeMillis();
        for(int i = 0; i < NumerosFuera.length; i++)
        {
            arbolM3.buscar(NumerosFuera[i]);
        }
        tiempoFin = System.currentTimeMillis();

        System.out.println("ABB M3: "+(tiempoFin-tiempoIni)+ "ms");	
		
        System.out.println("\n>>> Tiempo de eliminacion de 500000 llaves que pertenecen al arbol");

        tiempoIni = System.currentTimeMillis();
        for(int i = 0; i < NumerosDentro.length; i++)
        {
            arbol.eliminar(NumerosDentro[i]);
        }
        tiempoFin = System.currentTimeMillis();

        System.out.println("ABB Normal: "+(tiempoFin-tiempoIni)+ "ms");

        tiempoIni = System.currentTimeMillis();
        for(int i = 0; i < NumerosDentro.length; i++)
        {
            arbolM3.eliminar(NumerosDentro[i]);
        }
        tiempoFin = System.currentTimeMillis();

        System.out.println("ABB M3: "+(tiempoFin-tiempoIni)+ "ms");			
		
    }
}