package tarea4;
import java.util.ArrayList;
public class ArbolBinarioMediana {
    private NodoBinarioMediana raiz;
    
    public boolean estaVacio(){
        return (raiz == null);
    }
    
    public void insertar(int x)
    {
        if(estaVacio())
        {
            NodoBinarioMediana nuevo = new NodoBinarioMediana();
            nuevo.setValorMed(x);
            nuevo.setHijoDer(new ArbolBinarioMediana());
            nuevo.setHijoIzq(new ArbolBinarioMediana());
            nuevo.setCantidad(1);
            this.raiz = nuevo;
        }
        //se puede insertar
        else if(this.raiz.esHoja()){
            //se puede insertar directamente
            if(this.raiz.getCantidad() < 3){
                //si es menor al valor del medio
                if(x < this.raiz.getValorMed()){
                    //si no hay, se inserta directamente
                    if(this.raiz.getValorIzq() == -1){
                        this.raiz.setValorIzq(x);
                        this.raiz.setCantidad(this.raiz.getCantidad()+1);
                    }
                    //si no esta vacio el valor de la izquierda
                    else{
                        //menor al medio y al izquierdo
                        if(x < this.raiz.getValorIzq()){
                            this.raiz.setValorDer(this.raiz.getValorMed());
                            this.raiz.setValorMed(this.raiz.getValorIzq());
                            this.raiz.setValorIzq(x);
                            this.raiz.setCantidad(this.raiz.getCantidad()+1);
                        }
                        //menor al medio y mayor al izquierdo, es decir entre la llave de la izquierda y la del medio
                        else if(x > this.raiz.getValorIzq())//menor al medio y mayor al izquierdo
                        {
                            this.raiz.setValorDer(this.raiz.getValorMed());
                            this.raiz.setValorMed(x);
                            this.raiz.setCantidad(this.raiz.getCantidad()+1);
                        }
                    }
                }
                //mayor al del medio
                else if(x > this.raiz.getValorMed()){
                    //se inserta directamente si el derecho es vacio
                    if(this.raiz.getValorDer() == -1){
                        this.raiz.setValorDer(x);
                        this.raiz.setCantidad(this.raiz.getCantidad()+1);
                    }
                    //si no esta vacio el valor derecho
                    else{
                        //si es mayor al medio y al valor derecho
                        if(x > this.raiz.getValorDer()){
                            this.raiz.setValorIzq(this.raiz.getValorMed());
                            this.raiz.setValorMed(this.raiz.getValorDer());
                            this.raiz.setValorDer(x);
                            this.raiz.setCantidad(this.raiz.getCantidad()+1);
                        }
                        //mayor al medio pero menor al derecho
                        else if(x < this.raiz.getValorDer()){
                            this.raiz.setValorIzq(this.raiz.getValorMed());
                            this.raiz.setValorMed(x);
                            this.raiz.setCantidad(this.raiz.getCantidad()+1);
                        }
                    }
                }
            }
            //se realiza el split y luego se inserta en la hoja correspondiente
            else{
                //Ahora es una rama
                this.raiz.setEsHoja(false);
                this.raiz.getHijoDer().insertar(this.raiz.getValorDer());
                this.raiz.getHijoIzq().insertar(this.raiz.getValorIzq());
                this.raiz.setCantidad(1);
                this.raiz.setValorIzq(-1);
                this.raiz.setValorDer(-1);
                
                //se inserta por la izquierda
                if(x < this.raiz.getValorMed()){
                    this.raiz.getHijoIzq().insertar(x);
                }
                //se inserta por la derecha
                else if(x > this.raiz.getValorMed()){
                    this.raiz.getHijoDer().insertar(x);
                }               
            }
        }
        else//no puedo insertar
        {
            if(x < this.raiz.getValorMed())//se inserta por la izquierda
            {
                this.raiz.getHijoIzq().insertar(x);
            }
            else if(x > this.raiz.getValorMed())//se inserta por la derecha
            {
                this.raiz.getHijoDer().insertar(x);
            }
        }
    }
    
