#Por michael
import gc
import sys, time
import pcd8544
from machine import Pin, SPI
import time, ustruct
import math
#con la frecuencia del dispositivo 80k no funciona
#spi = SPI(1, baudrate=80000000, polarity=0, phase=0)
spi = SPI(1, baudrate=328125, polarity=0, phase=0)
cs = Pin(2) #D4
dc = Pin(15) #D8
rst = Pin(0) #D3
#Pin Map
#D3 to RST
#D4 to CE (cs)
#D8 to DC
#D7 to Din
#D5 to Clk
#D6 to BL

bl = Pin(12, Pin.OUT, value=1) #D6
print("Variables:OK")
lcd = pcd8544.PCD8544(spi, cs, dc, rst)
print("lcd ok")
#bl.value(0)
#time.sleep(2)
#bl.value(1)
import framebuf
buffer = bytearray((lcd.height // 8) * lcd.width)
framebuf = framebuf.FrameBuffer1(buffer, lcd.width, lcd.height)
framebuf.fill(1)
lcd.data(buffer)
time.sleep(1)
framebuf.fill(0)
lcd.data(buffer)
#
framebuf.text("Hello,", 0, 0, 1)
lcd.data(buffer)
#
time.sleep(1)
framebuf.fill(0)
lcd.data(buffer)
#
time.sleep(1)
lcd.clear()
#draw 8x16 in bank 0 (rows 0..7)
#lcd.position(0, 0)
#lcd.data(bytearray(b'\xE0\x38\xE4\x22\xA2\xE1\xE1\x61\xE1\x21\xA2\xE2\xE4\x38\xE0\x00'))
# draw 8x16 in bank 1 (rows 8..15)
#lcd.position(0, 1)
#lcd.data(bytearray(b'\x03\x0C\x10\x21\x21\x41\x48\x48\x48\x49\x25\x21\x10\x0C\x03\x00'))
#time.sleep(1)
#lcd.clear()
lcd.reset()
lcd.init()
#
#termox

#framebuf.pixel(8,47,1)
#framebuf.pixel(7,46,1)
#framebuf.pixel(6,45,1)
#framebuf.pixel(5,44,1)
#framebuf.pixel(4,43,1)
#framebuf.pixel(3,42,1)
#framebuf.pixel(2,41,1)
#framebuf.pixel(1,40,1)
#framebuf.pixel(0,39,1)
#
#w=0.09 #nice baja frecuencia
w=0.09
phi=0
amplitud=16
#Amplitud maxima 22. Aplitud minima 2. Sin DC.
#Frecuencia minima 0.05. Frecuencia maxima 0.6
for i in range(84):
    y=24-amplitud*math.sin((i*w)+phi)
    print(i,round(y), y)
    time.sleep_ms(40)
    framebuf.pixel(i,round(y),1)


#framebuf.vline(5, 0, 96, 0xffff)
framebuf.vline(0, 0, 96, 0xffff)
framebuf.hline(0, 24, 96, 0xffff)
lcd.data(buffer)





