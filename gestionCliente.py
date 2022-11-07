from DNI import DNI
from Tablas import Tablas
import os

tabla = Tablas()
tabla.crearBase()
tabla.conectarBaseDeDatos()


class gestionCliente(object):
    def crearCliente(self):
        nuevocliente = []
        os.system('cls')
        print("\nIngreso de nuevo cliente:")
        dni = DNI()
        nuevoDNI = dni.ingresoDni()
        if not dni.existeDni(nuevoDNI):
            nuevocliente.append(nuevoDNI)
            nombre = ""
            while True:
                try:
                    while len(nombre)<2 or len(nombre)>30:
                        nombre=input(f'\nIngrese el nombre del nuevo cliente: ')
                        if len(nombre)<2 or len(nombre)>30:
                            os.system('cls')
                            print('\nEl nombre debe tener desde 2 hasta un maximo de 30 caracteres.')
                    break
                except ValueError:
                    print('\nNombre invalido.')
            nombre=nombre.title()
            nuevocliente.append(str(nombre))
            apellido = ""
            while True:
                try:
                    while len(apellido)<2 or len(apellido)>30:
                        apellido=input(f'\nIngrese el apellido del nuevo cliente: ')
                        if len(apellido)<2 or len(apellido)>30:
                            os.system('cls')
                            print('\nEl apellido debe tener desde 2 hasta un maximo de 30 caracteres.')
                    break
                except ValueError:
                    print('\Apellido invalido.')
            apellido=apellido.title()
            nuevocliente.append(str(apellido))
            telefono = 0                           
            while True:
                try:
                    while 17<len(str(telefono)) or 10>len(str(telefono)):
                        telefono = int(input('\ningrese su teléfono anteponiendo el código de área (011): '))
                        if 17<len(str(telefono)) or 10>len(str(telefono)):
                            os.system('cls')
                            print('\nEl teléfono debe de 11 a 16 caracteres.')
                    break
                except ValueError:
                    print('\nteléfono solo acepta valor numéricos.')
            nuevocliente.append(str(telefono))                        
            calleEntera=""
            while True:
                try:
                    while len(calleEntera)<2 or len(calleEntera)>25:
                        calleEntera= input('\nIngrese el nombre de la calle de su domicilio: ')
                        if len(calleEntera)<2 or len(calleEntera)>25:
                            os.system('cls')
                            print('\nLa calle de su domicilio debe tener de 2 a 25 caracteres incluyendo espacios.')
                    break
                except ValueError:
                    print('\n Intentelo nuevamente')    
            calleEntera=calleEntera.title()
            altura = -1
            while True:
                try:
                    while altura<0 or altura>10000:
                        altura = int(input('\ningrese su altura de donde vive: '))
                        if altura<0 or altura>10000:
                            os.system('cls')
                            print('\nLa altura debe ser entre 0 y 10.000.')
                            altura=-1
                    break
                except ValueError:
                    print('\naltura solo acepta valor numéricos.')
            domicilio = calleEntera + " " + str(altura)
            nuevocliente.append(domicilio)
            final_lista = ["N","N"]
            nuevocliente.extend(final_lista)
        else:
            print("El DNI ingresado corresponde a un cliente que ya existe.")
        return nuevocliente
    def altaCliente(self):
        confirma =""
        while True:
            try:
                while confirma!= "SI" and confirma!="NO":
                    nuevocliente=self.crearCliente()
                    while len(nuevocliente)>1 and (confirma!= "SI" and confirma!="NO"):
                        confirma=input(f'''\nSe creará el cliente:
                        DNI: "{nuevocliente[0]}"
                        Nombre y Apellido: "{nuevocliente[1]}"
                        Teléfono: "{nuevocliente[2]}
                        Dirección: "{nuevocliente[3]}"
                        \n Confirmar?(si/no): ''').upper()
                        if confirma!= "SI" and confirma!="NO":
                            print('\n Por favor ingrese "si o no".')
                        if confirma == "SI":
                            tabla.agregarCliente(nuevocliente)
                            print('\n---  El cliente ha sido agregado exitosamente  --- \n---  Se salió del menu de gestion de cliente  ---') 
                    if confirma == "NO":
                        print(f'''\n 
                                --- Se canceló la operación ---
                          ---  Se salió del menu gestion cliente  --- ''')
                    if len(nuevocliente)<3:
                        break
                break
            except ValueError:
                print('\nSe ha producido un error, vuelva a intentarlo.') 
    def consultaCliente(self):
        print(" ----  Estado de clientes Biblioteca IFTSN°4  ----  ")
        dni = DNI()
        nuevoDNI = dni.ingresoDni()
        if dni.existeDni(nuevoDNI):
            clientePorConsola = tabla.hacerConsulta("Clientes","DNI",nuevoDNI) 
            if clientePorConsola[5] == "O":
                clientePorConsola[5]= "Posee libro en prestamo."
                print(f''' 
                      Dni: "{clientePorConsola[0]}"
                      Nombre: "{clientePorConsola[1]}"
                      Apeliido: "{clientePorConsola[2]}"
                      Telefono: "{clientePorConsola[3]}"
                      Direccion: "{clientePorConsola[4]}"
                      Disponibilidad: "{clientePorConsola[5]}"
                      Isbn:"{clientePorConsola[6]}"
                      ''')
            else:
                clientePorConsola[5]= " No posee devoluciones pendientes."
                print(f''' 
                      Dni: "{clientePorConsola[0]}"
                      Nombre: "{clientePorConsola[1]}"
                      Apellido: "{clientePorConsola[2]}"
                      Telefono: "{clientePorConsola[3]}"
                      Direccion: "{clientePorConsola[4]}"
                      Disponibilidad: "{clientePorConsola[5]}"
                      ''')
        else:
            print('\nEl dni ingresado no corresponde a un cliente registrado.') 
    def modificarCliente(self):
        print(" ---- Modificación de cliente ----  ")
        dni= DNI()
        nuevoDNI = dni.ingresoDni()
        if dni.existeDni(nuevoDNI):
            clienteamodificar = tabla.hacerConsulta("Clientes","DNI",nuevoDNI)
            telefono = 0                            
            while True:
                try:
                    while 16<len(str(telefono)) or 9>len(str(telefono)):
                        telefono = int(input('\ningrese su nuevo telefono: '))
                        if 16<len(str(telefono)) or 9>len(str(telefono)):
                            print('\nEl telefono debe tener mas de 8 numeros y hasta 15 numeros.')
                    break
                except ValueError:
                    print('\ntelefono solo acepta valor numericos.')
            clienteamodificar[3]= int(telefono)
            calleComp=[]
            calleEntera=""
            while True:
                try:
                    while 3>len(calleEntera) or 25<len(calleEntera):
                        calleEntera=input(f'\nIngrese la calle en correspondiente a su domicilio: ')
                        calleComp=calleEntera.split()
                        if 3>len(calleEntera) or 25<len(calleEntera):
                            print('\nLa calle de su dirección debe tener desde 3 hasta un maximo de 24 caracteres.')
                        if len(calleComp)==0:
                            print('\nPor favor solo ingrese al menos un campo.')
                            calleEntera=""
                        else:
                            for elemento in range(0,len(calleComp),1):
                                if calleComp[elemento].isalpha() == False:
                                    print(f'\nLa dirección solo acepta letras y espacios: {calleComp[elemento]} - No es valido.')
                                    calleEntera=""
                    break
                except ValueError:
                    print('\nNombre invalido.')
            calleEntera=calleEntera.title()
            altura = -1
            while True:
                try:
                    while altura<0 or altura>10000:
                        altura = int(input('\ningrese su altura de donde vive: '))
                        if altura<0 or altura>10000:
                            print('\nLa altura debe ser entre 0 y 10.000.')
                    break
                except ValueError:
                    print('\naltura solo acepta valor numericos.')
            domicilio = calleEntera + " " + str(altura)
            clienteamodificar[4]= str(domicilio)
            tabla.actualizarRegistros("Clientes","Telefono",clienteamodificar[3],"DNI",nuevoDNI)            
            tabla.actualizarRegistros("Clientes","Direccion",clienteamodificar[4],"DNI",nuevoDNI)
            print(f'''\nSe ha modificado el cliente "{clienteamodificar[1]}" exitosamente:
            Teléfono: "{clienteamodificar[3]}"
            Dirección: "{clienteamodificar[4]}"
            ''')
        else:
            print('\nEl dni ingresado no corresponde a un cliente registrado.') 
    def eliminarCliente(self):
        dni = DNI() 
        nuevoDNI = dni.ingresoDni()
        if dni.existeDni(nuevoDNI):
            clienteAEliminar = tabla.hacerConsulta("Clientes","DNI",nuevoDNI)
            if clienteAEliminar[5]!="O":
                validar=""
                while True:
                    try:
                        while validar!="SI" and validar!="NO":
                            validar=input(f'''\nSe va a eliminar el cliente:
                        DNI: "{clienteAEliminar[0]}"
                        Nombre: "{clienteAEliminar[1]}"
                        Apellido: "{clienteAEliminar[2]}"
                        Teléfono: "{clienteAEliminar[3]}"
                        Dirección: "{clienteAEliminar[4]}"
                        \nConfirma (Si/No): ''').upper()
                            if validar!="SI" and validar!="NO":
                                os.system('cls')
                                print(f'\nPor favor ingrese Si o No.')
                            if validar=="SI":
                                tabla.borrarRegistro("Clientes","DNI",clienteAEliminar[0])
                                print('\n---- El cliente ha sido borrado exitosamente ----')        
                            elif validar=="NO":
                                print('''\n
                                    -----  Se canceló la operación.  ----- 
                                -----  Se salió del menu gestión de cliente ----- ''')
                        break
                    except ValueError:
                        print(f'Hubo un error en su ingreso.')
            else:
                print('''\n
                 El cliente seleccionado tiene devoluciones pendientes.
                 ----  Se salió del menu de gestión de clientes. ----- ''')
        else:
            print('''\n
              El DNI ingresado no corresponde a ningun cliente.
            ----  Se salió del menu de gestión de clientes. ----- ''')
