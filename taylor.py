from math import *
import sympy as sp
from sympy.plotting import plot

def Taylor():
    x=sp.symbols('x')
    funcion = sp.sympify(input("Ingrese la función \n")) # definimos la función que vamos a utilizar
    punto= input('Digite alrededor de cual punto desea el polinomio ')
    if(punto=='pi'):
        div=float(input('inserte dividendo\n'))
        punto=pi/div
    grado= int(input('Digite el orden del polinomio de Taylor '))
    funcionGrafica=funcion
    Taylor=funcion.subs(x,punto)
    
    for k in range(1,grado+1):  
        derivadaK=sp.diff(funcion,x)
        Taylor=Taylor+derivadaK.subs(x,punto)*((x-punto)**k)/factorial(k)
        funcion=derivadaK
        
    print(sp.expand(Taylor))
    
    plot(funcionGrafica,Taylor,(x,punto-4,punto+4),title='Polinomio de Taylor')
    derivadaK=sp.diff(funcion,x)
    
    

if __name__ == '__main__':

    Taylor()
