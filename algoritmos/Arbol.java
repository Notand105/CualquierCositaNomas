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
                size++;
                aux=inicio; 

                while (aux.getC() != null){
                    aux=aux.getC();
                }
                aux.setC(nuevo);
                size++;
                aux=inicio; 

                while (aux.getG() != null){
                    aux=aux.getG();
                }
                aux.setG(nuevo);
                size++;
                aux=inicio; 

                while (aux.getT() != null){
                    aux=aux.getT();
                }
                aux.setT(nuevo);
                size++;
            }
            
            valor--;
        }
    }

    public void imprimirArbol(nodoArbol arbol){
        if(!esVacio()){
            System.out.println(size);
            /*
            if (arbol != null) {
                imprimirArbol(arbol.getA());
                System.out.print(" " + arbol.getValor());
                
            }
            if (arbol != null) {
                imprimirArbol((arbol.getC()));
                System.out.print(" " + arbol.getValor());
                
            }
            if (arbol != null) {
                imprimirArbol((arbol.getG()));
                System.out.print(" " + arbol.getValor());
                
            }
            if (arbol != null) {
                imprimirArbol((arbol.getT()));
                System.out.print(" " + arbol.getValor());
                
            }
*/
        }
    }

}
