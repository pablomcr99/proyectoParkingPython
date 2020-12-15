from datetime import datetime,timedelta
from io import open
import pickle

from modelos.Ticket import Ticket
from modelos.Vehiculo import Vehiculo
import random


fichero = open('ficheros/parking.pckl','rb')
# Cargamos los datos del fichero
parking = pickle.load(fichero)
fichero.close()

class Parking_Servicio():


    def devolver_plazas_libres(self):
        contadorT=15
        contadorM=15
        contadorC=15
        for i in parking.plazas_turismos:
            if i.estado!="libre":
                contadorT-1
        for i in parking.plazas_motocicletas:
            if i.estado!="libre":
                contadorM-1
        for i in parking.plazas_caravanas:
            if i.estado!="libre":
                contadorC-1
        print("Hay "+str(contadorT)+" plazas libres para Turismos")
        print("Hay "+str(contadorM)+" plazas libres para Motocicletas")
        print("Hay "+str(contadorC)+" plazas libres para Caravanas")

    def estado_plazas(self):
        for i in parking.plazas_turismos:
            print("Plaza Para Turismos Id:"+str(i.id)+" ,Estado: "+i.estado)
        for i in parking.plazas_motocicletas:
            print("Plaza Para Motocicletas Id:"+str(i.id)+" ,Estado: "+i.estado)
        for i in parking.plazas_caravanas:
            print("Plaza Para Caravanas Id:"+str(i.id)+" ,Estado: "+i.estado)


    def asignar_plaza(self,newvehiculo):
        if newvehiculo.tipo=="1":
            for i in parking.plazas_turismos:
                if i.estado=="libre":
                    i.vehiculo=newvehiculo
                    i.estado="OCUPADA"
                    break
                break
        if newvehiculo.tipo=="2":
            for i in parking.plazas_motocicletas:
                if i.estado=="libre":
                    i.vehiculo=newvehiculo
                    i.estado="OCUPADA"
                    break
                break
        if newvehiculo.tipo=="3":
            for i in parking.plazas_caravanas:
                if i.estado=="libre":
                    i.vehiculo=newvehiculo
                    i.estado="OCUPADA"
                    break
                break

    def devolver_plaza(self,vehiculo):
        for i in parking.plazas_turismos:
            if i.vehiculo==vehiculo:
                return i.id
        for i in parking.plazas_motocicletas:
            if i.vehiculo==vehiculo:
                return i.id
        for i in parking.plazas_caravanas:
            if i.vehiculo==vehiculo:
                return i.id

    def retirar_vehiculo(self,matricula,idPlaza,Pin):
        for i in parking.plazas_turismos:
            if i.id==idPlaza:
                i.estado="Libre"
                now=datetime.now()
                #parking.recaudacion+=int(now)*0.12


        for i in parking.plazas_motocicletas:
            if i.id==idPlaza:
                i.estado="Libre"
                now=datetime.now()
                #parking.recaudacion+=int(now)*0.08


        for i in parking.plazas_caravanas:
            if i.id==idPlaza:
               i.estado="Libre"
               now=datetime.now()
               #parking.recaudacion+=int(now)*0.45

    def devolver_facturacion(self):
        return parking.recaudacion


    def comprobar_abonado(self,dni):
        for i in parking.lista_clientes:
            if i.dni==dni:
                return True
            else:
                return False

    def devolver_cliente(self,dni):
        for i in parking.lista_clientes:
            if i.dni==dni:
                return i


    def devolver_plaza_cliente(self,cliente):
        return cliente.plaza




    def depositar_abonado(self,plaza):
        for i in parking.plazas_turismos:
            if i.id==plaza.id:
                i.estado="OCUPADO ABONADO"
        for i in parking.plazas_motocicletas:
            if i.id==plaza.id:
                i.estado="OCUPADO ABONADO"
        for i in parking.plazas_caravanas:
            if i.id==plaza.id:
                i.estado="OCUPADO ABONADO"



    def comprobar_plaza(self,idplaza):
        for i in parking.plazas_turismos:
            if i.id==idplaza and i.estado=="OCUPADO ABONADO":
                return True

        for i in parking.plazas_motocicletas:
            if i.id==idplaza and i.estado=="OCUPADO ABONADO":
                return True

        for i in parking.plazas_caravanas:
            if i.id==idplaza and i.estado=="OCUPADO ABONADO":
                return True




    def retirar_abonado(self,matricula,idplaza,pin):
        for i in parking.plazas_turismos:
            if i.id==idplaza:
                i.estado="RESERVADO"

        for i in parking.plazas_motocicletas:
            if i.id==idplaza:
                i.estado="RESERVADO"

        for i in parking.plazas_caravanas:
            if i.id==idplaza:
                i.estado="RESERVADO"

    def calcular_fecha_caducidad(self,tipoAbono):
        if tipoAbono=="1":
            fechaCaducidad1=datetime.now()+timedelta(days=30)
            parking.recaudacion_abonados+=25
            return fechaCaducidad1

        if tipoAbono=="2":
            fechaCaducidad2=datetime.now()+timedelta(days=90)
            parking.recaudacion_abonados+=70
            return fechaCaducidad2

        if tipoAbono=="3":
            fechaCaducidad3=datetime.now()+timedelta(days=180)
            parking.recaudacion_abonados+=130
            return fechaCaducidad3

        if tipoAbono=="4":
            fechaCaducidad4=datetime.now()+timedelta(days=365)
            parking.recaudacion_abonados+=200
            return fechaCaducidad4

    def listaAbonados(self):
        for i in parking.lista_clientes:
            print(i.nombre+" "+i.apellidos+" Abono:"+str(i.tipoabono)+" FechaIn: "+i.fechaActivacionAbono+" FechaFin: "+i.fechaCaducidadAbono);


    def consultaAbonados(self):
        return parking.recaudacionAbonados

    def modificarAbonado(self,dni,nombre,apellidos,email):
        for i in parking.lista_clientes:
            if i.dni==dni:
                i.nombre=nombre
                i.apellidos=apellidos
                i.email=email

    def eliminarAbonado(self,dni):
        cuentaIndice=-1
        for i in parking.lista_clientes:
            cuentaIndice=cuentaIndice+1
            if i.dni==dni:
                parking.lista_clientes.remove(i)














