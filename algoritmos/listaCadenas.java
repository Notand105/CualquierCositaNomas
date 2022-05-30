public class listaCadenas {
    
    private NodoCadenas inicio;
    private int size;
    

    public listaCadenas(){
        inicio=null;
        size=0;
    }


    public boolean esVacia(){
        return inicio==null;
    }

    public int getSize(){
        return size;
    }

//agragación de elementos a la lista
    public void agregar(int posicion,String cadena){
        NodoCadenas nuevo=new NodoCadenas();
        nuevo.setCadena(cadena);
        nuevo.setPosicion(posicion);

        if(esVacia()){
            inicio=nuevo;
        }
        else{
            NodoCadenas aux=inicio;

            while (aux.getSiguiente() != null){
                aux=aux.getSiguiente();
            }
            aux.setSiguiente(nuevo);
        }
        size++;
    }
    public void actualizar(int posicion,String cadena){
        //a la posición de la lista con aux.getcadena()= cadena agregarle posicion a su lista de posiciones
        
        if(buscar(cadena)){
            NodoCadenas aux=inicio;
            while(aux.getCadena().compareTo(cadena)!=0){
                aux=aux.getSiguiente();
            }
            aux.getLista().agregar(posicion);
        }
        
    }
    public boolean buscar(String cadena){
        NodoCadenas aux=inicio;
        boolean encontrado=false;
        while(aux!=null && encontrado!= true){
            if (cadena.compareTo(aux.getCadena())==0){
                encontrado=true;
            }
            else{
                aux=aux.getSiguiente();
            }
        }
        return encontrado;

    }

    public int encontrarMenor(){
        NodoCadenas aux=inicio;
        int menor=0;
        while(aux!=null){
            if(menor==0){
                menor=aux.getLista().getSize();
            }
            else{
                if(aux.getLista().getSize()< menor){
                    menor=aux.getLista().getSize();
                }
            }
            aux=aux.getSiguiente();
        }
        
        return menor;
        
    }
//imprimimos los elementos de la lista
    public void imprimirListaMenor(){
        if(!esVacia()){
            NodoCadenas aux=inicio;

            while(aux!=null){
                if(aux.getLista().getSize()==encontrarMenor()){
                    System.out.println("la cadena o cadenas con menos apariciones son "+aux.getCadena()+" en las posiciones: ");
                    aux.getLista().imprimirLista();
                }
                
                aux=aux.getSiguiente();
            }
            
            
        }
    }
}
