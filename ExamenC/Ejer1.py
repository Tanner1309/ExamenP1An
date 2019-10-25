#se importan las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
import math
#se piden los datos necesarios
print("Este programa resuelve la ecuacion f(x)=x^3+4*x^2-10")
xl=int(input("Inserte el valor del limite menor: "))
xu=float(input("Inserte el valor del limite mayor: "))
#se obtiene el primer xr
xr=(xl+xu)/2
#se declara la lista donde se guardaran los valores de los errores 
ve=[]
xrr=[]
while True:
    #se evalua en la funcion xl xu y xr
    fxl=((xl**3)+(4*(xl**2)))-10
    fxr=((xr**3)+(4*(xr**2)))-10
    fxu=((xu**3)+(4*(xu**2)))-10
    #se guarda el valor de xr para calcular el error
    xra=xr
    if (fxl*fxr) < 0:
        xu=xr
    elif (fxu*fxr) < 0:
        xl=xr
    xrn=(xl+xu)/2
    #se evalua el error
    e=math.fabs(xrn-xra)
    ve.append(e)
    xrr.append(xrn)
    if e <= 0.00001:
        break
    xr=(xl+xu)/2
#lineas para mostrar el grafico de error
#se pasa la lista a arreglo
vecE=np.array(ve)
vecXr=np.array(xrr)
#se obtiene el tamano del vector 
x=vecE.size
#se crea el vector x
vecX=np.arange(0,x)
print("El resultado mas cercano es:",xr)
#se hace la grafica
plt.figure()
plt.subplot(2,1,1)
plt.plot(vecX,vecE, "go--", linewidth=2, markersize=5)
plt.title("$Error$")
plt.subplot(2,1,2)
plt.plot(vecX,vecXr, "bo-", linewidth=2, markersize=5)
plt.title("$Resultados$")
#se muestra la grafica
plt.show()