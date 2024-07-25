"""
a = valor de abajo de la integral
b= valor de arriba de la integral
h= el valor de subida entre cada intervalo

"""

def Riemann(funcion,a,b,intervalo):
    area = 0
    h = (b - a) / intervalo
    
    for i in range(intervalo):
        area+=funcion(a+i*h) * h
    return area

def imprimir_Riemann(f,a,b,n):
    print("--------------------------------------RIEMANN--------------------------------------")
    print("el valor aproximado a traves del metodo de Riemman es:",Riemann(f,a,b,n))
    print("--------------------------------------------------------------------------------------------")
    return Riemann(f,a,b,n)
    
    
