import mfrc522
from os import uname
import machine
import time
import urequests
#sck, mosi, miso, rst, cs
#14, 13,12,5, 15
#rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)

def do_read(banco_memoria, pin):
	tipo=9
	url_post_s="http://mediadmin.herokuapp.com/api/v1/schedules/verify"
	headers = {'content-type': 'application/vnd.api+json'}
	
	if uname()[0] == 'WiPy':
		rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")
	elif uname()[0] == 'esp8266':
		rdr = mfrc522.MFRC522(14, 13,12,5, 15)
	else:
		raise RuntimeError("Unsupported platform")

	print("")
	print("Place card before reader to read from address 0x0%s" % (banco_memoria[0]))
	pin.value(1)
	print("")
	detection=False
	#data=""
	try:
		while detection==False:
		#while True:
			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
					detection=True
					print("New card detected")
					print("  - tag type: 0x%02x" % tag_type)
					print("  - uid	 : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
					mac=raw_uid[2]
					print("")

					if rdr.select_tag(raw_uid) == rdr.OK:

						key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

						if rdr.auth(rdr.AUTHENT1A, banco_memoria[0], key, raw_uid) == rdr.OK:
							print("Address %s data: %s" % (banco_memoria[0], rdr.read(banco_memoria[0]) ) )
							data=rdr.read(banco_memoria[0])
							if data[0]==0:
								print("tarjeta vacia", mac)
								return data[0], mac
								break
							elif data[0]==1:
								
								tipol=data[1]
								id_empleado=data[2]
								if tipo == tipol:
									payload = '{"data":{"type":"schedules","attributes":{"employee_id":"%s"}}}'%37
									responsep2= urequests.post(url_post_s, data=payload,headers=headers)
									return 1, data[3]
								else:
									return 0, data[3]
							print(4)
							rdr.stop_crypto1()
							
						else:
							print("Authentication error")
					else:
						print("Failed to select tag")
		print("Ejecucion terminada")
		pin.value(0)
	except KeyboardInterrupt:
		print("Bye")


if __name__ == "__main__":
	print("inicio")
	banco_memoria=[8, 9, 10]
	pin = machine.Pin(0, machine.Pin.OUT)
	test=do_read(banco_memoria, pin)
	pin = machine.Pin(0, machine.Pin.OUT)
	#url_post_s="http://mediadmin.herokuapp.com/api/v1/schedules/verify"
	print(test, type(test[0]))
	if test[0]==0:
		print(0)
		pin.value(1)
	else:
		print(1)
		pin.value(0)
		#url_post_s="http://mediadmin.herokuapp.com/api/v1/schedules/verify"



	time.sleep(4)
	pin.value(0)
	#	print("tarjeta vacia")
	#	pin.value(0)
	#print("exito: ", do_read(banco_memoria, pin))
else:
	print("Modulo lectura")







