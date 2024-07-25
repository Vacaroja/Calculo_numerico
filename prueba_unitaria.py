import unittest
from Biseccion import *
from NewtonRaphson import *
from Polinomio_taylor import *
from Riemann import *
from Trapecio import *



class test(unittest.TestCase):
	def test_biseccion(self):
		print("\n\n==========  METODO DE BISECCIÓN  ====================================")
		f1 = lambda x: math.exp(-x) - math.log(x)
		f2 = lambda x: pow((x-2),2) - math.log(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		f4 = lambda x: (x + 1)**0.5 - math.tan(x)
		self.assertEqual(imprimir_biseccion(f1,1,1.5,0.05,20),1.31005859375)
		self.assertEqual(imprimir_biseccion(f2,1,2,0.05,20),1.41259765625)
		self.assertEqual(imprimir_biseccion(f3,0,1,0.04,20),0.5885009765625)
		self.assertEqual(imprimir_biseccion(f4,0.5,1,0.01,20),0.94927978515625)
	def test_newton_raphson_method(self):
		print("\n\n==========  METODO DE NEWTHON RAPHSON  ===============================")
		f1 = lambda x: math.exp(x) - 2*x**2
		f2 = lambda x: pow((x-2),2) - math.log(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		self.assertEqual(imprimir_NR(f1,0.5,0.02,10),2.620530251267498)
		self.assertEqual(imprimir_NR(f3,0.5,0.02,10),0.5885547706231411)
	def test_polinomio_taylor(self):
		print("\n\n==========  POLINOMIO DE TAYLOR  =====================================")
		f1 = lambda x: math.exp(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		self.assertEqual(imprimir_polinomio(f1,1,0,5),2.718281828459045)
		self.assertEqual(imprimir_polinomio(f3,1,0,3),0.47359154363645417)
	def test_Rieman_method(self):
		print("\n\n==========  METODO DE RIEMAN  ========================================")
		f1 = lambda x: x / (x**2 + 1)
		f2 = lambda x: x * (x**2 + 1)**0.5
		self.assertEqual(imprimir_Riemann(f1,0,1,4),0.2788235294117647)
		self.assertEqual(imprimir_Riemann(f2,1,2,4),2.4116477770123668)
	def test_trapecio(self):
		print("\n\n==========  METODO DEL TRAPECIO  =====================================")
		f1 = lambda x: x*math.cos(x**2)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		self.assertEqual(imprimir_TRAPECIO(f1,0,1,4),0.2977516476987103)
		self.assertEqual(imprimir_TRAPECIO(f3,0,1,4),0.05260844566527276)


if __name__ == '__main__':
	unittest.main()