from Tablas import Tablas
from ISBN import ISBN
from DNI import DNI
import os

tabla = Tablas()
tabla.crearBase()
tabla.conectarBaseDeDatos()



class prestamoLibro(object):
    def __init__(self):
        menustr = ('''Ingreso a prestamo de libro:
    
    Opcion 1: Tabla de disponibilidad.
    Opcion 2: Registrar prestamo.
    Opcion 3: Registrar devolución.
    Opcion 4: Salir.''') 
    def disponibilidad(self):
        listaRegistros = []
        registros= tabla.cantidadDeRegistros('libros')
        for registro in registros:
            listaRegistros.append(list(registro))
        for elemento in listaRegistros:
            if elemento[3]=="O":
                elemento[3]="Ocupado"
            elif elemento[3]=="D":
                elemento[3]="Disponible" 
        tablaDisponibilidad = """\
            ---------------------- Se muestra un limite de 100 registros ----------------------
+------------------------------------------------------------------------------------------------------------------+
|     ISBN                   Titulo                           Autor               Disponibilidad     Cliente DNI   |
|------------------------------------------------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------------------------------------------------+\
"""
        tablaDisponibilidad = (tablaDisponibilidad.format('\n'.join("| {0:^13} |{1:^30} |{2:^30} |{3:^15}| {4:^15}  |".format(*fila)
 for fila in listaRegistros)))
        print(tablaDisponibilidad)
    def registrarPrestamo(self):
        isbn = ISBN()
        nuevoISBN = isbn.ingresoISBN()
        if isbn.existeISBN(nuevoISBN):
            registroLibro = tabla.hacerConsulta("libros","ISBN",nuevoISBN)
            if registroLibro[3] == "D":
                dni = DNI()
                nuevoDNI = dni.ingresoDni()
                if dni.existeDni(nuevoDNI):
                    registroCliente = tabla.hacerConsulta("Clientes","DNI",nuevoDNI)
                    if registroCliente[5] == "N":
                        os.system('cls')
                        confirma = input(f"""
                        ---  Se va a registrar el prestamo del libro:
                        ISBN: {registroLibro[0]}
                        Titulo: {registroLibro[1]}
                        Autor: {registroLibro[2]}
                        --------    A nombre del cliente:
                        DNI: {registroCliente[0]}
                        Nombre: {registroCliente[1]}
                        Apellido: {registroCliente[2]}
                        Ingrese "SI" para confirmar o cualquier otra cosa para cancelar: """).upper()
                        if confirma == "SI":
                            tabla.actualizarRegistros("Clientes","Prestados","O","DNI",registroCliente[0])
                            tabla.actualizarRegistros("Clientes","ISBN",registroLibro[0],"DNI",registroCliente[0])
                            tabla.actualizarRegistros("Libros","Disponibilidad","O","ISBN",registroLibro[0])
                            tabla.actualizarRegistros("Libros","DNI",registroCliente[0],"ISBN",registroLibro[0])
                            print("\nSe ha registrado el prestamo exitosamente.")
                        else:
                            print("\nSe canceló la operación.")
                    else:
                        print("\n El cliente seleccionado no se encuentra disponible, aún posee devoluciones pendientes.")
                else:
                    print(f"\nEl DNI: {nuevoDNI}, no corresponde a ningún cliente registrado.")

            else:
                print("\nEl libro seleccionado no se encuentra disponible, aún está pendiente de devolución.")
        else:
            print(f"\nEl ISBN: {nuevoISBN} no está regitrado en nuestra base de datos.")    
    def registrarDevolucion(self):
        isbn = ISBN()
        nuevoISBN = isbn.ingresoISBN()
        if isbn.existeISBN(nuevoISBN):
            registroLibro = tabla.hacerConsulta("libros","ISBN",nuevoISBN)
            if registroLibro[3] == "O":
                dni = DNI()
                nuevoDNI = dni.ingresoDni()
                if dni.existeDni(nuevoDNI):
                    registroCliente = tabla.hacerConsulta("Clientes","DNI",nuevoDNI)
                    if str(registroLibro[0]) == str(registroCliente[6]):
                        if registroCliente[5] == "O":
                            os.system('cls')
                            confirma = input(f"""
                        ---  Se va a registrar la devolución del libro:
                        ISBN: {registroLibro[0]}
                        Titulo: {registroLibro[1]}
                        Autor: {registroLibro[2]}
                        --------    A nombre del cliente:
                        DNI: {registroCliente[0]}
                        Nombre: {registroCliente[1]}
                        Apellido: {registroCliente[2]}
                        Ingrese "SI" para confirmar o cualquier otra cosa para cancelar: """).upper()
                            if confirma == "SI":
                                tabla.actualizarRegistros("Clientes","Prestados","N","DNI",registroCliente[0])
                                tabla.actualizarRegistros("Clientes","ISBN","N","DNI",registroCliente[0])
                                tabla.actualizarRegistros("Libros","Disponibilidad","D","ISBN",registroLibro[0])
                                tabla.actualizarRegistros("Libros","DNI","","ISBN",registroLibro[0])
                                print("\nSe ha registrado la devolución exitosamente.")
                            else:
                                print("\nSe canceló la operación.")
                        else:
                            print("\n El cliente seleccionado no posee devoluciones pendientes.")
                    else:
                        print("\nEl libro que se intenta devolver no figura en prestamo al cliente que intenta devolverlo.")
                else:
                    print(f"\nEl DNI: {nuevoDNI}, no corresponde a ningún cliente registrado.")

            else:
                print("\nEl libro seleccionado no está pendiente de devolución.")
        else:
            print(f"\nEl ISBN: {nuevoISBN} no está regitrado en nuestra base de datos.")    
        