#interpolacion lineal e interpolacion polinomial
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = symbols('x')

z = np.array([1, 3, 6, 9, 11])
y = np.array([2, 4, 6, 8, 9])  

#z = np.array([-3, -1, 1, 2])
#y = np.array([6, 2, -1, 3]) 

N = len(z)  # Es el tamaño de la matriz
A = np.zeros((N, N)) # se inicializa en ceros las duplas


for i in range (N):
    A.T[i] = z**i
#print(A)  la matriz transpuesta 
#print(A, y)

#####################
a = np.linalg.solve(A, y)  # resuelve el sistema de ecuaciones A, y

#print(a)  # imprime las constantes  la ordenada del origen y el valor la pendiente

xTeorica = np.linspace(min(z), max(z), 40) # 40 datos azules 
# yTeorica = a[0] + a[1]*xTeorica + a[2]*xTeorica**2  # trabaja de forma estatica

yTeorica = 0

for i in range (N):
    yTeorica = yTeorica + a[i]*xTeorica**i

pxtabla = []
tramo = 1 
for tramo in range (1,N,1):
    numerador = y[tramo] -y[tramo-1]
    denominador = z[tramo] -z[tramo-1]
    m = numerador / denominador 
    pxtramo = y[tramo-1]
    pxtramo = pxtramo + m*(x-z[tramo-1])
    pxtabla.append(pxtramo)

b=1
print("Interpolacion lineal", "\n")
for tramo in range(1,N,1):
    pxtramo = pxtabla[tramo-1]
    print(b,"\t",pxtramo)    # imprime la ecuacion por cada tramo
    b +=1

plt.plot(z, y, 'ro') # se grafican los puntos del arreglo dado
plt.plot(xTeorica, yTeorica, 'b.') # datos interpolados
















# https://www.youtube.com/watch?v=LZ4KUvwIHn8

