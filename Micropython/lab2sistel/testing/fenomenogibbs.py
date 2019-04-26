#Implemtenado por Michael para plotear funciones sin librerias.
#Name: ufunctions.
#import numpy as np
import matplotlib.pyplot as plt
import math
import time
import tesingconcepts as calculadora
#ecuacion de fourier para generar un pulso rectangular con la ecuacion del fenomeno de gibbs    
'''
La ecuacion que simula la suma parcial de armonicos de un pulso rectangular
y(t)=(4/pi)*sum((sen(2*k-1)/(2*k-1))*t), k=1->n
Fuente:http://sistemyse.blogspot.com/
El indice ha cambiado para evitar los numeros pares:
http://mathworld.wolfram.com/FourierSeriesSquareWave.html 

'''


def main(max, puntos, K):
    print("main")

    y_sum=0 #
    y_record=[] #
    y_res=[]
    T = calculadora.ulinspace(max,puntos)
    yt=[]
    print(T)

    
    for k in range(1,K+1):
        #print("k -> ",k)
        for t in T:
            print("Operacion: ", "k -> ",k, ", t -> ",t)
            y = (4/math.pi)*(math.sin((2*k-1)*t)/(2*k-1))
            y_record.append(y) #Lista de puntos de la funcion.
        #diseño: esta agregando a la lista ambas funciones.
    #
    print("T, y_record: ",len(T), ", ", len(y_record))
    time.sleep(5)
    c=0
    K=K-1
    for i in range(puntos):
                print("Suma: ", i, " con ", i+K*puntos )
                y_res.append(y_record[i]+y_record[i+K*puntos])
    print(K, len(y_res))
    time.sleep(5)
    while K !=1:
        for i in range(puntos):
                print("Suma: ", i, " con ", i+K*puntos )
                y_res[i]=y_res[i]+y_record[i+K*puntos]
        K=K-1
            
            
    '''
    for i in range(puntos):
            print("i: ",i, ", lista2 ", i+puntos )
            print(y_record[i], y_record[i+puntos])
            try:
                y_res.append(y_record[i]+y_record[i+puntos])
            except Exception as e:
                print(e)
    if K>2:
        while K !=1:
            #print("k ", K, ", puntos ", puntos)
            for i in range(puntos):
                print("Suma: ", i, " con ", i+K*puntos )
                y_res.append(y_record[i]+y_record[i+K*puntos])
            K=K-1
            
            for i in range(puntos):
                print("Suma: ", i, " con ", i+K*puntos )
                y_res[i]=y_res[i]+y_record[i+K*puntos]
             
    
    for i in range(puntos):
            print("i: ",i, ", lista2 ", i+puntos )
            y_record[i]=y_record[i]+y_record[i+puntos]
            #Si se deja asi hay problemas por que para n>100, la lista guarda esos valores. Hay que crear otra lista.
    print(len(y_record))
    time.sleep(10)
    while K !=1:
        print("k ", K, ", puntos ", puntos)
        for i in range(puntos):
            print("i: ",i, ", lista2 ", i+puntos )
            y_record[i]=y_record[i]+y_record[i+puntos]
            c=+1
        K=K-1 
    print(len(y_record), "count", c)
    

            
        y = (4/math.pi)*(math.sin((2*k-1)*t)/(2*k-1))
        #y_sum=y #si se puede hacer
        y_sum=np.add(y_sum,y)
        #print(np.shape(y))
        #y_record.append(y)
        plt.plot(t, y_sum)
        #if k>1:
        #    y_sum=np.add(y_record)
        #    plt.plot(t, y_sum)
    '''
    plt.plot(T, y_res)
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title('Fenomeno de Gibbs', fontsize=16, color='r')
    plt.grid(True)
    plt.show()
    
    





if __name__ == "__main__":
    #input: max, puntos para ulinspace. Presicion = n, {n E N}. Indica que tan parecida debe ser la funcion a la curva ideal
    max=30
    puntos=100
    presicion=3 #K =presicion
    main(max, puntos, presicion)

else:
    print("importado gibss")