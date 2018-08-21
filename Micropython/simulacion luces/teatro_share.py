#hardware platform: FireBeetle-ESP8266

import time
from machine import Pin
led1=Pin(5,Pin.OUT)
led2=Pin(4,Pin.OUT)

led3=Pin(12,Pin.OUT)
led4=Pin(15,Pin.OUT)
timing=0.5

def rojas():
  print("rojas")
  rcount=0
  while rcount<2:
    led1.value(1) 
    led2.value(1)  
    time.sleep(timing) #antes 0.17
    led1.value(0)
    led2.value(0)
    time.sleep(timing)
    rcount+=1
    print(rcount)
  

def azules():
  print("azules")
  bcount=0
  while bcount<2:
    led3.value(1) 
    led4.value(1)  
    time.sleep(timing) #antes 0.17
    led3.value(0)
    led4.value(0)
    time.sleep(timing)
    bcount+=1
    print(bcount)
 
count=0
while count<10:
  rojas()
  try:
    azules()
  except Exception as e:
    print(e)
  count+=2
  print(count)

  
  
