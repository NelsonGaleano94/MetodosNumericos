import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd
import math
p = math.pi

columnas = ["Iteracion", "Xi", "F(Xi)", "F'(Xi)", "Xi+1", "Error"]
datos = [[0,0,0,0,1,0]]
tabla = pd.DataFrame(datos, columns=columnas)

x = sp.symbols("x")
f = input("Introduzca la funcion ")   #   x**3 - cos(x)
df = sp.diff(f) #  funcion a derivar
f = sp.lambdify(x, f)
df = sp.lambdify(x, df)

x0 = 1
i = 1
error = 10

while error >  1e-6:  # error sera de 6 cifras siginificativas
    x1 = x0 - f(x0) / df(x0)
    error = abs(x1-x0)/x1
    
    # tabla = tabla.append({    # crear una tabla pero da error
    #     "Iteracion":i,
    #     "Xi":x0,
    #     "F(Xi)":f(x0),
    #     "F'(Xi)":df(x0),
    #     "Xi+1":x1,
    #     "Error":error
    #     },ignore_index=True)
    
    x0 = x1
    print("Iteracion ",i, ", raiz aproximada : ", x0)
    i = 1 + i


print("El error es : ", error) 
print("La Raiz es : ",x1)   

plt.title("Metodo de Newton Raphson")
x = np.linspace(-2, 2, 100)
plt.plot(x, f(x))
plt.plot(x0, f(x0), 'ro')
plt.grid()
plt.show()


