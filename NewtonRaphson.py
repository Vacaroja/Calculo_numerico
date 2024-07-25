from DERIVADA import df

"""
f=funcion evaluada
x=valor de el intervalo
Ea=variable para guardar el valor del error actual para compararlo con porc_error
porc_err=porcentaje de error tope
n=numero maximo de veces que se puede repetir la funcion

"""
def newton_raphson(f, x, porc_err, n):
    Ea=porc_err+1     #hace que el porcentaje de error actual sea mayor al que se recibe 
    I=1         
    Xi=0    #define el valor inicial de Xi
    derivada=df(f) #definicion de la derivada de la funcion "f"
    while ( ( Ea > porc_err ) & ( n > I ) ):
        
        Xi = x - ( f(x) / derivada(x) )
        
        Ea= abs( ( Xi - x ) / Xi)
        
        x=Xi #lo iguala para que la siguiente iteracion tenga el valor siguiente 
        I+=1
    return Xi

def imprimir(f,a,b,n):
    print("--------------------------------------NEWTON-RAPHSON--------------------------------------")
    print("el valor aproximado a traves del metodo de Newton Raphson es:",newton_raphson(f,a,b,n))
    print("___________________________________________________________________________________")
    
    
