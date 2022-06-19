public class Node {
    //nodos de la lista de enteros
    private int valor=0;
    private Node siguiente;

    public Node(){
        this.valor=0;
        this.siguiente=null;
    }

    public void setValor(int valor){
        this.valor=valor;
    }
    public void setSiguiente(Node siguiente){
        this.siguiente=siguiente;
    }

    public int getValor(){
        return valor;
    }
    public Node getSiguiente(){
        return siguiente;
    }

}
