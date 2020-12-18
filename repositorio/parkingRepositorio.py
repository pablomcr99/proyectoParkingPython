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
plazat16= Plaza(16,"libre",None)
plazat17= Plaza(17,"libre",None)
plazat18= Plaza(18,"libre",None)
plazat19= Plaza(19,"libre",None)
plazat20= Plaza(20,"libre",None)
plazat21= Plaza(21,"libre",None)
plazat22= Plaza(22,"libre",None)
plazat23= Plaza(23,"libre",None)
plazat24= Plaza(24,"libre",None)
plazat25= Plaza(25,"libre",None)
plazat26= Plaza(26,"libre",None)
plazat27= Plaza(27,"libre",None)
plazat28= Plaza(28,"libre",None)
plazat29= Plaza(29,"libre",None)
plazat30= Plaza(30,"libre",None)
plazat31= Plaza(31,"libre",None)
plazat32= Plaza(32,"libre",None)
plazat33= Plaza(33,"libre",None)
plazat34= Plaza(34,"libre",None)
plazat35= Plaza(35,"libre",None)

plazas_turismos=[plazat1,plazat2,plazat3,plazat4,plazat5,plazat6,plazat7,plazat8,plazat9,plazat10,plazat11
,plazat12,plazat13,plazat14,plazat15,plazat16,plazat17,plazat18,plazat19,plazat20,plazat21,plazat22,plazat23,
                 plazat24,plazat25,plazat26,plazat27,plazat28,plazat29,plazat30,plazat31,plazat32,plazat33,
                 plazat34,plazat35]


plazam1= Plaza(36,"libre",None)
plazam2= Plaza(37,"libre",None)
plazam3= Plaza(38,"libre",None)
plazam4= Plaza(39,"libre",None)
plazam5= Plaza(40,"libre",None)
plazam6= Plaza(41,"libre",None)
plazam7= Plaza(42,"libre",None)

plazas_motocicletas=[plazam1,plazam2,plazam3,plazam4,plazam5,plazam6,plazam7]


plazamr1= Plaza(43,"libre",None)
plazamr2= Plaza(44,"libre",None)
plazamr3= Plaza(45,"libre",None)
plazamr4= Plaza(46,"libre",None)
plazamr5= Plaza(47,"libre",None)
plazamr6= Plaza(48,"libre",None)
plazamr7= Plaza(49,"libre",None)

plazas_mov_red=[plazamr1,plazamr2,plazamr3,plazamr4,plazamr5,plazamr6,plazamr7]


vehiculo=Vehiculo("6459",3)
fechaActiv=datetime.now()
fechaFinal=fechaActiv+timedelta(days=30)


cliente1=Cliente("11111111A","Pablo","Mancina Castro",7141,1,"pablomancina@gmail.com",vehiculo,plazat14,789456,fechaActiv,fechaFinal)

lista_clientes=[cliente1]

f= open('../ficheros/lista_clientes.pckl','wb')

pickle.dump(lista_clientes,f)

f.close()

f= open('../ficheros/lista_clientes.pckl','rb')
clientes = pickle.load(f)
f.close()


parking_proyecto= Parking(plazas_turismos,plazas_motocicletas,plazas_mov_red,clientes,None,None)

parking_proyecto.recaudacion=100
parking_proyecto.recaudacion_abonados=25

f2=open('../ficheros/recaudacion.pckl','wb')
pickle.dump(parking_proyecto.recaudacion_abonados,f2)
f2.close()


fichero = open('../ficheros/parking.pckl','wb')

pickle.dump(parking_proyecto,fichero)

fichero.close()
