package tarea4;
public class NodoBinario
{
    private int num;
    private ArbolBinario Izq;
    private ArbolBinario Der;
    
    public NodoBinario(){
        this.num = 0;
        this.Der = null;
        this.Izq = null;
    }

    //---------------------------------------------------------------- Setters y getters -------------------------------------
    public int getNum(){
        return num;
    }

    public void setNum(int num){
        this.num = num;
    }

    public ArbolBinario getHijoIzq(){
        return Izq;
    }

    public void setHijoIzq(ArbolBinario Izq){
        this.Izq = Izq;
    }

    public ArbolBinario getHijoDer(){
        return Der;
    }

    public void setHijoDer(ArbolBinario Der){
        this.Der = Der;
    }
    //--------------------------------------------------------------------------------------------------------------------------------------
}