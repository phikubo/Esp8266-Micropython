import mireadm
import miwritem
import urequests
import time
import machine
import json
from mireadm import do_read


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
    url_post_s="http://mediadmin.herokuapp.com/api/v1/schedules/verify"
    url_post_f="http://mediadmin.herokuapp.com/api/v1/attendants"
    #para ambos casos solo cambia el payload
    #bancos_8=[0:estado, 1:tipo,2:id_registro, 3: zona, 4:mac]
    print("inicio")
    mac=5
    ban_memoria = [8,9]
    banco_memoria = ban_memoria[0]
    time.sleep(1)
    estado_ciclo=False
    c=0
    while estado_ciclo == False:
        time.sleep(0.5)
        print("Bienvenido")
        contenido=do_read(ban_memoria,pin)
        print("content")
        a,b=contenido
        print(type(a),type(b))
        #if contenido[0]==0:
        #   pass
        #else:
            #return contenido
        #   break
        #print(7)
        estado=contenido[0]
        mac=contenido[1]
        payload = '{"data":{"type":"attendants","attributes":{"gate":"%s"}}}'%mac
        headers = {'content-type': 'application/vnd.api+json'}
        responsep1= urequests.post(url_post_f, data=payload,headers=headers)
        resp=responsep1.json()
        id_registro=resp['data']['id'] #to burn
        url_get=url_get+"/%s/"%id_registro
        #ciclo for
        response = urequests.get(url_get)
        resp2=response.json()
        tipo=resp2['data']['type']
        zona=resp2['data']['attributes']['area_id']
        print(7)
        for i in range(3):
            print(8)
            print(zona)
            time.sleep(10)
            if zona == 0:
                print(9)
                #url_get=url_get+"/%s/"%id_registro
                response = urequests.get(url_get)
                #print(10)
                resp2=response.json()
                #print(11)
                tipo=resp2['data']['type']
                zona=resp2['data']['attributes']['area_id']
                #print(12)
                
            else:
                pass
        
        #print('z',zona,'t',tipo, 'id',id_registro, 'mac',mac)
        #print(13)
        id_registro=int(id_registro)
        #print(131)
        if tipo =='attendants':
            #print(132)
            tipo=8
        else:
            tipo=9
        #print(133)
        data=bytearray(16)
        #print(134)
        singledata=[0,1,2,3,4]
        #print(14)
        data[singledata[0]]=estado
        #print(15)
        data[singledata[1]]=tipo
        #print(16)
        data[singledata[2]]=id_registro
        data[singledata[3]]=zona
        #print(18)
        print(mac)
        data[singledata[4]]=mac
        data=bytes(data)
        miwritem.do_write(data,banco_memoria,pin)
        #print(responsep1.text)
        #peticion_post_burn(url_post,mac)
        #miwritem.do_write()
        #print(type(data))
        #print(datos)
        #if data[0]==0:
        #    print("data vacio")
        c=c+1
        if c==2:
            estado_ciclo=True
        #detener el ciclo
        #estado=True
    print("hubo break", contenido)
else:
    print("Modulo importado")






