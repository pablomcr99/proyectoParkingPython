from datetime import datetime,timedelta
from io import open
import pickle

from modelos.Ticket import Ticket
from modelos.Vehiculo import Vehiculo

import random


class Ticket_servicio():

    def __init__(self,ticket):
        self.__ticket=ticket

    def guardar(self):
        f=open('ficheros/lista_clientes.pckl','rb')
        tickets=pickle.load(f)
        f.close()
        tickets.append(self.__ticket)
        fichero = open('ficheros/tickets.pckl', 'wb')
        pickle.dump(tickets, fichero)
        fichero.close()

    def imprimirTicket(self):
      print("**************************************************************")
      print("*          Fecha: "+str(self.__ticket.fecha)+"                 *")
      print("*                                                            *")
      print("* Matricula: "+str(self.__ticket.matricula_vehiculo)+"          IDplaza: "+str(self.__ticket.id_plaza)+"                           *")
      print("*                                                            *")
      print("*           PIN: "+ str(self.__ticket.pin)+"                                        *")
      print("*                                                            *")
      print("*                                                            *")
      print("**************************************************************")



