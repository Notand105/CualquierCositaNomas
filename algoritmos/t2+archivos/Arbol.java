
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

    public void add(String cadena){
        if (this.inicio == null) {
            this.inicio = new nodoArbol (" ");
        }
        while(cadena.length()>0){
            insertar(cadena.substring(0, 1));
            cadena=cadena.substring(1);
        }    
    }

    public void insertar(String caracter){
        this.insertar(this.inicio, caracter);
        
    }

    private void insertar(nodoArbol padre, String valor){

        if (valor.compareTo("A")==0){
            if(padre.getA()==null){
                //System.out.println("se agrega A");
                padre.setA(new nodoArbol("A"));
                size+=1;
            }else{
                this.insertar(padre.getA(), "A");
            }
        }
        else if(valor.compareTo("C")==0){
            if(padre.getC()==null){
                //System.out.println("se agrega C");
                padre.setC(new nodoArbol("C"));
                size+=1;
            }else{
                this.insertar(padre.getC(), "C");
            }
        }
        else if(valor.compareTo("G")==0){
            if(padre.getG()==null){
               // System.out.println("se agrega G");
                padre.setG(new nodoArbol("G"));
                size+=1;
            }else{
                this.insertar(padre.getG(), "G");
            }
        }
        else if(valor.compareTo("T")==0){
            if(padre.getT()==null){
                //System.out.println("se agrega T");
                padre.setT(new nodoArbol("T"));
                size+=1;
            }else{
                this.insertar(padre.getT(), "T");
            }
        }
    }
    /*
    public void addListas(nodoArbol inicio){
        if (inicio==null){
            inicio.setLista();
        }
        addListas(inicio.getA());
        addListas(inicio.getC());
        addListas(inicio.getG());
        addListas(inicio.getT());

    }*/

    public void imprimirArbol(nodoArbol arbol){
        if (inicio==null){
            return;
        }
        System.out.println(arbol.getValor()+" ");
        if (arbol.getA()!=null){
            imprimirArbol(arbol.getA());
        }
        if (arbol.getC()!=null){
            imprimirArbol(arbol.getC());
        }
        if (arbol.getG()!=null){
            imprimirArbol(arbol.getG());
        }
        if (arbol.getT()!=null){
            imprimirArbol(arbol.getT());
        }
        
    }

}
