import gc
from machine import I2C,Pin, SPI
import machine
import ssd1306
import sys
import network
import time
import dht
import urequests
import conectar_red
gc.collect()



def interrupcion(v):
    global variable
    variable=variable+1
    print('se activo la interrupcion', v)
    print(variable)
    if variable>0:
        print('la variable es mayor que cero, re estableciendo')
        variable=4
        print('ahora la variable es ', variable)
    
    
    
def una_fun_mas():
    print('otra funcion')


def funcion_extra(variable):
    #global variable
    #variable=5
    print('funcion extra', variable)

def main():
    print('se ha ejecutado el main')
    #conectar_red.main()
    
    #definicion de variables, pueden ir por fuera.
    led = Pin(0, Pin.OUT)
    led.value(1)
    d=dht.DHT11(machine.Pin(2))
    
    
    btn_interrpt = Pin(5, Pin.IN)
    btn_interrpt.irq(trigger=Pin.IRQ_RISING, handler=interrupcion)
    
    
    print('variable: ',variable)
    #llamando una funcion extra.
    #funcion_extra(variable)
    time.sleep(2)
    while True:
        
        print('Ejecutando el while true')
        print('valor de la variable: ', variable)
        
        if variable==0:
            print('nada',variable)
            d.measure()
            print('Temperatura: ',d.temperature())
            print('Humedad: ', d.humidity())
            print('ENVIANDO DATOS DE TEMPERATURA') 
            #ESPACIO PARA EL POST           
            time.sleep(10)
        if variable>=4:
            print('se activo una interrupcion', variable)
            break
        
    
if __name__ == '__main__':
    variable=0
    main()
    print('fin del main')
    while True:
        variable=0
        print('INICIANDO PETICION GET') 
        response = urequests.get('http://jsonplaceholder.typicode.com/albums/1')
        print(response.text)
        time.sleep(5)
        print('Renovando servicio...')
        main()
    
else:
    print('Modulo main importado')
    
