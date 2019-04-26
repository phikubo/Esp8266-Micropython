#Implemtenado por Michael para obtener un linspace.
import math
import time

def ulinspace(max, puntos):
    '''Ejecuta una operacion similar a linspace pero para microcontroladores. Puntos debe ser par si se desean separaciones equidistantes
    en numeros enteros.'''
    cambio=max/puntos
    maxim=max
    resultado=[maxim]
    #max=max+1

    #for i in range(1,max+1):
    #    print(max-i+1)
        #print(i-puntos)
    #max=max-1
    cambio=max/puntos
    #print("Rata de cambio: ",cambio)
    while max > cambio:
        max=max-cambio
        resultado.append(max)
        #print(maxim, max)
    return resultado




if __name__ == "__main__":
    #Entradas:
    #max: El rango en el que las operaciones se ejecutan.
    #puntos: La cantidad de salidas que se desean obtener del rango.
    max=20
    puntos=3
    res=ulinspace(max,puntos)
    print("ok => ", res)
    #Pruebas esperadas:
    #output 20,10 si p=2
    #output 20, 15, 10, 5 si p=4
    #output 20,18,16,14,12,10,8,6,4,2, si p=10
    #output 20:1 si p =20
    
else:
    print("importado ulinspace")