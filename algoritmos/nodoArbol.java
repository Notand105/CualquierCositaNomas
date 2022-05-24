public class nodoArbol {
 
    private int valor=0;
    private nodoArbol A;
    private nodoArbol C;
    private nodoArbol G;
    private nodoArbol T;

    public nodoArbol(){
        this.valor=0;
        this.A=null;
        this.C=null;
        this.G=null;
        this.T=null;
    }

    public void setValor(int valor){
        this.valor=valor;
    }
    public void setA(nodoArbol A){
        this.A=A;
    }
    public void setC(nodoArbol C){
        this.C=C;
    }
    public void setG(nodoArbol G){
        this.G=G;
    }
    public void setT(nodoArbol T){
        this.T=T;
    }

    public int getValor(){
        return valor;
    }
    public nodoArbol getA(){
        return A;
    }
    public nodoArbol getC(){
        return C;
    }
    public nodoArbol getG(){
        return G;
    }
    public nodoArbol getT(){
        return T;
    }


}
