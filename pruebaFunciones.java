import java.util.Scanner;

public class pruebaFunciones {


    public static void main(String[] args) {
        String cad="";
        String cadena="holabuenastardes";/*
        System.out.println(cadena.length());
        
        while(cadena.length()>0){
            System.out.println(cadena.substring( 1));
            cadena=cadena.substring(1);

        }*/
        Scanner sc=new Scanner(cadena);
        while(sc.hasNext()){
            cad=sc.next();
        }
    }
}
