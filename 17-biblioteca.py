from gestionCliente import *
from gestionLibro import *
from OpcMenu import *
from prestamoLibro import *
from Tablas import *
import os



class menuBiblioteca(object):
    def __init__(self):
        self.tabla = Tablas()
        self.tabla.crearBase()
        self.tabla.conectarBaseDeDatos()
        self.tabla.clientesTabla()
        self.tabla.librosTabla()
        self.gestionCli = gestionCliente()
        self.gestionLi= gestionLibro()
        self.prestamoLi = prestamoLibro()
    def menuGeneral(self):
        imprimir = ('''
        ***       BIENVENIDO A BIBLIOTECA IFTSN°4        ***

Opcion 1: Consulta disponibilidad de libro.
Opcion 2: Prestamo de libro (Prestamo/Devolución).
Opcion 3: Gestión de cliente (Consulta/alta/Baja/Modificación).
Opcion 4: Gestión de libro (Consulta/alta/Baja/Modificación).''')
        if len(self.tabla.cantidadDeRegistros("Clientes")) > 1  or len(self.tabla.cantidadDeRegistros("Libros")) > 1 :
            opcmen = OpcMenu(imprimir)
            seleccion = opcmen.selMenu()
            if seleccion == 1:
                self.prestamoLi.disponibilidad()
            if seleccion == 2: 
                os.system('cls') 
                menuPrestamo = 0                                                       
                while True:                                                        
                    try:
                        while menuPrestamo < 1 or menuPrestamo > 3:                          
                            menuPrestamo = int(input(f'''\n
                            ---- Prestamo de Libro ----
                            Opcion 1: Registrar prestamo.
                            Opcion 2: Registrar devolución.
                            Opcion 3: Salir.
                            Ingrese en N° de la opcion deseada a realizar:  '''))  
                            if menuPrestamo < 1 or menuPrestamo > 3:
                                os.system('cls')                                               
                                print('\nPor favor ingrese un valor entre 1 y 3: \n')
                        break
                    except ValueError:
                        os.system('cls')                                                                                                                                         
                        print('\nPor favor ingrese un valor numerico.\n',self.menustr)
                if menuPrestamo == 1:
                    self.prestamoLi.registrarPrestamo()
                if menuPrestamo == 2:
                    self.prestamoLi.registrarDevolucion()
                if menuPrestamo == 3:
                    print("\nSe salió del menu de Prestamo de Libro")
            if seleccion == 3:
                imprimir = ('''
                    ---- Gestión de cliente ----
                Opcion 1: Consulta estado de cliente.
                Opcion 2: Registrar nuevo cliente.
                Opcion 3: Modificar cliente.
                Opcion 4: Eliminar cliente.
                ''')
                menGesCli = OpcMenu(imprimir)
                sel = menGesCli.selMenu()
                if sel == 1:
                    self.gestionCli.consultaCliente()
                if sel == 2:
                    self.gestionCli.altaCliente()
                if sel == 3:
                    self.gestionCli.modificarCliente()
                if sel == 4: 
                    self.gestionCli.eliminarCliente()    
            if seleccion == 4:
                imprimir = ('''
                    ---- Gestión de libro ----
                Opcion 1: Consulta estado de libro.
                Opcion 2: Registrar nuevo libro.
                Opcion 3: Modificar libro.
                Opcion 4: Eliminar libro.
                ''')
                menGesCli = OpcMenu(imprimir)
                sel = menGesCli.selMenu()
                if sel == 1:
                    self.gestionLi.consultaLibro()
                elif sel == 2:
                    self.gestionLi.altaLibro()
                elif sel == 3:
                    self.gestionLi.modificarLibro()
                else: 
                    self.gestionLi.eliminarLibro()
        elif len(self.tabla.cantidadDeRegistros("Clientes")) < 1 and len(self.tabla.cantidadDeRegistros("Libros")) < 1:
            altamasiva = ""
            while True:
                try:
                    while altamasiva!="si" and altamasiva!="no":
                        altamasiva = input("""\n
                        No se registran datos ni de clientes, ni de libros.
                        Desea generar alta masiva con valores genericos? si/no: """).lower()
                        if altamasiva!="si" and altamasiva!="no":
                            os.system('cls')
                            print('Por favor ingrese una opción.')
                    break
                except ValueError:
                    print('\nPor favor ingrese si o no, otro ingreso es invalido.')
            if altamasiva=="si":
                self.tabla.agregarValores()
                print("\nSe generaron valores en la base de datos.")
            else:
                print('\nSe salió de la opción de alta masiva.')
    def menuFinal(self):
        validar=""
        while True:
            try:
                while validar!="NO":
                    self.menuGeneral()
                    validar = input("\nDesea Realizar algo más? si/no: ").upper()
                    if validar!="SI" and validar!="NO":
                        print(f' Por favor ingrese Si o No.')
                    elif validar=="NO":
                        print("\nPrograma finalizado.")
                break
            except ValueError:
                print(f'Hubo un error en su ingreso.')


asd = menuBiblioteca()
asd.menuFinal()