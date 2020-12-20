from datetime import datetime,timedelta
from io import open
import pickle

from modelos.Plaza import Plaza
from modelos.Ticket import Ticket
from modelos.Vehiculo import Vehiculo
import random


fichero = open('ficheros/parking.pckl','rb')
# Cargamos los datos del fichero
parking = pickle.load(fichero)
fichero.close()

class Parking_Servicio():




    def cargar(self):
        f=open('ficheros/lista_clientes.pckl','rb')
        clientes=pickle.load(f)
        f.close()
        parking.lista_clientes=clientes

        f2=open('ficheros/recaudacion_abonados.pckl','rb')
        recaudacion_abonados=pickle.load(f2)
        f2.close()
        parking.recaudacion_abonados=recaudacion_abonados

        f3=open('ficheros/recaudacion.pckl','rb')
        recaudacion=pickle.load(f3)
        f3.close()
        parking.recaudacion=recaudacion

    def devolver_parking(self):
        return parking

    def actualizar_parking(self,nuevo_parking):
        fichero=open('ficheros/parking.pckl','wb')
        pickle.dump(nuevo_parking,fichero)
        fichero.close()

    def generar_plazas(self,n):
        nTurismos=round((n*70)/100)
        nMotocicletas=round((n*15)/100)
        nMovRed=round((n*15)/100)
        parking.plazas_turismos=[]
        parking.plazas_motocicletas=[]
        parking.plazas_mov_red=[]
        for i in range(0,nTurismos):
            nuevaPlaza=Plaza(int(i)+1,"libre",None)
            parking.plazas_turismos.append(nuevaPlaza)
        for i in range(0,nMotocicletas):
            nuevaPlaza=Plaza(int(i)+1+len(parking.plazas_turismos),"libre",None)
            parking.plazas_motocicletas.append(nuevaPlaza)
        for i in range(0,nMovRed):
            nuevaPlaza=Plaza(int(i)+1+len(parking.plazas_motocicletas)+len(parking.plazas_turismos),"libre",None)
            parking.plazas_mov_red.append(nuevaPlaza)



    def devolver_plazas_libres(self):
        contadorT=len(parking.plazas_turismos)
        contadorM=len(parking.plazas_motocicletas)
        contadorMr=len(parking.plazas_mov_red)
        for i in parking.plazas_turismos:
            if i.estado!="libre":
                contadorT=contadorT-1
        for i in parking.plazas_motocicletas:
            if i.estado!="libre":
                contadorM=contadorM-1
        for i in parking.plazas_mov_red:
            if i.estado!="libre":
                contadorMr=contadorMr-1
        print("Hay "+str(contadorT)+" plazas libres para Turismos")
        print("Hay "+str(contadorM)+" plazas libres para Motocicletas")
        print("Hay "+str(contadorMr)+" plazas libres para Movilidad Reducida")

    def estado_plazas(self):
        for i in parking.plazas_turismos:
            print("Plaza Para Turismos Id:"+str(i.id)+" ,Estado: "+i.estado)
        for i in parking.plazas_motocicletas:
            print("Plaza Para Motocicletas Id:"+str(i.id)+" ,Estado: "+i.estado)
        for i in parking.plazas_mov_red:
            print("Plaza Para Movilidad Reducida Id:"+str(i.id)+" ,Estado: "+i.estado)


    def asignar_plaza(self,newvehiculo):
        primeraPlazaLibre=Plaza(None, None, None)
        if newvehiculo.tipo=="1":
            for i in parking.plazas_turismos:
                if i.estado=="libre":
                    i.vehiculo=newvehiculo
                    i.estado="OCUPADA"
                    break

        if newvehiculo.tipo=="2":
            for i in parking.plazas_motocicletas:
                if i.estado=="libre":
                    i.vehiculo=newvehiculo
                    i.estado="OCUPADA"
                    break

        if newvehiculo.tipo=="3":
            for i in parking.plazas_mov_red:
                if i.estado=="libre":
                    i.vehiculo=newvehiculo
                    i.estado="OCUPADA"
                    break

    def asignar_plaza_abonado(self,newvehiculo):
        primeraPlazaLibre=Plaza(None, None, None)
        if newvehiculo.tipo=="1":
            for i in parking.plazas_turismos:
                if i.estado=="libre":
                    i.vehiculo=newvehiculo
                    return i
                    break

        if newvehiculo.tipo=="2":
            for i in parking.plazas_motocicletas:
                if i.estado=="libre":
                    i.vehiculo=newvehiculo
                    return i
                    break

        if newvehiculo.tipo=="3":
            for i in parking.plazas_mov_red:
                if i.estado=="libre":
                    i.vehiculo=newvehiculo
                    return i
                    break

    def devolver_plaza(self,vehiculo):
        for i in parking.plazas_turismos:
            if i.vehiculo==vehiculo:
                return i.id
        for i in parking.plazas_motocicletas:
            if i.vehiculo==vehiculo:
                return i.id
        for i in parking.plazas_mov_red:
            if i.vehiculo==vehiculo:
                return i.id

    def retirar_vehiculo(self,matricula,idPlaza,Pin):
        for i in parking.plazas_turismos:
            if i.id==idPlaza:
                i.estado="libre"
                i.vehiculo=None
                now=datetime.now()
                parking.recaudacion+=5*0.12
        for i in parking.plazas_motocicletas:
            if i.id==idPlaza:
                i.estado="libre"
                i.vehiculo=None
                now=datetime.now()
                parking.recaudacion+=5*0.08
        for i in parking.plazas_mov_red:
            if i.id==idPlaza:
               i.estado="libre"
               i.vehiculo=None
               now=datetime.now()
               parking.recaudacion+=5*0.45

    def devolver_facturacion(self):
        return parking.recaudacion


    def comprobar_abonado(self,dni):
        encontrado=True
        for i in parking.lista_clientes:
            if i.dni==dni:
                encontrado=True
            else:
                encontrado=False
        return encontrado

    def devolver_cliente(self,dni):
        for i in parking.lista_clientes:
            if i.dni==dni:
                return i


    def devolver_plaza_cliente(self,cliente):
        return cliente.plaza

    def guardar_cliente(self,cliente):
        parking.lista_clientes.append(cliente)
        f= open('ficheros/lista_clientes.pckl','wb')
        pickle.dump(parking.lista_clientes,f)
        f.close()




    def depositar_abonado(self,plaza):
        for i in parking.plazas_turismos:
            if i.id==plaza.id:
                i.estado="OCUPADO ABONADO"
        for i in parking.plazas_motocicletas:
            if i.id==plaza.id:
                i.estado="OCUPADO ABONADO"
        for i in parking.plazas_mov_red:
            if i.id==plaza.id:
                i.estado="OCUPADO ABONADO"



    def comprobar_plaza(self,idplaza):
        for i in parking.plazas_turismos:
            if i.id==idplaza and i.estado=="OCUPADO ABONADO":
                return True

        for i in parking.plazas_motocicletas:
            if i.id==idplaza and i.estado=="OCUPADO ABONADO":
                return True

        for i in parking.plazas_mov_red:
            if i.id==idplaza and i.estado=="OCUPADO ABONADO":
                return True




    def retirar_abonado(self,matricula,idplaza,pin):
        for i in parking.plazas_turismos:
            if i.id==idplaza:
                i.estado="RESERVADO"

        for i in parking.plazas_motocicletas:
            if i.id==idplaza:
                i.estado="RESERVADO"

        for i in parking.plazas_mov_red:
            if i.id==idplaza:
                i.estado="RESERVADO"

    def calcular_fecha_caducidad(self,tipoAbono):
        f2=open('ficheros/recaudacion_abonados.pckl','wb')
        if tipoAbono=="1":
            fechaCaducidad1=datetime.now()+timedelta(days=30)
            parking.recaudacion_abonados+=25
            pickle.dump(parking.recaudacion_abonados,f2)
            f2.close()
            return fechaCaducidad1

        if tipoAbono=="2":
            fechaCaducidad2=datetime.now()+timedelta(days=90)
            parking.recaudacion_abonados+=70
            pickle.dump(parking.recaudacion_abonados,f2)
            f2.close()
            return fechaCaducidad2

        if tipoAbono=="3":
            fechaCaducidad3=datetime.now()+timedelta(days=180)
            parking.recaudacion_abonados+=130
            pickle.dump(parking.recaudacion_abonados,f2)
            f2.close()
            return fechaCaducidad3

        if tipoAbono=="4":
            fechaCaducidad4=datetime.now()+timedelta(days=365)
            parking.recaudacion_abonados+=200
            pickle.dump(parking.recaudacion_abonados,f2)
            f2.close()
            return fechaCaducidad4


    def lista_abonados(self):
        for i in parking.lista_clientes:
            print(i.nombre+" "+i.apellidos+" Abono:"+str(i.tipo_abono)+" Fecha Inicio: "+str(i.fecha_activacion_abono)+" Fecha Fin: "+str(i.fecha_caducidad_abono))


    def consulta_abonados(self):
        return parking.recaudacion_abonados


    def modificar_abonado(self,dni,nombre,apellidos,email):
        for i in parking.lista_clientes:
            if i.dni==dni:
                i.nombre=nombre
                i.apellidos=apellidos
                i.email=email


    def eliminar_abonado(self,dni):
        cuentaIndice=-1
        for i in parking.lista_clientes:
            cuentaIndice=cuentaIndice+1
            if i.dni==dni:
                parking.lista_clientes.remove(i)
        fichero=open('ficheros/lista_clientes.pckl','wb')
        pickle.dump(parking.lista_clientes,fichero)
        fichero.close()














