import matplotlib.pyplot as plt



# Algoritmo de punto fijo
# [a,b] intervalo de búsqueda
# error = tolera

import numpy as np

def puntofijo(g,a,tolerancia):

    iteracionMaxima=100
    i = 0 # iteración
    b = a
    print("n", "                     Pn                                           Error relativo")
    print("-")
    error= tolerancia
    while(error>=tolerancia and i<=iteracionMaxima and b <=999999):
        print(i,'          ',b,"                                           ",error)
        a = b
        b = g(a)
        
        
        error= abs(b-a)/b
        i = i + 1
    print(i,'          ',b,"                                           ",error)    
    respuesta = b
   
    
    if (i>=iteracionMaxima or b>=999999 ):
        respuesta = np.nan
    return(respuesta)

    
    

def grafica(g,f,punto):
 x=np.linspace(-10,10,1000)
 x2=np.linspace(-10000000000,1000000000,100)
 




 plt.axvline( 0 ,color ='black')
 plt.axhline(0,color ='black')


 plt.scatter(punto, 0,color="red")
 plt.plot(x,f(x),label='funcion1',color="green")
 plt.plot(x,g(x),label='funcion2',color="orange")
 plt.legend(loc=1)

 v=[ -20,20,-12,12]

 plt.xlabel('x')
 plt.ylabel('y')
 plt.grid()
 plt.axis(v)
 plt.show()










# PROGRAMA ---------

# Hallar raiz
f = lambda x: np.exp(-x) - x         #converge        funcion e^-x-x   
g = lambda x: np.exp(-x)                               #funcion e^-x 

# f = lambda x: x*x+1                       #no se puede sacar raiz a numeros negativos   
# g = lambda x: np.sqrt(-1+x)    


#f = lambda x: x*x-5                   #no converge                     
#g = lambda x: x*x-5

#f = lambda x: np.sin(x)-x                   # converge                     
#g = lambda x: np.sin(x)   

a = 1       # intervalo
tolera = 0.00001

respuesta = puntofijo(g,a,tolera)





if np.isnan(respuesta):
    print('no converge')
else:
    print(respuesta)
    grafica(g,f,respuesta)
    
#Grafica









