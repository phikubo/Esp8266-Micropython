#Implemtenado por Michael para plotear funciones sin librerias.
#Name: ufunctions.
#import numpy as np
import matplotlib.pyplot as plt
import math
import time
import calculadora
#ecuacion de fourier para generar un pulso rectangular con la ecuacion del fenomeno de gibbs    
'''
La ecuacion que simula la suma parcial de armonicos de un pulso rectangular
y(t)=(4/pi)*sum((sen(2*k-1)/(2*k-1))*t), k=1->n
Fuente:http://sistemyse.blogspot.com/
El indice ha cambiado para evitar los numeros pares:
http://mathworld.wolfram.com/FourierSeriesSquareWave.html 

'''


def main(max, puntos, K, amplitud):
    print("main")
    y_sum=0 #
    y_record=[] #
    y_res=[]
    T = calculadora.ulinspace(max,puntos)
    yt=[]
    #print(T)
    for k in range(1,K+1):
        #print("k -> ",k)
        for t in T:
            #print("Operacion: ", "k -> ",k, ", t -> ",t)
            y = amplitud*(4/math.pi)*(math.sin((2*k-1)*t)/(2*k-1))
            y_record.append(y) #Lista de puntos de la funcion.
        #diseño: esta agregando a la lista ambas funciones.
    #
    print("Puntos: ",len(T), ", tamaño del arreglo ", len(y_record), "presicion: ",K)
    for i in range(puntos):
                #print("Suma: ", i, " con ", i+(K-1)*puntos )
                #time.sleep(0.2)
                y_res.append(y_record[i]+y_record[i+(K-1)*puntos])
    K=K-1
    
    while K!=1:
        for i in range(puntos):
                #print("Suma while: ", i, " con ", i+(K-1)*puntos )
                #time.sleep(0.2)
                y_res[i]=y_res[i]+y_record[i+(K-1)*puntos]
        print("Tamaño del arreglo res", len(y_res), "presicion: ",K)
        K=K-1

    plt.plot(T, y_res, "-o")
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title('Fenomeno de Gibbs', fontsize=16, color='r')
    plt.grid(True)
    plt.show()
    
    





if __name__ == "__main__":
    #input: max, puntos para ulinspace. Presicion = n, {n E N}. Indica que tan parecida debe ser la funcion a la curva ideal
    max=7.5
    puntos=40 #no funciona para puntos>200
    presicion=10 #K =presicion
    amplitud=1
    main(max, puntos, presicion, amplitud)

else:
    print("importado gibss")