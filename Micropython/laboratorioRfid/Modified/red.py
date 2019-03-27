
#a este modulo se le llama desde otro modulo asi:
#conetar_red.main()
def main():
    import network
    import time
    veces=0
    sta_if=network.WLAN(network.STA_IF)
 
    if sta_if.isconnected():
        print('ya hay una conexion activa, desactivando...')
        sta_if.disconnect()
        print('Reintente nuevamente')
        veces=0
        
    if not sta_if.isconnected():
        print('Conectando a la red...')
        sta_if.active(True)
        #sta_if.connect('Fidelity','PK132158')
        #sta_if.connect('FernandezR','ejecutable95')
        #sta_if.connect('TadHack','12345678')
        #sta_if.connect('LAB-DIGITALES','123456Ab')
        while not sta_if.isconnected() and veces!=4:
            print('Intento: ', veces)
            veces=veces+1
            time.sleep(4)
            pass
            
    if veces==4:
        print('conexion fallida tras:',veces,' intentos')
        veces=0
    if veces!=4 and veces!=0:
        print('Ya te has conectado!, bienvenido...')
        print('Conectado a: ', sta_if.ifconfig())
        veces=0
        
if __name__ == '__main__':
    main()
else:
    print('Modulo Conectar_red importado')


