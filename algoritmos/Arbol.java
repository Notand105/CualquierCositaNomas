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

    public void add(String valor){
        inicio=addRecursivo(inicio, valor);
    }

    private nodoArbol addRecursivo(nodoArbol actual ,String valor){

        //nodoArbol nuevo=new nodoArbol(valor);
        if (actual == null) {
            return new nodoArbol(valor);
        }
    
        if (valor =="A") {
            actual.setA(addRecursivo(actual.getA(), valor));
        } else if (valor=="C") {
            actual.setC(addRecursivo(actual.getC(), valor));
        }else if (valor=="G") {
            actual.setG(addRecursivo(actual.getG(), valor));
        }else if (valor=="T") {
            actual.setC(addRecursivo(actual.getC(), valor));
        }else{
            return actual;
        }
        return actual;
            /*
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
        }*/
    }

    public void imprimirArbol(nodoArbol arbol){
        if(!esVacio()){
            if (arbol != null) {
                imprimirArbol(arbol.getA());
                imprimirArbol(arbol.getC());
                imprimirArbol(arbol.getG());
                imprimirArbol(arbol.getT());
                System.out.print(" " + arbol.getValor());
            }

        }
    }

}
