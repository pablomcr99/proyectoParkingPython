# Proyecto Python Pablo Mancina Castro.
## Parking automatizado(sí, otra vez)
Este proyecto Python simula un Parking automatizado, este consta de dos zonas una para los clientes, y otra para los administradores, está inicializado con 35 plazas para turismos,7 para motocicletas y otras 7 para movilidad reducida, a continuación explico las funcionalidades con más detalle:
### Zona Cliente
- En la zona cliente de la aplicacion tenemos la posibilidad de depositar un vehiculo , para ello introduciremos la opción 1 donde se nos informara de las plazas disponibles de cada tipo(turismos, motocicletas, caravanas), el sistema asigna una plaza para el vehiculo del cliente de entre las que se encuentran disponibles habiendo este dedicado datos sobre su vehiculo, tras esto se imprime un Ticket para poder pasar a retirar el vehiculo mas Tarde.
- Tras depositar el vehiculo y con el ticket en posesion el cliente indica el Pin de este más los datos sobre su vehiculo y plaza asignada y el sistema devuelve el vehiculo, deja la plaza libre y procede a sumar a su recaudacion lo generado dependiendo de los minutos que el vehiculo ha sido depositado.
- Depositar el vehiculo como abonado, los clientes abonados podrán depositar su vehiculo aportando una serie de datos personales, estos clientes además tienen una plaza propia reservada para ellos dependiendo de su vehiculo, a estos no se le realizan cobros ya que estos clientes ya pagan con sus abonos, la plaza quedara como ABONO OCUPADA.
- Retirar el vehiculo Abonado: el cliente abonado vuelve a introducir datos personales con los que se procede a retirar su vehiculo si este se encuentra en el parking.

### Zona Administrador
Para entrar a la zona de administracion necesitamos una contraseña de administrador, en este caso 1234, en esta zona tenemos las siguientes funcionalidades:
- Mostrar todas las plazas con su estado.
- Ver la facturacion, sacada de los datos de los clientes no abonados que han usado el servicio.
- Consultar abonados, esta opción nos permite ver la lista de abonados actuales y la cantidad total recaudada.
- Añadir un abonado, añadimos así un nuevo cliente con sus datos personales y el tipo de abono que determina el tiempo que va a poder utilizar el servicio, al añadir el abonado también se debe aportar los datos de su vehiculo y se le asignará una plaza de entre las disponibles.
- Modificar abonado, podremos modificar una serie de datos del abonado introduciendo su Dni.
- Eliminar abonado, introduciendo tambien el dni igual que en la funcionalidad anterior, sus datos de facturacion de los abonos no serán eliminados.
- El administrador podrá también elegir el número de plazas totales con las cuales el programa genera un nuevo parking cuyas plazas serán un 70% para turismos, un 15% para motocicletas y el 15% restante para vehiculos de mov reducida
