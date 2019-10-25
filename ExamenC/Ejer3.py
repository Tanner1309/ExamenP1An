#Se importa el modulo de matematicas
import math
#Se importa numpy como la palabra np 
import numpy as np
#Se importa matplotlib como la palabra plt 
import matplotlib.pyplot as plt
#se piden los datos necesario
print("Este programa resuelve f(x)=x^3-x-1 ")
xr=int(input("Inserte el valor del primer punto: "))
#se obtiene el primer valor
xr=(10*xr+5)**(1/3)
#se declara la lista donde se guardaran los valores de los errores 
ve=[]
xrr=[]
c=0
while True:
    #se guarda el valor de xr para calcular el error
    xra=xr
    xrr.append(xr)
    xrn=(xr+1)**(1/3)
    #se evalua el error
    e=math.fabs(xra-xrn)
    ve.append(e)
    if e <= 0.000001 or e == 0.0:
        break
    xr=xrn
    
    c=c+1
#se muestra el grafico de error
#se pasa la lista a arreglo
vecE=np.array(ve)
vecXr=np.array(xrr)
#se obtiene el tamano del vector 
x= vecE.size
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