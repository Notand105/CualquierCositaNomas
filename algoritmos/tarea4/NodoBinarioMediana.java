package tarea4;
public class NodoBinarioMediana {
    
        private int valorIzq;
        private int valorMed;
        private int valorDer;
        
        private ArbolBinarioMediana Izq;
        private ArbolBinarioMediana Der;
        
        private int cantidad;
        private boolean esHoja;
        
        public NodoBinarioMediana(){
            this.valorIzq = -1;
            this.valorMed = -1;
            this.valorDer = -1;
            
            this.Der = null;
            this.Izq = null;
            
            this.cantidad = 0;
            this.esHoja = true;
        }
    
        public int getValorIzq(){
            return valorIzq;
        }
    
        public void setValorIzq(int valorIzq){
            this.valorIzq = valorIzq;
        }
    
        public int getValorMed(){
            return valorMed;
        }
    
        public void setValorMed(int valorMed){
            this.valorMed = valorMed;
        }
    
        public int getValorDer(){
            return valorDer;
        }
    
        public void setValorDer(int valorDer){
            this.valorDer = valorDer;
        }
    
        public ArbolBinarioMediana getHijoIzq(){
            return Izq;
        }
    
        public void setHijoIzq(ArbolBinarioMediana Izq){
            this.Izq = Izq;
        }
    
        public ArbolBinarioMediana getHijoDer(){
            return Der;
        }
    
        public void setHijoDer(ArbolBinarioMediana Der){
            this.Der = Der;
        }
    
        public int getCantidad(){
            return cantidad;
        }
    
        public void setCantidad(int cantidad){
            this.cantidad = cantidad;
        }    
    
        public boolean esHoja(){
            return esHoja;
        }
    
        public void setEsHoja(boolean esHoja){
            this.esHoja = esHoja;
        }

        //----------------------------------------------------------------------------------------------------------------------
}
