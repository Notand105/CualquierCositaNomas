public class Lista {
    
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
    public void agregar(int valor, String cadena){
        Node nuevo=new Node();

        nuevo.setValor(valor);
        nuevo.setCadena(cadena);
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
            int i=0;

            while(aux!=null){
                System.out.println(i+".[" + aux.getValor() +"]" +"-> ");
                aux=aux.getSiguiente();
                i++;
            }

        }
    }

}
