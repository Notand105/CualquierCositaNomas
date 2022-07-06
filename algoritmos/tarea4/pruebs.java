package tarea4;
public class pruebs {
    public static void main(String[] args) {
        int maximo=10;
        int[] inpares=new int[maximo];
        for (int i=0;i<inpares.length;i++){
            inpares[i]=2*(i+1)-1;
        }
        int[] pares=new int[maximo];
        for (int i=0;i<pares.length;i++){
            pares[i]=2*(i);
        }
        printa(inpares);
        printa(pares);

    }
    public static void printa(int[] array){
        for (int i=0;i<array.length;i++){
            System.out.println(array[i]);
        }
    } 

}
