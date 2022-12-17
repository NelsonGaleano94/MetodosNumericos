#  Lagrange

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt



cordenadaX = np.array([2,2.5,4,7])
cordenadaY = np.array([1/2,1/2.5,1/4,1/7])

# cordenadaX = np.array([2,67])
# cordenadaY = np.array([2*2-3,67*67-3])

poliExpandido=lambda x:x

def graficar():
    return 1




def polinomioInterpolaor():







 tamanoVector = len(cordenadaX) # tamaño del vector
 x = sym.Symbol('x')
 polinomio = 0


 for i in range(0,tamanoVector,1):
    
    # Termino de Lagrange
    primero =1
    segundo = 1
    for j  in range(0,tamanoVector,1):
        if (j!=i):
            primero = primero*(x-cordenadaX [j])
            segundo= segundo*(cordenadaX[i]-cordenadaX [j])
    terminoLi = primero/segundo

    polinomio = polinomio + terminoLi*cordenadaY[i]
 


 expancionPolinomica = polinomio.expand() # expanir el polinomio interpolante
 print('Polinomio de Lagrange: ')
 print( expancionPolinomica)

 poliExpandido = sym.lambdify(x,expancionPolinomica) # lambda funcion
 return poliExpandido 







#graficar y mostra valores


poliExpandido=polinomioInterpolaor()


a = np.min(cordenadaX)
b = np.max(cordenadaX)
x = np.linspace(a,b,100)





plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinomio de lagrange')


plt.plot(cordenadaX,cordenadaY,'o', label = 'Puntos')
plt.plot(x,poliExpandido(x), label = 'Polinomio',color="green")
plt.legend(loc=2)

valor=22   # aproximar valor en el poinomio
print("aproximar  f( ",valor,") = ",poliExpandido(valor))
plt.show()