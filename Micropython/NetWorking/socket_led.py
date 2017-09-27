 
import machine
import socket
import time
import network

mired=network.WLAN(network.AP_IF)
mired.config(essid="prueba_de_red_local", authmode=network.AUTH_WPA_WPA2_PSK, password="123456789")
mired.active(True)
#print(mired.ifconfig('ip'))
#print(mired.ifconfig('gateway'))
print('configuracion total: ',mired.ifconfig())

html='''<!DOCTYPE html>
<html>
<head><title> PRUEBA DE DESARROLLO INICIAL </title></head>
<center><h2>  Webserver para encender un led  on</h2></center>
<form>
<button name ="LED" value='ON' type='submit'> LED ON </button>
<button name="LEDb" value='OFF' type='submit'> LED OFF</button>
<br><br>
'''

led0=machine.Pin(0,machine.Pin.OUT)
led0.value(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)

while True:
	conn,addr=s.accept()
	print("se logro comunicar desde %s" % str(addr))
	request=conn.recv(1024)
	print("Contenido %s" % str(request))
	request=str(request)
	Ledon=request.find('/?LED=ON')
	Ledoff=request.find('/?LEDb=OFF')
	if(Ledon==6):
		led0.value(1)
	if(Ledoff==6):
		led0.value(0)
	response=html
	conn.send(response)
	conn.close()

