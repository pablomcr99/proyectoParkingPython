class Parking():

    def __init__(self,plazas_turismos,plazas_motocicletas,plazas_caravanas,lista_clientes,recaudacion,recaudacion_abonados):
        self.__plazas_turismos=plazas_turismos
        self.__plazas_motocicletas=plazas_motocicletas
        self.__plazas_caravanas=plazas_caravanas
        self.__lista_clientes=lista_clientes
        self.__recaudacion=recaudacion



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
    def plazas_caravanas(self):
        return self.__plazas_caravanas

    @plazas_caravanas.setter
    def plazas_caravanas(self,newPlazaCaravanas):
        self.__plazas_caravanas = newPlazaCaravanas


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



"""    def devolverPlazasLibres():
        contadorT=15
        contadorM=15
        contadorC=15
        for(let i=0;i<this._plazasTurismos.length;i++){
            if(this._plazasTurismos[i].estado!="libre"){
                contadorT--;
            }
        }
        for(let i=0;i<this._plazasMotocicletas.length;i++){
            if(this._plazasMotocicletas[i].estado!="libre"){
                contadorM--;
            }
        }
        for(let i=0;i<this._plazasCaravanas.length;i++){
            if(this._plazasCaravanas[i].estado!="libre"){
                contadorC--;
            }
        }
        console.log("Hay "+contadorT+" plazas libres para Turismos");
        console.log("Hay "+contadorM+" plazas libres para Motocicletas");
        console.log("Hay "+contadorC+" plazas libres para Caravanas");
    }

    estadoPlazas(){
        for(let i=0;i<this._plazasTurismos.length;i++){
            console.log("Plaza Para Turismos Id:"+this._plazasTurismos[i].id+" ,Estado "+this._plazasTurismos[i].estado);
        }
        for(let i=0;i<this._plazasMotocicletas.length;i++){
            console.log("Plaza Para Motocicletas Id:"+this._plazasMotocicletas[i].id+" ,Estado "+this._plazasMotocicletas[i].estado);
        }
        for(let i=0;i<this._plazasCaravanas.length;i++){
            console.log("Plaza Para Caravanas Id:"+this._plazasCaravanas[i].id+" ,Estado "+this._plazasCaravanas[i].estado);
        }

    }

    asignarPlaza(newvehiculo){
        switch(newvehiculo.tipo){
            case "1":
                for(let i=0;i<this._plazasTurismos.length;i++){
                    if(this._plazasTurismos[i].estado=="libre"){
                        this._plazasTurismos[i].vehiculo=newvehiculo;
                        this._plazasTurismos[i].estado="OCUPADA";
                        break;
                    }
                }
                break;
            case "2":
                for(let i=0;i<this._plazasMotocicletas.length;i++){
                    if(this._plazasMotocicletas[i].estado=="libre"){
                        this._plazasMotocicletas[i].vehiculo=newvehiculo;
                        this._plazasMotocicletas[i].estado="OCUPADA";
                        break;
                    }
                }
                break;
            case "3":
                for(let i=0;i<this._plazasCaravanas.length;i++){
                    if(this._plazasCaravanas[i].estado=="libre"){
                        this._plazasCaravanas[i].vehiculo=newvehiculo;
                        this._plazasCaravanas[i].estado="OCUPADA";
                        break;
                    }
                }
                break;
        }
    }

    devolverPlaza(vehiculo){
        for(let i=0;i<this._plazasTurismos.length;i++){
            if(this._plazasTurismos[i].vehiculo==vehiculo){
                return this._plazasTurismos[i].id;
            }
        }
        for(let i=0;i<this._plazasMotocicletas.length;i++){
            if(this._plazasMotocicletas[i].vehiculo==vehiculo){
                return this._plazasMotocicletas[i].id;
            }
        }
        for(let i=0;i<this._plazasCaravanas.length;i++){
            if(this._plazasCaravanas[i].vehiculo==vehiculo){
                return this._plazasCaravanas[i].id;
            }
        }

    }


    retirarVehiculo(matricula,idPlaza,Pin){
        for(let i=0;i<this._plazasTurismos.length;i++){
            if(this._plazasTurismos[i].id==idPlaza){
                this._plazasTurismos[i].estado="Libre";
                let now=moment().format('mm');
                this._recaudacion+=parseInt(now)*0.12;
                return parseInt(now)*0.12;
            }
        }
        for(let i=0;i<this._plazasMotocicletas.length;i++){
            if(this._plazasMotocicletas[i].id==idPlaza){
                this._plazasMotocicletas[i].estado="Libre";
                let now=moment().format('mm');
                this._recaudacion+=parseInt(now)*0.08;
                return parseInt(now)*0.08;
            }
        }
        for(let i=0;i<this._plazasCaravanas.length;i++){
            if(this._plazasCaravanas[i].id==idPlaza){
               this._plazasCaravanas[i].estado="Libre";
               let now=moment().format('mm');
               this._recaudacion+=parseInt(now)*0.45;
               return parseInt(now)*0.45;
            }
        }
    }

    devolverFacturacion(){
        return this._recaudacion;
    }


    comprobarAbonado(dni){
        for(let i=0;i<this._listaClientes.length;i++){
            if(this._listaClientes[i].dni==dni){
                return true;
            }else{
                return false;
            }
        }
    }

    devolverCliente(dni){
        for(let i=0;i<this._listaClientes.length;i++){
            if(this._listaClientes[i].dni==dni){
                return this._listaClientes[i];
            }
        }
    }

    devolverPlazaCliente(cliente){
        return cliente.plaza;
    }

    depositarAbonado(plaza){
        for(let i=0;i<this._plazasTurismos.length;i++){
            if(this._plazasTurismos[i].id==plaza.id){
                this._plazasTurismos[i].estado="OCUPADO ABONADO";
            }
        }
        for(let i=0;i<this._plazasMotocicletas.length;i++){
            if(this._plazasMotocicletas[i].id==plaza.id){
                this._plazasMotocicletas[i].estado="OCUPADO ABONADO";
            }
        }
        for(let i=0;i<this._plazasCaravanas.length;i++){
            if(this._plazasCaravanas[i].id==plaza.id){
                this._plazasCaravanas[i].estado="OCUPADO ABONADO";
            }
        }

    }

    comprobarPlaza(idplaza){
        for(let i=0;i<this._plazasTurismos.length;i++){
            if(this._plazasTurismos[i].id==idplaza && this._plazasTurismos[i].estado=="OCUPADO ABONADO"){
                return true;
            }
        }
        for(let i=0;i<this._plazasMotocicletas.length;i++){
            if(this._plazasMotocicletas[i].id==idplaza && this._plazasMotocicletas[i].estado=="OCUPADO ABONADO"){
                return true;
            }
        }
        for(let i=0;i<this._plazasCaravanas.length;i++){
            if(this._plazasCaravanas[i].id==idplaza && this._plazasCaravanas[i].estado=="OCUPADO ABONADO"){
                return true;
            }
        }
    }

    retirarAbonado(matricula,idplaza,pin){
                for(let i=0;i<this._plazasTurismos.length;i++){
                    if(this._plazasTurismos[i].id==idplaza){
                        this._plazasTurismos[i].estado="RESERVADO";
                    }
                }
                for(let i=0;i<this._plazasMotocicletas.length;i++){
                    if(this._plazasMotocicletas[i].id==idplaza ){
                        this._plazasMotocicletas[i].estado="RESERVADO";
                    }
                }
                for(let i=0;i<this._plazasCaravanas.length;i++){
                    if(this._plazasCaravanas[i].id==idplaza){
                        this._plazasCaravanas[i].estado="RESERVADO";
                    }
                }
        

    }

    calcularFechaCaducidad(tipoAbono){
        switch(tipoAbono){
            case "1":
                let fechaCaducidad1=moment().add(1,'months').format('MM-DD-YYYY');
                this._recaudacionAbonados+=25;
                return fechaCaducidad1;
                break;
            case "2":
                let fechaCaducidad2=moment().add(3,'months').format('MM-DD-YYYY');
                this._recaudacionAbonados+=70;
                return fechaCaducidad2;
                break;
            case "3":
                let fechaCaducidad3=moment().add(6,'months').format('MM-DD-YYYY');
                this._recaudacionAbonados+=130;
                return fechaCaducidad3;
                break;
            case "4":
                let fechaCaducidad4=moment().add(12,'months').format('MM-DD-YYYY');
                this._recaudacionAbonados+=200;
                return fechaCaducidad4;
                break;
        }

    }

    listaAbonados(){
        for(let i=0;i<this._listaClientes.length;i++){
            console.log(this._listaClientes[i].nombre+" "+this._listaClientes[i].apellidos+" Abono:"+this._listaClientes[i].tipoabono+" FechaIn: "+this._listaClientes[i].fechaActivacionAbono+" FechaFin: "+this._listaClientes[i].fechaCaducidadAbono);
        }
    }

    consultaAbonados(){
        return this._recaudacionAbonados;
    }

    modificarAbonado(dni,nombre,apellidos,email){
        for(let i=0;i<this._listaClientes.length;i++){
            if(this._listaClientes[i].dni==dni){
                this._listaClientes[i].nombre=nombre;
                this._listaClientes[i].apellidos=apellidos;
                this._listaClientes[i].email=email;
            }
        }

    }

    eliminarAbonado(dni){
        for(let i=0;i<this._listaClientes.length;i++){
            if(this._listaClientes[i].dni==dni){
                this._listaClientes.splice(i,1);
            }
        }

    }

    caducidadMes(mes){
        for(let i=0;i<this._listaClientes.length;i++){
            if(this._listaClientes[i].fechaCaducidadAbono.format("MM")==mes){
                this._listaClientes[i];
            }
        }
    }

    



"""
