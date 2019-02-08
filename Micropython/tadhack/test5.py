
import socket
from machine import Timer
import machine
import time


puertos=[3031,3031,3031,3031,6000,6001,6002,6003,6004,6005]
contador_universal=0
def main(contador_universal):
    mi_led=machine.Pin(2,machine.Pin.OUT) #configuramos el pin D3 

    mi_led.value(0) #encendemos el led.-apagamos en realidad
    host = '192.168.4.1' # '192.168.4.1'
    port = 3031
    addr_server = socket.getaddrinfo(host, port)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr_server)
    print("Sever Address: ", addr_server)
    s.listen(2)
    
    c, addr_client = s.accept()
    print("Client Address:",str(addr_client))
    try:
      while(True):
        data = c.recv(1024).decode()
        if not data:
          print("not data")
          break
        print("Received from clinent:", str(data))
        data = 'bye'
        print("Sending to client:", str(data))
        time.sleep(0.6)
        c.send(data.encode())
        c.close()
        break
    except Exception as e:
      print(e)
      pass


def main2(contador_universal):
    host = '192.168.4.1' # '192.168.4.1'
    mi_led=machine.Pin(16,machine.Pin.OUT) #configuramos el pin D3 
    mi_led.value(16) #apagamos en realidad
    #port = 6000
    print("contador universal: ",contador_universal)
    port=Validar_puert(puertos,contador_universal)
    time.sleep(0.5)
    print("puerto asignado, debe salir 3031: ", port)
    try:
      addr_server = socket.getaddrinfo(host, port)[0][-1]
      s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      s2.bind(("192.168.4.1",3031))
    except Exception as e:
      print(e)
    print("Sever Address: ", addr_server)
    s2.listen(2)
    
    c2, addr_client = s2.accept()
    print("Client Address:",str(addr_client))

    while(True):
        data = c2.recv(1024).decode()
        if not data:
            break
        print("Received from clinent:", str(data))
        data="mac addrs pls"
        #print("Sending to client:", str(data))

        #c.send(data.encode())
    print("cerrando socket")
    c.close()
    s.close()

def Validar_puert(puertos,contador):
    puerto_valido=puertos[contador]
    return puerto_valido

if __name__ == '__main__':
    main(contador_universal)
    print("cambio")
    contador_universal=contador_universal+1
    print("contador universal: ",contador_universal)
    tim=Timer(-1)
    tim.init(period=60000,mode=Timer.ONE_SHOT, callback=main2(contador_universal))
    #main()