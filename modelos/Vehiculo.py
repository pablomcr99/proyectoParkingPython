class Vehiculo():

    def __init__(self,matricula,tipo):
        self.matricula=matricula
        self.tipo=tipo


    @property
    def matricula(self) :
        return self.__matricula

    @matricula.setter
    def matricula(self,newMatricula):
        self.__matricula = newMatricula

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,newTipo):
        self.__tipo = newTipo






