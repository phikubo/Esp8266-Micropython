

import network
mired=network.WLAN(network.AP_IF)

#mired.config(essid="Red_de_prueba_phi")
mired.config(essid="<AP_NAME>", authmode=network.AUTH_WPA_WPA2_PSK, password="<password>")
mired.active(True)
mired.ifconfig('ip')
mired.ifconfig('gateway')
