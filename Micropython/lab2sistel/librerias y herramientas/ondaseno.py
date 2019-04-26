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
    w=0.09
    #w=0.4
    phi=0
    for i in range(84):
        y=10*math.sin((i*w)+phi)
        print(i,round(y), y)
        plt.plot(i, y, "-o")
        #time.sleep_ms(40)
    
    #plt.plot(T, y, "-o")
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title('Onda seno', fontsize=16, color='r')
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