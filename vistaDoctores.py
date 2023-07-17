from DoctoresRepo import Doctor

doctor1 = Doctor()
valor = 0
while valor != 6:
    print("--- PULSA EN LA OPCIÓN ---\n")
    print("1.- ALTA DOCTOR\n")
    print("2.- ELIMINAR DOCTOR\n")
    print("3.- MODIFICAR SALARIO DOCTOR\n")
    print("4.- MOSTRAR APELLIDO Y ESPECIALIDAD DE UN DOCTOR\n")
    print("5.- MOSTRAR APELLIDO Y ESPECIALIDAD DE UN DOCTOR\n")
    print("6.- Salir \n")
    valor=int(input("Opción: "))
    if valor == 1:
        doctor1.alta()
    elif valor == 2:
        doctor1.eliminar()
    elif valor == 3:
        doctor1.modificar()
    elif valor == 4:
        print("entra al 4")
        doctor1.mostrar()
        #doctor1.modificar()
    elif valor == 5:
        doctor1.verHospital()
        print("entra al 5")
        #doctor1.modificar()

print("Hasta pronto!")