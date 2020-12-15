class Plaza():

    def __init__(self,id,estado,vehiculo):
        self.__id=id
        self.__estado=estado
        self.__vehiculo=vehiculo


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,Id):
        self.__id = Id

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self,estado):
        self.__estado = estado


    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self,newVehiculo):
        self.__vehiculo = newVehiculo








