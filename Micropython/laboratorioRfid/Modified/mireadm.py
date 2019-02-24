import mfrc522
from os import uname
#sck, mosi, miso, rst, cs
#14, 13,12,5, 15
#rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)

def do_read(banco_memoria):

	if uname()[0] == 'WiPy':
		rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")
	elif uname()[0] == 'esp8266':
		rdr = mfrc522.MFRC522(14, 13,12,5, 15)
	else:
		raise RuntimeError("Unsupported platform")

	print("")
	print("Place card before reader to read from address 0x0%s" % banco_memoria)
	print("")
	detection=False
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
					print("")

					if rdr.select_tag(raw_uid) == rdr.OK:

						key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

						if rdr.auth(rdr.AUTHENT1A, banco_memoria, key, raw_uid) == rdr.OK:
							print("Address %s data: %s" % (banco_memoria, rdr.read(banco_memoria) ) )
							rdr.stop_crypto1()
						else:
							print("Authentication error")
					else:
						print("Failed to select tag")
		print("Ejecucion terminada")
	except KeyboardInterrupt:
		print("Bye")
		return 0
	return 1

if __name__ == "__main__":
	print("inicio")
	banco_memoria=10
	print("exito: ", do_read(banco_memoria))
else:
	print("Modulo lectura")


