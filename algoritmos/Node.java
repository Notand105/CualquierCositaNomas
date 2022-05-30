public class Node {
    private int valor=0;
    private String cadena;
    private Node siguiente;

    public Node(){
        this.valor=0;
        this.siguiente=null;
        this.cadena="";
    }

    public void setValor(int valor){
        this.valor=valor;
    }
    public void setSiguiente(Node siguiente){
        this.siguiente=siguiente;
    }
    public void setCadena(String cadena){
        this.cadena=cadena;
    }

    public int getValor(){
        return valor;
    }
    public Node getSiguiente(){
        return siguiente;
    }
    public String getCadena(){
        return cadena;
    }

}
