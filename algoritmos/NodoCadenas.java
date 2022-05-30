public class NodoCadenas {
    //nodos de las listas de cadenas
    private String cadena; //guarda la cadena 
    private Lista posiciones; //es una lista que guarda las posiciones de cada cadena
    private NodoCadenas siguiente;

    public NodoCadenas(){
        this.posiciones= new Lista();
        this.siguiente=null;
        this.cadena="";
    }
    //-----------------------------------setters-------------------------------------------------------

    public void setPosicion(int valor){
        this.posiciones.agregar(valor); //como tenemos una lista, para agregar hay que llamar a la funcion agregar de las listas
    }
    public void setSiguiente(NodoCadenas siguiente){
        this.siguiente=siguiente;
    }
    public void setCadena(String cadena){
        this.cadena=cadena;
    }

    //-----------------------------------getters--------------------------------------------------------

    public Lista getLista(){
        return posiciones;
    }

    public void getPosiciones(){
        posiciones.imprimirLista();
    }
    public String getCadena(){
        return cadena;
    }
    public NodoCadenas getSiguiente(){
        return siguiente;
    }
}
