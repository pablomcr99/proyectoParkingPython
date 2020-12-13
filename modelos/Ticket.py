class Ticket():

    def __init__(self,matricula_vehiculo,fecha,id_plaza,pin):
        self.__matricula_vehiculo=matricula_vehiculo
        self.__fecha=fecha
        self.__id_plaza=id_plaza
        self.__pin=pin


    @property
    def matricula_vehiculo(self):
        return self.__matricula_vehiculo

    @matricula_vehiculo.setter
    def matricula_vehiculo(self,newMatriculaVehiculo):
       self.__matricula_vehiculo = newMatriculaVehiculo


    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self,newFecha):
        self.__fecha = newFecha

    @property
    def idplaza(self):
        return self.__idplaza

    @idplaza.setter
    def id_plaza(self,newIdPlaza):
        self.__id_plaza = newIdPlaza


    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self,pin):
        self.__pin=pin



