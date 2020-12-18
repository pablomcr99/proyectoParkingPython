from datetime import datetime,timedelta
from io import open
import pickle

from modelos.Cliente import Cliente
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

ps.cargar()

print("Bienvenido al Parking robotizado")
while eleccion!=0:
    print("1 para entrar como Cliente")
    print("2 para entrar como Administrador")
    print("0 para salir")
    try:
        eleccion = int(input('¿Qué desea hacer?: '))
        if eleccion!=1 and eleccion!=2 and eleccion!=0:
            raise ValueError
        else:
            if eleccion==1:
                while eleccion2!=0 :
                    print("1 para depositar vehiculo")
                    print("2 para retirar vehiculo")
                    print("3 para depositar abonado")
                    print("4 para retirar abonado")
                    print("0 para salir")
                    try:
                        eleccion2 = int(input('¿Qué desea hacer? '))
                        if eleccion2!=1 and eleccion2!=2 and eleccion2!=3 and eleccion2!=4 and eleccion2!=0:
                            raise ValueError
                        else:
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
                                ts.imprimirTicket()
                            if eleccion2==2:
                                matricula2 = input('Introduzca matricula: ')
                                idplaza = int(input('Diga el Id de la plaza '))
                                pin = int(input('Introduzca el PIN'))
                                ps.retirar_vehiculo(matricula2,idplaza,pin)
                                print("Su vehiculo ha sido retirado")
                            if eleccion2==3:
                                acceso = input('Para demostrar que eres un cliente abonado introduce tu dni :')
                                if ps.comprobar_abonado(acceso):
                                    ps.depositar_abonado(ps.devolver_plaza_cliente(ps.devolver_cliente(acceso)))
                                    print("Su vehiculo ha sido depositado correctamente")
                                else:
                                    print("No estas abonado o has introducido mal los datos")
                            if eleccion2==4:
                                acceso2 = input('Introduzca la matricula de su vehiculo : ')
                                idplaza2 = int(input('Introduzca el id de su plaza : '))
                                pin2 = int(input('Introduzca su pin :'))
                                if ps.comprobar_plaza(idplaza2):
                                    ps.retirar_abonado(acceso2,idplaza2,pin2);
                                    print("Se ha retirado su vehiculo pero su plaza ha quedado reservada")
                                else:
                                    print("No estas abonado,has introducido mal los datos o su vehiculo no se encuentra en el parking")
                            if eleccion2==0:
                                break
                    except ValueError:
                        print("Introduzca una de las opciones posibles")
            elif eleccion==2:
                pase=int(input("Introduzca contraseña de administrador: "))
                if pase==passAdmin:
                    while eleccion3!=0 :
                        print("1 para ver el estado del parking")
                        print("2 para ver la facturacion")
                        print("3 para consultar abonados")
                        print("4 añadir abonado")
                        print("5 modificar abonado")
                        print("6 borrar abonado")
                        print("7 consultar caducidad")
                        print("0 para salir")
                        try:
                            eleccion3 = int(input('¿Qué desea hacer? '))
                            if eleccion3!=1 and eleccion3!=2 and eleccion3!=3 and eleccion3!=4 and eleccion3!=5 and eleccion3!=6 and eleccion3!=7 and eleccion3!=0:
                                raise ValueError
                            else:
                                    if eleccion3==1:
                                        ps.estado_plazas()
                                    elif eleccion3==2:
                                        print("La recaudación es de "+str(ps.devolver_facturacion()))
                                    elif eleccion3==3:
                                        ps.lista_abonados()
                                        print("La recaudacion Total por abonos es "+str(ps.consulta_abonados())+" euros")
                                    elif eleccion3==4:
                                        dni = input('Introduzca dni :')
                                        nombre=input('Introduzca Nombre: ')
                                        apellidos=input('Introduza apellidos: ')
                                        num_tarjeta=int(input('Introduzca el numero de su Tarjeta: '))
                                        tipo_abono=input('¿Qué tipo de abono desea? 1:Mensual 2:Trimestral 3:Semestral 4:Anual')
                                        email=input('Introduzca email: ')
                                        fecha_activacion=datetime.now()
                                        nuevo_pin=random.randint(1000,9999)
                                        nuevo_cliente=Cliente(dni,nombre,apellidos,num_tarjeta,tipo_abono,email,None,None,nuevo_pin,fecha_activacion,ps.calcular_fecha_caducidad(tipo_abono))
                                        ps.guardar_cliente(nuevo_cliente)
                                        print("El cliente y el abono han sido guardados correctamente")
                                    elif eleccion3==5:
                                        int_dni = input('Introduce el dni del cliente que deseas modificar :')
                                        nn=input('Introduce nuevo nombre: ')
                                        nap=input('Introduce nuevos apellidos: ')
                                        n_email=input('Introduce de nuevo el email para modificarlo: ')
                                        ps.modificar_abonado(int_dni,nn,nap,n_email)
                                        print("El cliente abonado ha sido eliminado correctamente")
                                    elif eleccion3==6:
                                        intDNi2 = input('Introduce el dni del cliente que deseas eliminar :')
                                        ps.eliminar_abonado(intDNi2)
                                        print("El cliente abonado ha sido eliminado correctamente")
                                    elif eleccion3==7:
                                        mes=input('Introduce el mes del que quieras saber la caducidad :')
                                        print("El abono de "+ps.caducidadMes(mes)+" caduca este mes")
                                    elif eleccion3==0:
                                        break
                        except ValueError:
                            print("Introduzca una de las opciones posibles")
                    else:
                        print("No puedes pasar")
                        break
            elif eleccion==0:
                break
    except ValueError:
        print("Introduzca una de las opciones posibles")
ps.actualizar_parking(ps.devolver_parking())
print("¡Pase un buen día!")
print("Cerrando...")
