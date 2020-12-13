eleccion=int;
eleccion2=int;
eleccion3=int;
passAdmin=1234;
pase=int;

print("Bienvenido al Parking robotizado")
while eleccion!=0:
    print("1 para entrar como Cliente")
    print("2 para entrar como Administrador")
    print("0 para salir")
    eleccion = input(int('¿Qué desea hacer?: '))

    if eleccion==1:
        while eleccion2!=0 :
            print("1 para depositar vehiculo")
            print("2 para retirar vehiculo")
            print("3 para depositar abonado")
            print("4 para retirar abonado")
            print("0 para salir")
            eleccion2 = input(int('¿Qué desea hacer? '))
            if eleccion2==1:

                break

            if eleccion2==2:

                break

            if eleccion2==3:
                break

            if eleccion2==4:
                break

            if eleccion2==0:
                break

    elif eleccion==2:
        pase=input(int("Introduzca contraseña de administrador: "))
        if(pase==passAdmin):
            while eleccion3!=0 :
                print("1 para ver el estado del parking")
                print("2 para ver la facturacion")
                print("3 para consultar abonados")
                print("4 añadir abonado")
                print("5 modificar abonado")
                print("6 borrar abonado")
                print("7 consultar caducidad")
                print("0 para salir")
                eleccion3 = input(int('¿Qué desea hacer? '))
                if eleccion3==1:
                    break
                elif eleccion3==2:
                    break
                elif eleccion3==3:
                    break
                elif eleccion3==4:
                    break
                elif eleccion3==5:
                    break
                elif eleccion3==6:
                    break
                elif eleccion3==7:
                    break
                elif eleccion3==0:
                    break
        else:
            print("No puedes pasar")
            break
    elif eleccion==0:
        break
print("Cerrando...")
