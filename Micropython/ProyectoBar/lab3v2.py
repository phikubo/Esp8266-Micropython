#----importar librearias
try:
    import gc
    from machine import I2C,Pin, SPI
    import machine
    import sys
    import network
    import time, ustruct
    import dht
    import urequests
    import pcd8544, framebuf
    import conectar_red
    gc.collect()
    print("Modulos:OK")
except:
    print("Modulos: ERROR")
#----funciones auxialiares
#import time #borrar 
def interrupt(p):
    global intCuenta, parsed_str
    time.sleep_ms(50)
    if (boton.value()==0):
        return
    while(boton.value() == 1):
        time.sleep_ms(100)
    time.sleep_ms(100)
    intCuenta+=1
    print("irq counter",intCuenta)
    #time.sleep(1)
    response = urequests.get('http://192.168.1.18:8000/GestionAc/pedirPin/')
    parsed=response.json()
    parsed_str=str(parsed["id"]) #valorPin
    imprimir(parsed_str)
#----declaracion de variables
intCuenta=0
parsed_str="No Pin"
#
#incluso definicion de pines.
try:
    led=Pin(16,Pin.OUT)
    led.value(0)
    sensorTemperatura=dht.DHT11(machine.Pin(4))
    boton=Pin(5, Pin.IN)
    spi = SPI(1, baudrate=328125, polarity=0, phase=0)
    cs = Pin(2)
    dc = Pin(15)
    rst = Pin(0)
    bl = Pin(12, Pin.OUT, value=1)
    #
    print("Variables:OK")
except:
    print("Variables: ERROR")
#inicializar variables
try:
    boton.irq(trigger=Pin.IRQ_RISING, handler=interrupt)
    lcd = pcd8544.PCD8544(spi, cs, dc, rst)
    buffer = bytearray((lcd.height // 8) * lcd.width)
    framebuf = framebuf.FrameBuffer1(buffer, lcd.width, lcd.height)
    sta_if=network.WLAN(network.STA_IF)
    ap_if=network.WLAN(network.AP_IF)
    ap_if.active(False)
    #
    gc.collect()
    print("Inicializacion: OK")
except Exception as n:
    print("Inicializacion: ERROR", n)
#OTRAS FUNCIONES QUE NECESITAN INICIALIZACION
def imprimir(mistr):
    try:
        #
        msgAux=""
        msgAux2=""
        msgAux3=""
        msg=str(mistr)
        msglen=len(msg)
        print(msglen)
        print(mistr)
    except:
      print("error")
    for i in range(msglen):
        if i<10:
            msgAux=msgAux+msg[i]
        elif i<20:
            msgAux2=msgAux2+msg[i]
        else:
            msgAux3=msgAux3+msg[i]
    if msglen<=10 and msglen>0 :
        print(msgAux+".")
        try:
            framebuf.fill(0)
            framebuf.text(msgAux+".",0,0,1)
            lcd.data(buffer)
        except Exception as e:
            print(e)
    elif msglen<=19 and msglen>=9:
        framebuf.fill(0)
        framebuf.text(msgAux+"-",0,0,1)
        framebuf.text(msgAux2+".",0,9,1)
        lcd.data(buffer)
    elif msglen<=39 and msglen>19:
        framebuf.fill(0)
        framebuf.text(msgAux+"-",0,0,1)
        framebuf.text(msgAux2+"-",0,9,1)
        framebuf.text(msgAux3+"-",0,18,1)
        lcd.data(buffer)
        
def ubicar(msg_temp,msg_est):
        msgAuxt=str(msg_temp)
        msgAuxSt=str(msg_est)
        print(msgAuxt,msgAuxSt)
        framebuf.text(msgAuxt+" Grados",0,27,1)
        framebuf.text(msgAuxSt,0,36,1)
        lcd.data(buffer)
#----inicio del main
print("------------------MAIN-----------------")
time.sleep(1)
estadoInternet=sta_if.isconnected()
print(estadoInternet)
if estadoInternet==False:
    try:
        conectar_red.Connect("907793758213","p123581321")
        estadoInternet=sta_if.isconnected()
    except Exception as k:
        print(k)
else:
  pass
try:
    while estadoInternet==True:
        print("main: true")
        time.sleep(10)
        imprimir("---Eagle------Bar---->:"+parsed_str)
        sensorTemperatura.measure()
        tempValue=sensorTemperatura.temperature()
        #payload='{"temperature":%s,"table_id":"20"}' %(tempValue)
        #headers = {'content-type': 'application/json'}
        #response= urequests.post("http://7ee1ea27.ngrok.io/post_measurement", data=payload,headers=headers)
        print("sending Temp",tempValue)
        ubicar(tempValue,"No At. 7")
        #con response llamo a una funcion que procese la infomracion y me regrese numeros.
        #con los numeros valido si hay informacion que motrar, 
        #si hay un pedido que fue atentido, si hay: inicio la alarma la alarma, por algunos segundos y regreso
        #el limite maximo de temperatura, si hay: encender viento hasta que no supere el valor requerido
        #por ahora, solo esa informacion
        time.sleep(2)
        print("limpiando datos anteriores")
        print("imprimiendo estado del pedido")
    time.sleep(2)
    print("estado falso")
    #conectar_red.Connect("907793758213","p123581321")
except :
    print("OFF, levantando, ")

