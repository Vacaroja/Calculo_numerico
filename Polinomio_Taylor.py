from DERIVADA import df
import math
""" 
f=funcion evaluada
a = valor de abajo de la integral
b= valor de arriba de la integral
n=numero de derivadas
xcero=valor inicio
"""

def polinomio_taylor(f, xcero, n):
    def w(x):
        I=1
        polinomio=f(xcero) #añade el primer polinomio
        while (I!=n+1): #itera hasta llegar al numero de derivadas deseadas
            if (I==1):
                derivada=df(f) #primera derivada
                polinomio+=derivada(xcero) * (x-xcero)
            else: # a partir de la segunda derivada
                derivada=df(derivada)
                
                polinomio += ( derivada(xcero) * (x-xcero)**I ) / math.factorial(I) 
            I+=1      
        return polinomio
    return w

def imprimir_polinomio(f,xcero,n,x):
    pol=polinomio_taylor(f,xcero,n)
    
    print("--------------------------------------POLINOMIO_TAYLOR--------------------------------------")
    print("el valor aproximado a traves del metodo del Polinomio de Taylor es:",pol(x))
    print("--------------------------------------------------------------------------------------------")
    return pol(x)
