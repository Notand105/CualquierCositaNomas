package tarea3;
import java.util.Random;
public class quicksort 
{
  public static void main(String[] args) 
  {
    //contadores de coomparaciones
	/*int compQuick1=0;
	int compQuick2=0;
	int compQuick3=0;
	int compQuick4=0;*/
	// arrelgo desordenado
	long inicio=0;
	long fin=0;
	double tiempo=0;
	int top=1000000;
    int[] array = new int[top]; //{ 12, 13, 24, 10, 3, 6, 90, 70,12,142,32,45,2,12,32,12,12,2323 };
	shuffle(array, top);
	//toma de tiempo
	
	System.out.print("QuickSort Normal : ");
	inicio = System.currentTimeMillis();
    quickSort( array, 0, array.length - 1 );
	fin = System.currentTimeMillis();
	
	tiempo = (double) ((fin - inicio));
    System.out.print(tiempo +" milisegundos");
	System.out.println();
	shuffle(array, top);
	System.out.print("QuickSort Mediana 2k+1 : ");
	inicio = System.currentTimeMillis();
    quickSort2k( array, 0, array.length - 1 );
	fin = System.currentTimeMillis();
	tiempo = (double) ((fin - inicio));
    System.out.print(tiempo +" milisegundos");
	System.out.println();
	shuffle(array, top);
	System.out.print("QuickSort + InsertSort : ");
	inicio = System.currentTimeMillis();
    quickSort_InsertSort( array, 0, array.length - 1 );
	fin = System.currentTimeMillis();
	tiempo = (double) ((fin - inicio));
    System.out.print(tiempo +" milisegundos");
	System.out.println();
	shuffle(array, top);
	System.out.print("QuickSort + InsertSort+mediana 2k+1 : ");
	inicio = System.currentTimeMillis();
    quickSort_Insert_mediana( array, 0, array.length - 1 );
	fin = System.currentTimeMillis();
	tiempo = (double) ((fin - inicio));
    System.out.print(tiempo +" milisegundos");
	System.out.println();
  }
 //------------------------------------------------------ Quicksort Normal ------------------------------------------------------------------------------
  public static void quickSort(int[] arr, int low, int high) 
  {
    //Ver si el arreglo está vacio
    if (arr == null || arr.length == 0){
      return;
    }
    if (low >= high){
      return;
    }
    //Obtener el pivote de la mitad del arreglo
    //int middle = low + (high - low) / 2;
	int middle=high; //quicksort normal usando el ultimo elemento como pivote
    int pivot = arr[middle];
 
    // Izquierda menor al pivote y derecha mayor al pivote
    int i = low, j = high;
    while (i <= j) 
    {
      //Todos los valores de la izquierda sean menor al pivote
      while (arr[i] < pivot) 
      {
        i++;
      }
      //Valores de la derecha mayores al pivote
      while (arr[j] > pivot) 
      {
        j--;
      }
      //Ver si los valores necesitan intercambiarse
      //Si lo nocesitan mover los iteradores
      if (i <= j) 
      {
        swap (arr, i, j);
        i++;
        j--;
      }
    }
    //Recursion para los subarreglos
    if (low < j){
      quickSort(arr, low, j);
    }
    if (high > i){
      quickSort(arr, i, high);
    }
  }
   
//------------------------------------------------------- Quicksort Mediana de 2k+1 ---------------------------------------------------------------------
public static void quickSort2k(int[] arr, int low, int high) 
{
  //Ver si el arreglo está vacio
  int pivot=0;
  int middle=0;
  if (arr == null || arr.length == 0){
	return;
  }
  if (low >= high){
	return;
  }
  //Obtener el pivote de la mediana de 2k+1
  int k=1; //declarar k 1=3, 2=5, 3=7, etc...
  if(high>=2*k+1){	
	int[] array2 = new int[2*k+1]; //crear un nuevo arreglo para obtener la mediana
	Random rand = new Random(); 	
	for(int c=0;c<=array2.length-1;c++){//lenar el nuevo arreglo con elementos al azar
		array2[c]=arr[rand.nextInt(high+1)]; 
	}
	insertionSort(array2, 0, array2.length-1); //ordenamos el arreglo nuevo
	middle = k; //el elemento del medio de nuestro nuevo arreglo es la mediana en este caso el elemento del medio es k
  	pivot = array2[middle];
  }
  else{
	middle = low + (high - low) / 2; // en caso que no se pueda aplicar mediana de 2k+1, funciona igual
  	pivot = arr[middle];
  }
  

  // Izquierda menor al pivote y derecha mayor al pivote
  int i = low, j = high;
  while (i <= j) 
  {
	//Todos los valores de la izquierda sean menor al pivote
	while (arr[i] < pivot) 
	{
	  i++;
	}
	//Valores de la derecha mayores al pivote
	while (arr[j] > pivot) 
	{
	  j--;
	}
	//Ver si los valores necesitan intercambiarse
	//Si lo nocesitan mover los iteradores
	if (i <= j) 
	{
	  swap (arr, i, j);
	  i++;
	  j--;
	}
  }
  //Recursion para los subarreglos
  if (low < j){
	quickSort(arr, low, j);
  }
  if (high > i){
	quickSort(arr, i, high);
  }
}

//------------------------------------------------------- Quicksort + insertSort -------------------------------------------------------------------------
public static void quickSort_Insert_mediana(int[] arr, int low, int high) 
  {
	int k=10; //k es el numero en el que los arreglos menores serán pasados por insertSort
	while (low < high) {
		if (high - low < k) {
			insertionSort(arr, low, high);
			break;
		}
		else {
			int pivot = partition2k(arr, low, high);
			if (pivot - low < pivot - high) {
				quickSort_InsertSort(arr, low, pivot - 1);
				low = pivot + 1;
			}
			else {
				quickSort_InsertSort(arr, pivot + 1, high);
				high = pivot - 1;
			}
		}
	}
	
	
	
  }
   
// ------------------------------------------------------ Quicksort + insertSort + Mediana de 2k+1--------------------------------------------------------
public static void quickSort_InsertSort(int[] arr, int low, int high) {
	int k=10; //k es el numero en el que los arreglos menores serán pasados por insertSort
	while (low < high) {
		if (high - low < k) {
			insertionSort(arr, low, high);
			break;
		}
		else {
			int pivot = partition(arr, low, high);
			if (pivot - low < pivot - high) {
				quickSort_InsertSort(arr, low, pivot - 1);
				low = pivot + 1;
			}
			else {
				quickSort_InsertSort(arr, pivot + 1, high);
				high = pivot - 1;
			}
		}
	}
	
	
  }

// ------------------------------------------------------ InsertSort -------------------------------------------------------------------------------------
	private static void insertionSort(int a[], int low,int high){
		for (int i = low + 1; i <= high; i++) {
			for (int j = i - 1; j >= low; j--) {
				if (a[j] > a[j + 1]) {
				// Swap
					int temp = a[j];
					a[j] = a[j + 1];
					a[j + 1] = temp;
				}
				else{
					break;
				}
			}
		}
	}
	public static int partition(int arr[], int low,int high){
        int pivot = arr[high];
        int i = low;
        int j = low;
 
        while (i <= high) {
            if (arr[i] > pivot)
                i++;
            else {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j++;
            }
        }
        return j - 1;
    }
	public static int partition2k(int arr[], int low,int high){
		int pivot=0;
		int middle=0;
		int k=1; //declarar k 1=3, 2=5, 3=7, etc...
  		if(high>=2*k+1){	
			int[] array2 = new int[2*k+1]; //crear un nuevo arreglo para obtener la mediana
			Random rand = new Random(); 	
			for(int c=0;c<=array2.length-1;c++){//lenar el nuevo arreglo con elementos al azar
			array2[c]=arr[rand.nextInt(high+1)]; 
			}
			insertionSort(array2, 0, array2.length-1); //ordenamos el arreglo nuevo
			middle = k; //el elemento del medio de nuestro nuevo arreglo es la mediana en este caso el elemento del medio es k
  			pivot = array2[middle];
  		}
  		else{
        	pivot = arr[high];
		}
        int i = low;
        int j = low;
 
        while (i <= high) {
            if (arr[i] > pivot)
                i++;
            else {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j++;
            }
        }
        return j - 1;
    }
  public static void swap (int array[], int x, int y)
    {
    int temp = array[x];
    array[x] = array[y];
    array[y] = temp;
    }

 
	public static void shuffle(int array[],int top){
		Random rands=new Random();
		for(int k=0;k<top;k++){
			array[k]=rands.nextInt(top);
		}
	}

	public static void printa(int arr[]){
		for(int k=0;k<=arr.length-1;k++){
			System.out.print(arr[k]+ " ");
		}
	}

}