print("Bienvenido maestro")

try:
    import time
    #import machine
    #import sys
    #import network
    import socket
    import gc
    import random
    import urequests
    print("ok")
except:
    print("Error")
    
''' El usuario tiene dos parametros principales, el socket asociado a el, y la mac'''
class userEquipment:
    #cuando creo un objeto de tipo Ue, lo creo con un socket.
    def __init__(self,puerto):
        #variables
        self.puerto=puerto
        self.host='192.168.4.1'
        self.id='zona 1'
        
    def iniciar_socket(self):
        self.addr_server = socket.getaddrinfo(self.host, self.puerto)[0][-1]
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(self.addr_server)
        time.sleep(0.3)
        print("Sever Address: ", self.addr_server)
        self.s.listen(2)
        self.c, self.addr_client = self.s.accept()
        time.sleep(0.3)
        print("c: ",self.c)
        print("addr ",self.addr_client)
        gc.collect()
    def funciones(self):
        pass
    def responder(self):
        time.sleep(0.2)
        print("servidor respondera 200")
        self.data_resp="200"
        self.c.send(self.data_resp.encode())
    def recibir(self):
        time.sleep(0.2)
        print("servidor debe recibir una mac")
        self.data = self.c.recv(1024).decode()
        print(self.data)

    def conectar_django(self):
        payload='{"mac":%s}' %(self.data)
        headers = {'content-type': 'application/json'}
        #la direccion del servidor
        responsep= urequests.post("http://192.168.1.74:3031/api/", data=payload,headers=headers)
        #rp_json=responsep.json()
        print(responsep.text)
    

''' Funciones adicionales '''
def funcion(params):
    pass

def generar_puerto_aleatorio():
    return random.randint(2900,3100)
def verificar_puerto(puerto, lista, cuenta):
    print(cuenta)
    if cuenta==0:
        return puerto
    else:
        for i in lista:
            print(i,puerto)
            if puerto==i:
                #el puerto ya esta en uso 
                pass
            else:
                return puerto


def generar_red():
    pass
def conectar_red():
    pass




def main():
    print("No hay errores")
    lista_de_puertos=[]
    '''
    for i in range(5):
        puerto=generar_puerto_aleatorio()
        time.sleep(0.1)
        print("genere ",puerto)
        puerto_verificado=verificar_puerto(puerto,lista_de_puertos, cuenta)
        print("agregando ", puerto_verificado)
        lista_de_puertos.append(puerto_verificado)
        print(lista_de_puertos)
        cuenta+=1
    '''
    lista_de_puertos.append(3031)
    print(lista_de_puertos)
    try:
        ue1=userEquipment(lista_de_puertos[0])
        ue1.iniciar_socket()
        ue1.recibir()
        ue1.responder()
        ue1.conectar_django()
        #esperando una conexion
    except Exception as e:
        print(e)
    #print(ue1.puerto, ue1.host)

if __name__ == '__main__':
    print("Ejutando main")
    main()