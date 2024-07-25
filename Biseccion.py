"""
f=funcion evaluada
a = valor de abajo de la integral
b= valor de arriba de la integral
ni=numero de iteraciones
es=porcentaje de error maximo
M_pre= valor anterior
M_act= valor actual
"""



def biseccion(f,a,b,es,ni):
    Ea=100
    I=1
    M_act=0
    M_pre=0
    while((I<ni) and (Ea>es)):
        M_pre=M_act
        M_act=(a+b)/2
        if (f(M_act)*f(b))<0:
            a=M_act
        else:
            b=M_act
        
        if(I>1):
            Ea=abs((M_act - M_pre)/M_act)*100
        
        I+=1
        
    return M_act

def imprimir_biseccion(f,a,b,es,n):
    print("--------------------------------------BISECCION--------------------------------------")
    print("el valor aproximado a traves del metodo de Biseccion es:",biseccion(f,a,b,es,n))
    print("--------------------------------------------------------------------------------------------")
    return biseccion(f,a,b,es,n)
    