    public ArbolBinarioMediana buscar(int x)
    {
        ArbolBinarioMediana arbol = null;
        
        if (!estaVacio() && x != -1) { 
            if(x == this.raiz.getValorIzq() || x == this.raiz.getValorMed() || x == this.raiz.getValorDer()){ //busca el valor dentre de la raiz
                return this;
            }
            else if(x < this.raiz.getValorMed()){ //se mueve a buscarlo al hizo izquierdo si es menor
                arbol = this.raiz.getHijoIzq().buscar(x);
            }
            else if(x > this.raiz.getValorDer()){ //se mueve a buscarlo al hijo derecho si es mayor
                arbol = this.raiz.getHijoDer().buscar(x);
            }	
        }
        return arbol;
    }    

    public int buscarMayorMenores()
    {
        ArbolBinarioMediana actual = this.raiz.getHijoIzq();//Se obtiene el sub arbol de los pequeños
        //Moverse lo mas a la derecha posible
        while(!actual.raiz.getHijoDer().estaVacio()){
            actual = actual.raiz.getHijoDer();
        }
        int devuelvo = -1;
        
        if(actual.raiz.esHoja()){
            //Queda solo una llave en esta hoja
            if(actual.raiz.getCantidad() == 1) {
                devuelvo = actual.raiz.getValorMed();
                actual.raiz = null;
            }
            //quedan dos llaves
            else if(actual.raiz.getCantidad() == 2) {
                devuelvo = actual.raiz.getValorMed();
                actual.raiz.setValorMed(actual.raiz.getValorIzq());
                actual.raiz.setValorIzq(-1);
            }
            //quedan 3 llaves
            else {
                devuelvo = actual.raiz.getValorDer();
                actual.raiz.setValorDer(-1);
            }
        }
        //es un nodo interno sin hijo derecho
        else {
            devuelvo = actual.raiz.getValorMed();
            if(actual.raiz.getHijoIzq().raiz.getCantidad() == 1) //sólo queda una llave en esa hoja
            {
                actual.raiz.setValorMed(actual.raiz.getHijoIzq().raiz.getValorMed());
                actual.raiz.getHijoIzq().raiz = null;
                actual.raiz.setEsHoja(true); //pasa de nodo interno a hoja.
            }
            else if(actual.raiz.getHijoIzq().raiz.getCantidad() == 2) //dos llaves
            {
                //el valor del medio pasa como nodo interno
                actual.raiz.setValorMed(actual.raiz.getHijoIzq().raiz.getValorMed());
                
                //el valor de la izquieda pasa al medio
                actual.raiz.getHijoIzq().raiz.setValorMed(actual.raiz.getHijoIzq().raiz.getValorIzq());
                
                //el valor de la izquierda queda vacio.
                actual.raiz.getHijoIzq().raiz.setValorIzq(-1);
            }
            else //3 llaves
            {
                //el valor de la derecha pasa como nodo interno
                actual.raiz.setValorMed(actual.raiz.getHijoIzq().raiz.getValorDer());
                
                //dejamos el valor de la derecha como vacio
                actual.raiz.getHijoIzq().raiz.setValorDer(-1);
            }
        }
        return devuelvo;         
    }
    
