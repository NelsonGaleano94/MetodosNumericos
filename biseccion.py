from math import ceil
import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
from sympy import lambdify
from sympy import sympify

"""

DEFINIMOS LA FUNCIÓN
    
"""

x= symbols('x') # definimos a X como una variable simbolica para ser ingresada en la función
funcion = sympify(input("Ingrese la función \n")) # definimos la función que vamos a utilizar
f = lambdify(x,funcion) # le decimos a python que la x ingresada en la función es nuestra variable simbolica

"""

INICIAMOS LAS VARIABLES

"""

a = float(input("Intervalo inicial: " )) # definimos el intervalo inical
b = float(input("Intervalo final: " )) # definimos el intervalo final
tolerancia = int(input("Nivel de tolerancia permitida, **Agregue solo el numero de exponente ** : " )) # definimos un nivel de tolerancia para nuestro calculo y a su vez criterio de parada
t= 10**-tolerancia
n = 0 # Numero de la iteración
error = 1 # Iniciamos el error
pn_1 = 0 # definimos nuestro X anterior
cantidadIteraciones = ceil((math.log((b-a)/t))/math.log(2))
print("\nEl número de iteraciones para la tolerancia ingresada será de: ",cantidadIteraciones)

"""

PROCEDIMIENTOS

"""

"""

ENCABEZADO DE NUESTRA TABLA

"""
    
print("\n\n{:^110}".format("METODO DE BISECCIÓN"))
print("{:^15}{:^14}{:^14}{:^15}{:^25}{:^25}{:^15}".format("n", "a", "b","pn","f(pn)","f(a)*f(pn)","error(%"))

### DEFINIMOS NUESTRA CRITERIO ###
if f(a) * f(b) < 0: ## gracias a la librería sympy nos permite evaluar la función directamente como variables simbolicas    
    pn = (a + b) / 2
    if pn == 0: ## Condición en caso de encontrar de manera inmediata el valor de la raíz
        error = 0
        print("{:^15}{:^15}{:^15}{:^15}{:^15}{:^15}".format(n,a,b,pn,f(pn),f(a)*f(pn),round(error*100),10))
        print("\nEl valor aproximado de x es: ", round(pn,10), "con un error de.: ", round(error * 100,15),"%\n")
        
        
        """
        
        GRAFICAR LA FUNCIÓN
        
        """
        
        puntosX = np.linspace(-10,10) ## Definimos los puntos a graficar en el eje x
        plt.plot(puntosX, f(puntosX))
        plt.title("GRAFICA DE LA FUNCIÓN / METODO BISECCIÓN")
        plt.axhline(color="black")
        plt.axvline(color="black")
        plt.scatter(pn, 0 , c="red")
        plt.annotate(round(pn,10), xy=(pn,0.5))
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True, which='both')
        plt.ylim([-15,15]) ## definimos los puntos a gráficar en el eje y
        plt.show()
    
   
    else:
        while error > t and n <= cantidadIteraciones: ## Condiciones de parada
            pn = (a + b) / 2
            error = abs((pn - pn_1)/pn)
            criterio = f(pn) * f(a) ## nuestro criterio de ubicación de la raíz
            
            if criterio< 0: ## debemos cambiar f(b) por f(pn) ya que la raiz se encuentra en el intervalo medio superior
                b = pn
                
            else:
                a = pn ## Condición en que la raíz se encuentre en el intervalo medio inferior
                
            pn_1 = pn ## Igualamos el valor actual de pn para luego utilizarlo en el calculo del error la siguiente iteración 
                
            
            """
            
            IMPRIMIMOS VALORES EN NUESTRA TABLA
            
            """
            print("{:^15}{:^14}{:^14}{:^15}{:^25}{:^25}{:^15}".format(n,a,b,pn,f(pn),criterio,round(error*100),10))
            n+=1
            
            
        """
        
        PRESENTACIÓN DE LOS CÁLCULOS
        
        """
        
        print("\nEl valor aproximado de x es: ", round(pn,10), "con un error de.: ", round(error * 100,15),"%")
        
        
        """
        
        GRAFICAR LA FUNCIÓN
        
        """
        
        puntosX = np.linspace(-10,10)
        plt.plot(puntosX, f(puntosX))
        plt.title("GRAFICA DE LA FUNCIÓN / METODO BISECCIÓN")
        plt.axhline(color="black")
        plt.axvline(color="black")
        plt.scatter(pn, 0 , c="red")
        plt.annotate(round(pn,10), xy=(pn,0.5))
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True, which='both')
        plt.ylim([-15,15])
        plt.show()
    
else: # COndicion f(a)*f(b) >= 0
    print("\nLa función no contiene raices en el intervalo de " + "x = "+ str(a)+" a x = "+ str(b))
    
    puntosX = np.linspace(-10,10)
    plt.plot(puntosX, f(puntosX))
    plt.title("GRAFICA DE LA FUNCIÓN")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.ylim([-15,15])
    plt.show()
    