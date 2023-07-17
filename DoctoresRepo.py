import cx_Oracle
import sys
class Doctor:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "netoracle", "localhost/XE")

    def mensajesString(self,cadena):
        dato = input(cadena)
        return dato

    def mensajesNumber(self,cadena):
        num = int(input(cadena))
        return num

    def alta(self):
        hos_cod = self.mensajesNumber("Introduzca hospital_cod: ")
        doc_cod = self.mensajesNumber("Introduzca doctor_cod: ")
        ape = self.mensajesString("Introduzca apellido: ")
        espe = self.mensajesString("Introduzca la especialidad: ")
        salario = self.mensajesString("Introduzca el salario: ")


        cursor = self.connection.cursor()
        try:
            # altaEnfermo = ("INSERT INTO enfermo "
            #                 "VALUES (:P1, :P2, :P3, to_date(:P4,'dd-mm-yyyy'), :P5, :P6)")
            data_docs = (hos_cod, doc_cod, ape, espe, salario)
            cursor.callproc('paquetedoctor.insertar', data_docs)

            if cursor.rowcount > 0:
                print("\n\nRegistro insertado satisfactoriamente")
            else:
                print("\n\nAlta no realizada")

        except:
            print(f"Error: {sys.exc_info()}")

    def eliminar(self):

        cod_d = self.mensajesNumber("Introduzca codigo doctor: ")

        cursor = self.connection.cursor()
        try:
            # bajaEnfermo = ("Delete from enfermo "
            #                "where nss=:P1")

            data_docs = (cod_d,)

            cursor.callproc('paquetedoctor.borrar', data_docs)

            if cursor.rowcount > 0:
                print("\n\nRegistro eliminado satisfactoriamente")
            else:
                print("\n\nDato no encontrado")

            # self.connection.commit()

        except:
            print(f"Error: {sys.exc_info()}")

    def modificar(self):

        cod_d = self.mensajesNumber("Introduzca el codigo del doctor: ")
        salario = self.mensajesString("Introduzca el nuevo salario: ")

        cursor = self.connection.cursor()
        try:
            # modificarEnfermo = ("Update enfermo "
            #                "set direccion=:P1 where nss=:P2")

            data_docs = (salario,cod_d)

            cursor.callproc('paquetedoctor.modificar', data_docs)

            if cursor.rowcount > 0:
                print("\n\nRegistro modificado satisfactoriamente")
            else:
                print("\n\nDato no encontrado")

            # self.connection.commit()

        except:
            print(f"Error: {sys.exc_info()}")

    def mostrar(self):

        cod_d = self.mensajesNumber("Introduzca el codigo del doctor: ")
        cursor = self.connection.cursor()
        try:
            mostrarDoc_query = ("select apellido ,especialidad from doctor where doctor_no = :P1")

            datos = (cod_d,)

            cursor.execute(mostrarDoc_query, datos)
            for v1, v2 in cursor:
                print("*******************************************************************")
                print("APELLIDO :",v1)
                print("ESPECIALIDAD",v2)


            if cursor.rowcount > 0:
                print("\n\nRegistro eliminado satisfactoriamente")
            else:
                print("\n\nDato no encontrado")

        except:
            print(f"Error: {sys.exc_info()}")


    def verHospital(self):

        cursor = self.connection.cursor()
        try:
            mostrar_query = ("select * from Hospital ")


            cursor.execute(mostrar_query)
            print("****************************SOY SINCERO Y LA 5 NO ME IBA A SALIR POR MI CUENTA***************************************")
            index = 0
            for v1, v2, v3, v4, v5 in cursor:
                index = index + 1
                print(f"************************ DATO NUMERO: {index} *****************************")
                print("hospital :", v1)
                print("nombre : ", v2)
                print("direccion :", v3)
                print("telf : ", v4)
                print("cama : ", v5)

            if cursor.rowcount > 0:
                print("\n\nRegistro eliminado satisfactoriamente")
            else:
                print("\n\nDato no encontrado")

        except:
            print(f"Error: {sys.exc_info()}")
