import mireadm
import miwritem
import urequests
import time
import machine


def peticion_get(url_get, id_registro):
    url_get=url_get+"/%s/"%id_registro
    response = urequests.get(url_get)
    print(response.txt)

def peticion_post_burn(url_post, mac):
    payload = '{"data":{"type":"attendants","attributes":{"gate":"%s"}}}'%mac
    headers = {'content-type': 'application/vnd.api+json'}
    responsep1= urequests.post(url_post, data=payload,headers=headers)
    print(responsep1.txt)

def peticion_post_schedule(url_post, id_empleado):
    payload = '{"data":{"type":"schedules","attributes":{"employee_id":"%s"}}}'%id_empleado
    headers = {'content-type': 'application/vnd.api+json'}
    responsep2= urequests.post(url_post, data=payload,headers=headers)
    print(responsep2.txt)

def main():
    pass

if __name__ == "__main__":
    pin = machine.Pin(0, machine.Pin.OUT)
    url_get="http://mediadmin.herokuapp.com/api/v1/attendants"
    url_post="http://mediadmin.herokuapp.com/api/v1/schedules/verify"
    #para ambos casos solo cambia el payload
    print("inicio")
    ban_memoria = [8, 9, 10]
    time.sleep(3)
    estado=False
    while estado == False:
        time.sleep(0.5)
        print("Bienvenido")
        mireadm.do_read()
        #detener el ciclo
        #estado=True
    
else:
    print("Modulo importado")
