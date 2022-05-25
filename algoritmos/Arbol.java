public class Arbol {
    
    private nodoArbol inicio;
    private int size;


    public Arbol(){
        inicio=null;
        size=0;
    }


    public boolean esVacio(){
        return inicio==null;
    }

    public int getSize(){
        return size;
    }

    public nodoArbol getInicio(){
        return inicio;
    }
    public void iniciar(int valor){

        nodoArbol nuevo=new nodoArbol();

        while (valor>0){
                nuevo.setValor(valor);
                nuevo.setA(null);
                nuevo.setC(null);
                nuevo.setG(null);
                nuevo.setT(null);
            
            
            if(esVacio()){
                inicio=nuevo;
            }
            else{

                nodoArbol aux=inicio;   

                while (aux.getA() != null){
                    aux=aux.getA();
                }
                aux.setA(nuevo);
                size=size+4;
                aux=inicio; 

                while (aux.getC() != null){
                    aux=aux.getC();
                }
                aux.setC(nuevo);
                size=size+4;
                aux=inicio; 

                while (aux.getG() != null){
                    aux=aux.getG();
                }
                aux.setG(nuevo);
                size=size+4;
                aux=inicio; 

                while (aux.getT() != null){
                    aux=aux.getT();
                }
                aux.setT(nuevo);
                size=size+4;
            }
            
            valor--;
        }
    }

    


    public void imprimirArbol(nodoArbol arbol){
        
            if (arbol != null) {
                System.out.println(size);
        }
    }

}
