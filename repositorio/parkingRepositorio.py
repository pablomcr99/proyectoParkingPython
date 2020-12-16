from modelos.Parking import Parking
from modelos.Plaza import Plaza
from modelos.Cliente import Cliente
from modelos.Vehiculo import Vehiculo
from datetime import datetime,timedelta
from io import open
import pickle


plazat1= Plaza(1,"libre",None)
plazat2= Plaza(2,"libre",None)
plazat3= Plaza(3,"libre",None)
plazat4= Plaza(4,"libre",None)
plazat5= Plaza(5,"libre",None)
plazat6= Plaza(6,"libre",None)
plazat7= Plaza(7,"libre",None)
plazat8= Plaza(8,"libre",None)
plazat9= Plaza(9,"libre",None)
plazat10= Plaza(10,"libre",None)
plazat11= Plaza(11,"libre",None)
plazat12= Plaza(12,"libre",None)
plazat13= Plaza(13,"libre",None)
plazat14= Plaza(14,"libre",None)
plazat15= Plaza(15,"libre",None)

plazas_turismos=[plazat1,plazat2,plazat3,plazat4,plazat5,plazat6,plazat7,plazat8,plazat9,plazat10,plazat11
,plazat12,plazat13,plazat14,plazat15]

plazam1= Plaza(16,"libre",None)
plazam2= Plaza(17,"libre",None)
plazam3= Plaza(18,"libre",None)
plazam4= Plaza(19,"libre",None)
plazam5= Plaza(20,"libre",None)
plazam6= Plaza(21,"libre",None)
plazam7= Plaza(22,"libre",None)
plazam8= Plaza(23,"libre",None)
plazam9= Plaza(24,"libre",None)
plazam10= Plaza(25,"libre",None)
plazam11= Plaza(26,"libre",None)
plazam12= Plaza(27,"libre",None)
plazam13= Plaza(28,"libre",None)
plazam14= Plaza(29,"libre",None)
plazam15= Plaza(30,"libre",None)

plazas_motocicletas=[plazam1,plazam2,plazam3,plazam4,plazam5,plazam6,plazam7,plazam8,plazam9,plazam10,plazam11
    ,plazam12,plazam13,plazam14,plazam15]

plazac1= Plaza(31,"libre",None)
plazac2= Plaza(32,"libre",None)
plazac3= Plaza(33,"libre",None)
plazac4= Plaza(34,"libre",None)
plazac5= Plaza(35,"libre",None)
plazac6= Plaza(36,"libre",None)
plazac7= Plaza(37,"libre",None)
plazac8= Plaza(38,"libre",None)
plazac9= Plaza(39,"libre",None)
plazac10= Plaza(40,"libre",None)
plazac11= Plaza(41,"libre",None)
plazac12= Plaza(42,"libre",None)
plazac13= Plaza(43,"libre",None)
plazac14= Plaza(44,"libre",None)
plazac15= Plaza(45,"libre",None)

plazas_caravanas=[plazac1,plazac2,plazac3,plazac4,plazac5,plazac6,plazac7,plazac8,plazac9,plazac10,plazac11
    ,plazac12,plazac13,plazac14,plazac15]


vehiculo=Vehiculo("6459",3)
fechaActiv=datetime.now()
fechaFinal=fechaActiv+timedelta(days=30)


cliente1=Cliente("11111111A","Pablo","Mancina Castro",7141,1,"pablomancina@gmail.com",vehiculo,plazac14,789456,fechaActiv,fechaFinal);

lista_clientes=[cliente1];


parking_proyecto= Parking(plazas_turismos,plazas_motocicletas,plazas_caravanas,lista_clientes,None,None)


fichero = open('../ficheros/parking.pckl','wb')

pickle.dump(parking_proyecto,fichero)

fichero.close()
