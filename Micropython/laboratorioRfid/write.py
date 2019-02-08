import mfrc522
from os import uname


def do_write():

	if uname()[0] == 'WiPy':
		rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")
	elif uname()[0] == 'esp8266':
    
    #sck, mosi, miso, rst, cs
    #14, 13,12,5, 15
	#D5	D7	D6
    #rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
	#Pins:| D0 | D1  | D2  | D3  | D4  |VCC GND| D5  | D6   | D7   | D8    |
    #GPIO:| 16 | 5***| 4***| 0***| 2***|       | 14**| 12***| 13***| 15*** |
    #sck, mosi, miso, rst, cs
    #14, 13,12,5, 15
    #rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)

		rdr = mfrc522.MFRC522(14, 13,12,5, 15)

	else:
		raise RuntimeError("Unsupported platform")

	print("")
	print("Place card before reader to write address 0x08")
	print("")

	try:
		while True:

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
					print("New card detected")
					print("  - tag type: 0x%02x" % tag_type)
					print("  - uid	 : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
					print("")

					if rdr.select_tag(raw_uid) == rdr.OK:

						key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

						if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
							stat = rdr.write(8, b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f")
							rdr.stop_crypto1()
							if stat == rdr.OK:
								print("Data written to card")
							else:
								print("Failed to write data to card")
						else:
							print("Authentication error")
					else:
						print("Failed to select tag")

	except KeyboardInterrupt:
		print("Bye")

