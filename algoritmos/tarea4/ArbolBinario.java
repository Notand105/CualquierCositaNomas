package tarea4;

public class ArbolBinario {
    
    private NodoBinario raiz;
        
    public boolean estaVacio(){
        return (this.raiz == null);
    }
    
    public void insertar(int x){
        if(estaVacio()){
            NodoBinario nuevo = new NodoBinario();
            nuevo.setNum(x);
            nuevo.setHijoDer(new ArbolBinario());
            nuevo.setHijoIzq(new ArbolBinario());
            this.raiz = nuevo;
        }
        else if(x > this.raiz.getNum()){
            this.raiz.getHijoDer().insertar(x);
        }
        else if(x < this.raiz.getNum()){
            this.raiz.getHijoIzq().insertar(x);
        }        
    }
    
    public ArbolBinario buscar(int x){
        ArbolBinario arbol = null;
        
        if (!estaVacio()) {
            if (x == this.raiz.getNum()) {
                return this;
            }
            else if (x < this.raiz.getNum()) {
                arbol = this.raiz.getHijoIzq().buscar(x);
            }
            else if (x > this.raiz.getNum()){
                arbol = this.raiz.getHijoDer().buscar(x);
            }		
        }
        return arbol;
    }
    
    public int altura() {
        if (estaVacio()) {
            return 0;
        }
        else {
            return (1 + Math.max(((raiz.getHijoIzq()).altura()), ((raiz.getHijoDer()).altura())));
        }
    }     
    
    public boolean esHoja() { 
        boolean hoja = false; 
        if((raiz.getHijoIzq()).estaVacio() && (raiz.getHijoDer()).estaVacio()) { 
            hoja = true; 
        } 
        return hoja; 
    }    
    
    public int buscarMin() {
        ArbolBinario arbolActual = this; 
        while(!arbolActual.raiz.getHijoIzq().estaVacio()) { 
            arbolActual = arbolActual.raiz.getHijoIzq(); 
        } 
        int devuelvo= arbolActual.raiz.getNum();
        arbolActual.raiz = null;
        return devuelvo; 
    }    
    
    public void eliminar(int x) {
        ArbolBinario paraEliminar = buscar(x);
        if (paraEliminar != null && !paraEliminar.estaVacio()) {
            if (paraEliminar.esHoja()) {
                paraEliminar.raiz = null;
            }	
            else {
                if (!paraEliminar.raiz.getHijoIzq().estaVacio() && !paraEliminar.raiz.getHijoDer().estaVacio()) {
                    paraEliminar.raiz.setNum(paraEliminar.raiz.getHijoDer().buscarMin());
                }
                else if (paraEliminar.raiz.getHijoIzq().estaVacio()) {
                    paraEliminar.raiz = paraEliminar.raiz.getHijoDer().raiz;
                }
                else{
                    paraEliminar.raiz = paraEliminar.raiz.getHijoIzq().raiz;
                }
            }
        }
    }    
        
    public NodoBinario getRaiz()
    {
        return this.raiz;
    }
}
