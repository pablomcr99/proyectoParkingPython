class Cliente():


    def __init__(self,dni,nombre,apellidos,num_tarjeta,tipo_abono,email,vehiculo,plaza,pin,fecha_Activacion_Abono,fecha_Caducidad_Abono):
        self.__dni=dni
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.__num_tarjeta=num_tarjeta
        self.__tipo_abono=tipo_abono
        self.__email=email
        self.__vehiculo=vehiculo
        self.__plaza=plaza
        self.__pin=pin
        self.__fecha_Activacion_Abono=fecha_Activacion_Abono
        self.__fecha_Caducidad_Abono=fecha_Caducidad_Abono



    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,newDni):
        self.__dni = newDni


    @property
    def nombre(self):
        return self.__nombre


    @nombre.setter
    def nombre(self,newNombre):
        self.__nombre = newNombre


    @property
    def apellidos(self):
        return self.__apellidos


    @apellidos.setter
    def apellidos(self,newApellidos):
        self._apellidos = newApellidos



    @property
    def num_tarjeta(self):
        return self.__num_tarjeta


    @num_tarjeta.setter
    def num_tarjeta(self,newNumtarjeta):
        self.__num_tarjeta = newNumtarjeta


    @property
    def tipo_abono(self):
        return self.__tipo_abono


    @tipo_abono.setter
    def tipo_abono(self,newTipoAbono):
        self.__tipo_abono = newTipoAbono

    @property
    def email(self):
        return self.__email


    @email.setter
    def email(self,newEmail):
        self.__email = newEmail


    @property
    def vehiculo(self):
        return self.__vehiculo


    @vehiculo.setter
    def vehiculo(self,vehiculo):
        self.__vehiculo = vehiculo


    @property
    def plaza(self):
        return self.__plaza


    @plaza.setter
    def plaza(self,plaza):
        self.__plaza = plaza


    @property
    def pin(self):
        return self.__pin


    @pin.setter
    def pin(self,pin):
        self.__pin = pin


    @property
    def fecha_Activacion_Abono(self):
      return self.__fecha_Activacion_Abono


    @fecha_Activacion_Abono.setter
    def fecha_Activacion_Abono(self,fechaActivacionAbono):
        self.__fecha_Activacion_Abono = fechaActivacionAbono


    @property
    def fecha_Caducidad_Abono(self):
      return self.__fecha_Caducidad_Abono


    @fecha_Caducidad_Abono.setter
    def fecha_Caducidad_Abono(self,fechaCaducidadAbono):
        self.__fecha_Caducidad_Abono = fechaCaducidadAbono
    


