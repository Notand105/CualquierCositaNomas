public class pruebaFunciones {


    public static void main(String[] args) {
        String cadena="holabuenastardes";
        System.out.println(cadena.length());
        
        while(cadena.length()>0){
            System.out.println(cadena.substring(0, 1));
            cadena=cadena.substring(1);

        }
    }
}
