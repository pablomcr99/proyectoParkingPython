class Parking():

    def __init__(self,plazas_turismos,plazas_motocicletas,plazas_mov_red,lista_clientes,recaudacion,recaudacion_abonados):
        self.__plazas_turismos=plazas_turismos
        self.__plazas_motocicletas=plazas_motocicletas
        self.__plazas_mov_red=plazas_mov_red
        self.__lista_clientes=lista_clientes
        self.__recaudacion=recaudacion
        self.__recaudacion_abonados=recaudacion_abonados



    @property
    def lista_clientes(self):
        return self.__lista_clientes


    @lista_clientes.setter
    def lista_clientes(self,newlistaClientes):
       self.__lista_clientes = newlistaClientes



    @property
    def plazas_motocicletas(self):
        return self.__plazas_motocicletas

    @plazas_motocicletas.setter
    def plazas_motocicletas(self,newPlazaMotocicletas):
        self.__plazas_motocicletas = newPlazaMotocicletas



    @property
    def plazas_turismos(self):
        return self.__plazas_turismos

    @plazas_turismos.setter
    def plazas_turismos(self,newPlazaTurismos):
        self.__plazas_turismos = newPlazaTurismos


    @property
    def plazas_mov_red(self):
        return self.__plazas_mov_red

    @plazas_mov_red.setter
    def plazas_mov_red(self,newPlazaCaravanas):
        self.__plazas_mov_red = newPlazaCaravanas


    @property
    def recaudacion(self):
        return self.__recaudacion

    @recaudacion.setter
    def recaudacion(self,recaudacion):
        self.__recaudacion = recaudacion



    @property
    def recaudacion_abonados(self):
        return self.__recaudacion_abonados

    @recaudacion_abonados.setter
    def recaudacion_abonados(self,recaudacion_abonados):
        self.__recaudacion_abonados = recaudacion_abonados
