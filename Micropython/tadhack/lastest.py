
print("Welcome Master to Production")
import time
import machine
import sys
import ubinascii
import network
import socket

from machine import Pin

time.sleep(0.4)
lista=[1,2,3,4,0,4,6,7]
#pin_bad = machine.Pin(0)
#pin_good = machine.Pin(0)
pin_red = machine.Pin(16, machine.Pin.OUT)
pin_grn = machine.Pin(0, machine.Pin.OUT)


def abrir_red():
    mired = network.WLAN(network.AP_IF)
    mired.config(essid="fakeTadhack", authmode=network.AUTH_WPA_WPA2_PSK, password="123456789")
    mired.active(True)
    print('configuracion total: ',mired.ifconfig())
    mac = ubinascii.hexlify(mired.config('mac'),':').decode()
    print (mac)

def abrir_socket(s):
    #s=socket.socket() #creamos el socket
    s.bind(("", 3031))

    s.listen(10) #se deja el socket esperando a clientes
    cliente,a=s.accept()
    
    print("se ha conectado un cliente", cliente)
    print("informacion del cliente: ",a)
    estado=True

    while estado:
        #abrir_socket()
        data=cliente.recv(1) #recibimos un byte.
        if data:
          print("entra aqui",len(data))
          time.sleep(0.8)
          break
        else:
          print("else")
        break
    print("closing socket")
    s.close()
    
    


while True:
  abrir_red() 
  s=socket.socket()
  abrir_socket(s)
  
  #llamamos la funcion
  pin_grn.value(1)
  pin_red.value(0)
  for i in range(1,2):
    print(i)
    time.sleep(0.5)
    for k in lista:
      time.sleep(0.5)
      try:
        print(i/k)
        #puede ocurrir el error
      except:
        #reiniciamos todo, redefiniendo las variables
        print("reiniciando")
        pin_grn.value(0)
        pin_red.value(1)
        print(".")
        time.sleep(0.1)
        print("..")
        time.sleep(0.1)
        print("...")
        time.sleep(0.3)
        print("...")
        gc.collect()
        
  print("final")
  '''try:
    s=socket.socket()
  except Exception as e:
    print(e)'''
  