   public void eliminar(int x) 
    {
        ArbolBinarioMediana paraEliminar = buscar(x);
		
        if(paraEliminar != null) 
        {
            if (paraEliminar.raiz.esHoja())//si la llave esta en una hoja
            {
                if(paraEliminar.raiz.getValorIzq() == x)//si la llave esta a la izquierda
                {
                    paraEliminar.raiz.setValorIzq(-1);
                }
                else if(paraEliminar.raiz.getValorDer() == x)//si la llave esta a la derecha
                {
                    paraEliminar.raiz.setValorDer(-1);
                }
                else if(paraEliminar.raiz.getValorMed() == x)//si la llave esta al medio
                {
                    paraEliminar.raiz.setValorMed(-1);
                    
                    //no podemos dejar el nodo sin valor del medio.
                    
                    if(paraEliminar.raiz.getValorDer() != -1)//movemos el valor de la derecha, si existe, al centro
                    {
                        paraEliminar.raiz.setValorMed(paraEliminar.raiz.getValorDer());
                        paraEliminar.raiz.setValorDer(-1);
                    }
                    else if(paraEliminar.raiz.getValorIzq() != -1)//movemos el valor de la izquierda, si existe, al centro
                    {
                        paraEliminar.raiz.setValorMed(paraEliminar.raiz.getValorIzq());
                        paraEliminar.raiz.setValorIzq(-1);                        
                    }
                    else//no existe valor de derecha, ni izquierda. Borrar el nodo completo
                    {
                        paraEliminar.raiz = null;
                    }
                }
				if(paraEliminar.raiz != null)
				{
					paraEliminar.raiz.setCantidad(paraEliminar.raiz.getCantidad()-1);
				}
            }	
            else//la llave esta en una rama (nodo interno)
            {
				if(paraEliminar.raiz.getHijoIzq().raiz == null && raiz.getHijoDer().raiz == null)
				{
					paraEliminar.raiz = null;
				}
                //suma de llaves de subarboles menores o iguales a 3, los compactamos en una hoja.
				
				int suma = 0;
				boolean hayHi = false;
				boolean hayHd = false;
				if(paraEliminar.raiz.getHijoIzq().raiz != null)
				{
					suma = suma+paraEliminar.raiz.getHijoIzq().raiz.getCantidad();
					hayHi = true;
				}
				if(paraEliminar.raiz.getHijoDer().raiz != null)
				{
					suma = suma+paraEliminar.raiz.getHijoDer().raiz.getCantidad();
					hayHd = true;
				}
				
                else if(suma <= 3)
                {
                    //como son sólo 3 llaves, las guardamos y si guardamos desde el hijo izquierdo
                    //con menor valor, hasta el hijo derecho con mayor valor. Nos quedarán ordenadas
                    
                    NodoBinarioMediana hi = null;
					NodoBinarioMediana hd = null;
					if(paraEliminar.raiz.getHijoIzq().raiz != null && paraEliminar.raiz.getHijoIzq().raiz.esHoja())
					{
						hi = paraEliminar.raiz.getHijoIzq().raiz;
					}
                    else if (paraEliminar.raiz.getHijoDer().raiz != null && paraEliminar.raiz.getHijoDer().raiz.esHoja())
					{
						hd = paraEliminar.raiz.getHijoDer().raiz;
					}

                    ArrayList<Integer> numeros = new ArrayList<Integer>();
                    
					if(hi != null)
					{
						if(hi.getValorIzq() != -1){
							numeros.add(hi.getValorIzq());
						}
						if(hi.getValorMed() != -1){
							numeros.add(hi.getValorMed());
						}
						if(hi.getValorDer() != -1){
							numeros.add(hi.getValorDer());
						}
					}
					if(hd != null)
					{
						if(hd.getValorIzq() != -1)
						{
							numeros.add(hd.getValorIzq());
						}
						if(hd.getValorMed() != -1)
						{
							numeros.add(hd.getValorMed());
						}
						if(hd.getValorDer() != -1)
						{
							numeros.add(hd.getValorDer());
						}
					}
                    if(numeros.size() > 0)
					{
						if(numeros.size() == 1)
						{
							paraEliminar.raiz.setValorMed(numeros.get(0));
						}
						else if(numeros.size() == 2)
						{
							paraEliminar.raiz.setValorIzq(numeros.get(0));
							paraEliminar.raiz.setValorMed(numeros.get(1));
						}
						else
						{
							paraEliminar.raiz.setValorIzq(numeros.get(0));
							paraEliminar.raiz.setValorMed(numeros.get(1));
							paraEliminar.raiz.setValorDer(numeros.get(2));
						}
						paraEliminar.raiz.setEsHoja(true); //pasa a ser hoja
						//dejamos los hijos vacíos.
						paraEliminar.raiz.getHijoDer().raiz = null;
						paraEliminar.raiz.getHijoIzq().raiz = null;
					}
                }
                //hay mas de 3 llaves, buscar al mas grande de los chicos y reemplazar
                else 
                {
                    paraEliminar.raiz.setValorMed(this.buscarMayorMenores());
                }
            }
        }
    }      
    
    public int altura() 
    {
        if (estaVacio()) 
        {
            return 0;
        }
        else 
        {
            return (1 + Math.max(((raiz.getHijoIzq()).altura()), ((raiz.getHijoDer()).altura())));
        }
    }     
        
}
