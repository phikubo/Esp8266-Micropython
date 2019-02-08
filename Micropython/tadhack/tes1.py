
import network
import urequests
import time
import sys
import machine
try:
  time.sleep(0.3)
  response = urequests.get('http://jsonplaceholder.typicode.com/albums/1')
  print(type(response))
except Exception as e:
  time.sleep(0.3)
  print(e)
  #sys.exit()
  machine.reset()