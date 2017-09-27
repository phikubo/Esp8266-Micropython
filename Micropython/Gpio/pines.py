import machine
miPin=machine.Pin(0, machine.Pin.OUT)
#se refiere a gpio 0, que esta en el D3.
miPin.value(1)

###prueba terminada.
#funcionamiento de los pines:

#Pins:| D0 | D1  | D2  | D3  | D4  |VCC GND| D5  | D6   | D7   | D8    |
#GPIO:| 16 | 5***| 4***| 0***| 2***|       | 14**| 12***| 13***| 15*** |
#
#---->8 pines disponibles de 9

#Los Pins se refieren a la referencia física de la board,
#pero python no reconoce esa referencia, pero si reconoce
#la del GPIO, por tanto si se desea usar los pines en upython
#se referencian los GPIO.

#segun la api:  Not all pins are available to use, in most cases 
#only pins 0, 2, 4, 5, 12, 13, 14, 15, and 16 can be used.