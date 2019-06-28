
#implemented by Phikubo

#mired.config(essid="Red_de_prueba_phi")
#mired.config(essid="<AP_NAME>", authmode=network.AUTH_WPA_WPA2_PSK, password="<password>")
#mired.active(True)
#mired.ifconfig('ip')
#mired.ifconfig('gateway')


def create_net(ap_name,passw):
    import network
    mired=network.WLAN(network.AP_IF)
    mired.config(essid=ap_name, authmode=network.AUTH_WPA_WPA2_PSK, password=passw)
    mired.active(True)
    mired.ifconfig('ip')
    mired.ifconfig('gateway')



if __name__ == "__main__":
    #mired=network.WLAN(network.AP_IF)
    ap_name="upylab2sistel"
    passw=123456789
    create_net(ap_name,passw)
else:
    print("networking importado")