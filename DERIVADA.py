def df(f, h=0.03):#funcion para derivada
    def w(x):
        return (f(x+h)-f(x))/h #formula de la derivada
    return w