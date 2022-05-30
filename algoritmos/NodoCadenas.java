public class NodoCadenas {
    private String cadena;
    private Lista posiciones;
    private NodoCadenas siguiente;

    public NodoCadenas(){
        this.posiciones= new Lista();
        this.siguiente=null;
        this.cadena="";
    }

    public void setPosicion(int valor){
        this.posiciones.agregar(valor);
    }
    public void setSiguiente(NodoCadenas siguiente){
        this.siguiente=siguiente;
    }
    public void setCadena(String cadena){
        this.cadena=cadena;
    }

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
