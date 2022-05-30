public class Lista {
    //declaramos una lista de enteros
    private Node inicio;
    private int size;
    

    public Lista(){
        inicio=null;
        size=0;
    }


    public boolean esVacia(){
        return inicio==null;
    }

    public int getSize(){
        return size;
    }

//agragación de elementos a la lista, como tenemos que mostrar las posiciones solo agregamos al final
    public void agregar(int valor){
        Node nuevo=new Node();

        nuevo.setValor(valor);
        if(esVacia()){
            inicio=nuevo;
        }
        else{
            Node aux=inicio;

            while (aux.getSiguiente() != null){
                aux=aux.getSiguiente();
            }
            aux.setSiguiente(nuevo);
        }
        size++;
    }

//imprimimos los elementos de la lista

    public void imprimirLista(){
        if(!esVacia()){
            Node aux=inicio;
            while(aux!=null){
                System.out.print("[" + aux.getValor() +"]" +"-> ");
                aux=aux.getSiguiente();
            }
            System.out.println();

        }
    }

}
