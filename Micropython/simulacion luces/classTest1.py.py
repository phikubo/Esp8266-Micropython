

#Developed by Phikubo

import time
from machine import Pin
from machine import ADC
led1=Pin(5,Pin.OUT)
led2=Pin(4,Pin.OUT)

led3=Pin(12,Pin.OUT)
led4=Pin(15,Pin.OUT)

adc0=ADC(0)


class setLuces():
  def __init__(self, ledA,ledB):
    self.ledA=ledA
    self.ledB=ledB
  def blinkTwice(self, param, timing):
    print("Luces parpadeantes, parametro: ", param)
    #Param sirve para indicar si las luces parpadean 2 veces o solo una vez.
    globalCount=0
    while globalCount<param:
      self.ledA.value(1)
      self.ledB.value(1)  
      time.sleep(timing) #antes 0.17
      self.ledA.value(0)
      self.ledB.value(0)
      time.sleep(timing)
      globalCount+=1
      #print(globalCount)
  def blinkOnce(self):
    print("Intercambio de luces")
    
    
  
rojas=setLuces(led1,led2)
azules=setLuces(led3,led4)
 
count=0
while count<50:
  try:
    leer=adc0.read()
    print(leer)
    if leer > 5 and leer <200:
      outTiming=0.1
      rojas.blinkTwice(2,outTiming)
      azules.blinkTwice(2,outTiming)
      
    elif leer > 200 and leer < 400:
      outTiming=0.2
      rojas.blinkTwice(2,outTiming)
      azules.blinkTwice(2,outTiming)
 
    elif leer > 400 and leer < 600:
      outTiming=0.3
      rojas.blinkTwice(2,outTiming)
      azules.blinkTwice(2,outTiming)
      
    elif leer > 600 and leer < 800:
      outTiming=0.4
      rojas.blinkTwice(1,outTiming)
      azules.blinkTwice(1,outTiming)
      
    elif leer > 800 and leer < 1100:
      outTiming=0.5
      rojas.blinkTwice(1,outTiming)
      azules.blinkTwice(1,outTiming)
    
    
    #rojas.blinkTwice(2)
    #azules.blinkTwice(2)
  except Exception as e:
    print(e)
  count+=1
  time.sleep(0.1)
  print(count)


