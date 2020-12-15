from datetime import datetime,timedelta
from io import open
import pickle

from modelos.Ticket import Ticket
from modelos.Vehiculo import Vehiculo
from servicios.parkingservicio import Parking_Servicio
from servicios.ticketServicio import Ticket_servicio
import random


ps=Parking_Servicio()

eleccion=int
eleccion2=int
eleccion3=int
passAdmin=1234
pase=int

fichero = open('ficheros/parking.pckl','rb')
# Cargamos los datos del fichero
parking = pickle.load(fichero)
fichero.close()

print("Bienvenido al Parking robotizado")
while eleccion!=0:
    print("1 para entrar como Cliente")
    print("2 para entrar como Administrador")
    print("0 para salir")
    eleccion = int(input('¿Qué desea hacer?: '))

    if eleccion==1:
        while eleccion2!=0 :
            print("1 para depositar vehiculo")
            print("2 para retirar vehiculo")
            print("3 para depositar abonado")
            print("4 para retirar abonado")
            print("0 para salir")
            eleccion2 = int(input('¿Qué desea hacer? '))
            if eleccion2==1:
                ps.devolver_plazas_libres()
                matricula = int(input('Introduzca matricula '))
                tipo = input('Introduzca Tipo 1:turismo 2:motocicletas 3:caravanas ')
                nuevoVehiculo=Vehiculo(matricula,tipo)
                ps.asignar_plaza(nuevoVehiculo)
                m = datetime.now()
                Pin=random.randint(1000,9999)
                ticket=Ticket(matricula,m,ps.devolver_plaza(nuevoVehiculo),Pin)
                ts=Ticket_servicio(ticket)
                ts.guardar()
                ts.imprimirTicket();
                break
            if eleccion2==2:
                matricula2 = input('Introduzca matricula: ')
                idplaza = int(input('Diga el Id de la plaza '))
                pin = int(input('Introduzca el PIN'))
                ps.retirarVehiculo(matricula2,idplaza,pin)
                print("Su vehiculo ha sido retirado")
                break
            if eleccion2==3:
                break
            if eleccion2==4:
                break
            if eleccion2==0:
                break

    elif eleccion==2:
        pase=int(input("Introduzca contraseña de administrador: "))
        if(pase==passAdmin):
            while eleccion3!=0 :
                print("1 para ver el estado del parking")
                print("2 para ver la facturacion")
                print("3 para consultar abonados")
                print("4 añadir abonado")
                print("5 modificar abonado")
                print("6 borrar abonado")
                print("7 consultar caducidad")
                print("0 para salir")
                eleccion3 = int(input('¿Qué desea hacer? '))
                if eleccion3==1:
                    ps.estadoPlazas()
                    break
                elif eleccion3==2:
                    break
                elif eleccion3==3:
                    break
                elif eleccion3==4:
                    break
                elif eleccion3==5:
                    break
                elif eleccion3==6:
                    break
                elif eleccion3==7:
                    break
                elif eleccion3==0:
                    break
        else:
            print("No puedes pasar")
            break
    elif eleccion==0:
        break
print("Cerrando...")
