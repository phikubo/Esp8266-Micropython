from tkinter import*
import tkinter
import socket
import time
contador_global=-1
puertos=[3031,6000,6001,6002,6003,6004,6005]

def preuba_de_funcion_ext():
    print("si imprime esto, se puede usar funciones externas")
    #podre hacer un contador aqui, como poder aumentar un contador al aumentar el boton
def setContador():
    contador=contador+1
    return contador

def main():
    global puertos
    global contador_global
    preuba_de_funcion_ext()
    def Validar_puert(puertos,contador):
        #global puertos
        #global contador_global
        puerto_valido=puertos[contador]
        return puerto_valido
    padX=40
    padY=20
    root = Tk()
    
    root.title("Controlador ESP8266")	
    frame = Frame (root)  #Creamos el contenedor denuestros objetos
    frame.config(bg="#6699FF")
    lbl_titulo = Label(frame, text="Welcome to TadHack!")
    lbl_titulo.grid(row=0, column=0, pady=padY,padx=padX) 
    
    imagenESP = PhotoImage(file="esp82662.png")
    lbl_imagen = Label(frame, image=imagenESP) #Creamos etiqueta para poner la foto del ESP8266
    lbl_imagen.grid (row=0, column=1,columnspan=2,pady=padY,padx=padX) 
    
    lbl_LEDControl = Label (frame, text="Production")
    lbl_LEDControl.grid (row=1, column=0)
    
    def abrirSemaforo():
        global contador_global
        global puertos
        contador_global=contador_global+1
        print("el contador: ")
        print(contador_global)
        print("Se ha abierto el semaforo") #aqui se conecta el socket
        host = '192.168.4.1' #'0.0.0.0'
        
        port=Validar_puert(puertos,contador_global)
        port=3031
        print("valor del puerto", port)
        funcioncion_test()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((host,port))

        #message = input("-->")
        print("se va a iniciar la comunicacion")
        message="ack, mac: mi mac"
        while message != 'bye':
            s.send(message.encode())
            data = s.recv(1024).decode()
            print("Received from server: ", str(data))
            #message = input("-->")
            message=str(data)
            s.send(message.encode())
        print("cerrando socket")
        s.close()

    def confirmarSalida():
        print("Se ha confirmado el semaforo")   
    def funcioncion_test():
        print("entro a la funcion test")    
    btn_LEDOn = Button(frame, text="Abrir Socket", fg="green", command=abrirSemaforo) 
    #btn_LEDOff = Button(frame, text="Confirmar salida", fg="red",command=confirmarSalida)     
    btn_LEDOn.grid (row=1, column=1,pady=padY)                                                       
    #btn_LEDOff.grid (row=1, column=2,pady=padY)     
    frame.pack()
    root.mainloop()


if __name__ == '__main__':
    main()