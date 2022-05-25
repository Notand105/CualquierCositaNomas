public class nodoArbol {
 
    private String valor;
    private nodoArbol A;
    private nodoArbol C;
    private nodoArbol G;
    private nodoArbol T;

    public nodoArbol(String valor){
        this.valor=valor;
        this.A=null;
        this.C=null;
        this.G=null;
        this.T=null;
    }

    public void setValor(String valor){
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

    public String getValor(){
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
