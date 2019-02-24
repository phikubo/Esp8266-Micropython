import miread
import urequests
import gc
import time
import json
#import conectar_red

def terminar_conexion(api_url):
    api_url+"/terminado"
    responsep= urequests.get(api_url)

def procesar_informacion():
    '''La informaci贸n recibida se entrega al modulo de escritura.'''
    pass

 #informacion lista? entonces escribir
def interfaz_lectura():
    pass
def interfaz_escritura(contenido1, contenido2):
    '''Recibe la zona y cc respectivamente. Escribe estos datos en el puerto 8 y 9.'''
    #falta modificar este puerto
    #\x00\x00\x00\x00\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f
    pass
    #return 1
#Interfaz de escritura.
#habilita el servidor.
def iniciar_comunicacion(api_url, mac):
    '''La tarjeta es ubicada en el lector, debe enviar una peticion de tipo post 
    avisando que tiene informacion. As铆 le dice al servidor que habilite el registro 
    de un acompa帽ante. Cuando es le铆da se termina la ejecuci贸n d lectura.'''
    payload = '{"data":{"type":"attendants","attributes":{"gate":"%s"}}}'%mac
    headers = {'content-type': 'application/vnd.api+json'}
    responsep= urequests.post(api_url, data=payload,headers=headers)
    print(responsep.text)
   

def preguntar_informacion(url, id_registro):
    '''Pregunta al servidor si la informacion del acompa帽ante esta lista. Si esta lista continua.
    Luego recibe la informaci贸n. Los bancos de memoria estan predefinidos como 8 y 9.'''
    url=url+"/%s/"%id_registro
    response = urequests.get(url)
    #procesar infomracion
    #resp=response.json()
    #zona=resp['data']['attributes']['id']
    #return response 



if __name__ == "__main__":
    print("Main")
    #time.sleep(3)
    print("lectura")
    url ="http://mediadmin.herokuapp.com/api/v1/attendants"
    #conectar_red
    
    ##mac=gate
    ##id_registro regresa.


    #puertos a usar:
    ##Codigo de zona=8
    ###Codigo de acompa帽ante=9
    ###C贸digo de paciente=10

    #lee la tarjeta
    #miread.do_read()
    
    #flujo
    #conectarse a la red

    #si hay una targeta envivar id
    #si el texto recibido es 1 el servidor ha respondido

    #proceso: esperar que el cliente(guardia) ingrese datos a la base.
    #esperar 20 segundos preguntar al servidor por informacion de id
    #esperar 10 segundos preguntar al servidor por informacion de id
    #esperar 5 segundo preguntar al servidor por informacion de id
    #fallo en el registro.

    #si informacion de id entonces
        #grabar en puerto 8 la zona
        #grabar en puerto 9 self.cedula
    
    #cambiar por el nombre interfaz_lectura()
    if miread.do_read(8)==1:
        print("read: ok")
        iniciar_comunicacion_exp(url)
        #retire la tarjeta por favor.
        time.sleep(20)
        estado, respuesta=preguntar_informacion(url)
        while estado != "ok":
            time.sleep(10)
        #escribe los datos ya que estado es ok.

        if interfaz_lectura(respuesta[0], respuesta[1]) ==1:
            terminar_conexion()

        #if estado == "ok":
        #    #respuesta debe ser de tipo lista con 2 elementos, zona y cc
        #    interfaz_lectura(respuesta[0], respuesta[1])

    else:
        print("Error")
 
else:
    print("Modulo importado")