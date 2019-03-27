import mfrc522
from os import uname
import machine
    
#sck, mosi, miso, rst, cs
#14,  13,   12,   5,   15  
#D5	 D7	D6  D1
#rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
#Pins:| D0 | D1  | D2  | D3  | D4  |VCC GND| D5  | D6   | D7   | D8    |
#GPIO:| 16 | 5***| 4***| 0***| 2***|       | 14**| 12***| 13***| 15*** |
#sck, mosi, miso, rst, cs
#14, 13,12,5, 15
#rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)

def do_write(data, banco_memoria, pin):

	if uname()[0] == 'WiPy':
		rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")
	elif uname()[0] == 'esp8266':
    #sck, mosi, miso, rst, cs
		rdr = mfrc522.MFRC522(14, 13,12,5, 15)

	else:
		raise RuntimeError("Unsupported platform")

	print("")
	print("Place card before reader to write address 0x0%s" % banco_memoria)
	pin.value(1)
	print("")
	detection=False
	try:
		while detection==False:

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
					detection=True
					print("New card detected")
					print("  - tag type: 0x%02x" % tag_type)
					print("  - uid	 : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
					print("")

					if rdr.select_tag(raw_uid) == rdr.OK:

						key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

						if rdr.auth(rdr.AUTHENT1A, banco_memoria, key, raw_uid) == rdr.OK:
							#st=b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
							#bdata=b"\0%s"%data
							#burn=st+data
							#stat = rdr.write(banco_memoria, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
							#stat2 = rdr.write(banco_memoria, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
							#data=bytearray(15)
							stat = rdr.write(banco_memoria, data)
							rdr.stop_crypto1()
							if stat == rdr.OK:
								print("Data written to card")
							else:
								print("Failed to write data to card")
						else:
							print("Authentication error")
					else:
						print("Failed to select tag")
		print("Ok")
		pin.value(0)
	except KeyboardInterrupt:
		print("Bye")
	return 1

if __name__ == "__main__":
	print("inicio")
	mac="123"
	pin = machine.Pin(0, machine.Pin.OUT)
	banco_memoria=8
	data=bytearray(16)
	singledata=[0,1,2,3]
	data[singledata[0]]=1
	data[singledata[1]]=0
	data[singledata[2]]=0
	data[singledata[3]]=0
	data=bytes(data)
	print(data)
	print("exito: ", do_write(data, banco_memoria, pin))
else:
	print("Modulo lectura")




