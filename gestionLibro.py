from ISBN import ISBN
from OpcMenu import OpcMenu
from Tablas import Tablas
import os

tabla = Tablas()
tabla.crearBase()
tabla.conectarBaseDeDatos()


class gestionLibro(object):
    def altaLibro(self):
        os.system('cls')
        nuevoLibro = []
        print(f'               INGRESO DE UN NUEVO LIBRO.')
        isbn = ISBN()
        nuevoISBN = isbn.ingresoISBN()
        if not isbn.existeISBN(nuevoISBN):
            nuevoLibro.append(nuevoISBN)
            print("-"*20, " * ", "-"*20)
            print("")
            nombreL = ""
            while True:
                try:
                    while len(nombreL)<1 or len(nombreL)>30:
                        nombreL = input("\nIngrese Nombre del libro: ").upper()
                        if len(nombreL)<1 or len(nombreL)>30:
                            print("\nPor favor, ingrese caracteres entre 1 y 30 contando los espacios.")
                    break
                except ValueError:
                    print("\nUsted a ingresado un nombre invalido.")
            nuevoLibro.append(nombreL)
            print("-"*20, " * ", "-"*20)
            print("")
            nombreAutor =""
            while True:
                try:
                    while len(nombreAutor)<1 or len(nombreAutor)>30:
                        nombreAutor = input("\nIngrese el Autor: ").title()
                        if len(nombreAutor)<1 or len(nombreAutor)>30:
                            print("\nEl Nombre del autor debe tener de 1 a 30 caracteres.")
                    break
                except ValueError:
                    print("\nUsted a hecho un ingreso invalido.")
            nuevoLibro.append(nombreAutor)
            print("-"*20, " * ", "-"*20)
            print("")
            nuevoLibro.extend(["D",""])
            validar=""
            while True:
                try:
                    while validar!="SI" and validar!="NO":
                        validar=input(f'''\nSe va a dar de alta el libro:
                            ISBN: {nuevoLibro[0]}
                            Titulo: {nuevoLibro[1]}
                            AUTOR: {nuevoLibro[2]}
                            \nConfirma (Si/No): ''').upper()
                        if validar!="SI" and validar!="NO":
                            os.system('cls')
                            print(f' Por favor ingrese Si o No.')
                        if validar=="SI":
                            tabla.agregarLibro(nuevoLibro)
                            print('\n---- El libro ha sido creado exitosamente ----')
                        elif validar=="NO":
                            print('\n ---  Se anulo la operación  --- ')
                    break
                except ValueError:
                    print(f'Hubo un error en su ingreso.')	
        else:
            print("\nEl ISBN corresponde a un título ya registrado.")
    def consultaLibro(self):
        os.system('cls')
        print(f'\n                       "CONSULTA DE LIBRO".\n')
        isbn = ISBN()
        nuevoISBN = isbn.ingresoISBN()
        if isbn.existeISBN(nuevoISBN):
            libroconsultado = tabla.hacerConsulta("Libros","ISBN",nuevoISBN)
            if libroconsultado[3] == "O":
                libroconsultado[3] = "Ocupado"
                print(f"""
                ISBN: {libroconsultado[0]}
                TITULO: {libroconsultado[1]}
                AUTOR: {libroconsultado[2]}
                DISPONIBILIDAD: {libroconsultado[3]}
                DNI.Cliente: {libroconsultado[4]} """)
            else:
                libroconsultado[3] = 'disponible'
                print(f"""
                ISBN: {libroconsultado[0]}
                TITULO: {libroconsultado[1]}
                AUTOR: {libroconsultado[2]}
                DISPONIBILIDAD: {libroconsultado[3]}""")
        else:
            print("\nEl ISBN no se registra en la base de datos.")
        
        print('\n            ---  Se salió del menu de gestión de libro  --- ')
    def modificarLibro(self):
        os.system('cls')
        print(f'                      "MODIFICAR LIBRO".\n')
        libromodificar = []
        isbn = ISBN()
        nuevoISBN = isbn.ingresoISBN()
        if isbn.existeISBN(nuevoISBN):
            libromodificar = tabla.hacerConsulta("Libros","ISBN",nuevoISBN)
        if len(libromodificar) >1:
            paraImprimir = (f'''
            opción 1: Modificar titulo "{libromodificar[1]}"
            opción 2: Modificar autor "{libromodificar[2]}"
            opción 3: Modificar ambas "(titulo y autor)"
            opción 4: salir ''')
            menu = OpcMenu(paraImprimir)
            sel= menu.selMenu()
            if sel == 1:
                nuevotitulo = ""
                while True:
                    try:
                        while len(nuevotitulo)<1 or len(nuevotitulo)>30:
                            nuevotitulo = input("\nIngrese el titulo nuevo: ").upper()
                            if len(nuevotitulo)<1 or len(nuevotitulo)>30:
                                print("\nEl nuevo titulo debe tener entre 1 y 30")
                        break
                    except ValueError:
                        print("\nDebe ingresar los parametros solicitados.")
                libromodificar[1] = nuevotitulo
                validar=""
                while True:
                    try:
                        while validar!="SI" and validar!="NO":
                            validar=input(f'''\nSe Modificara Titulo del libro:
                                Titulo: "{libromodificar[1]}"
                                \nConfirma (Si/No): ''').upper()
                            if validar!="SI" and validar!="NO":
                                os.system('cls')
                                print(f' Por favor ingrese Si o No.')
                            if validar=="SI":
                                tabla.actualizarRegistros("Libros","Libro",libromodificar[1],"ISBN",libromodificar[0])
                                print('\n    --- Se modificaron los registros exitosamente ---')
                            elif validar=="NO":
                                print('\n           --- Se cancelo la modificación --- ')
                        break
                    except ValueError:
                        print(f'Hubo un error en su ingreso.')
            if sel == 2:
                nuevoautor = ""
                while True:
                    try:
                        while len(nuevoautor)<1 or len(nuevoautor)>30:
                            nuevoautor = input("\nIngrese autor nuevo: ")
                            if len(nuevoautor)<1 or len(nuevoautor)>30:
                                print("\nEl nuevo autor debe tener entre 1 y 30")
                        break
                    except ValueError:
                        print("\nDebe ingresar los parametros solicitados.")
                libromodificar[2] = nuevoautor
                validar=""
                while True:
                    try:
                        while validar!="SI" and validar!="NO":
                            validar=input(f'''\nSe Modificará el autor del libro "{libromodificar[1]}":
                                Autor: "{libromodificar[2]}"
                                \nConfirma (Si/No): ''').upper()
                            if validar!="SI" and validar!="NO":
                                os.system('cls')
                                print(f'\nPor favor ingrese Si o No.')
                            if validar=="SI":
                                tabla.actualizarRegistros("Libros","Autor",libromodificar[2],"ISBN",libromodificar[0])
                                print('\n    --- Se modificaron los registros exitosamente ---')
                            elif validar=="NO":
                                print('\n           --- Se cancelo la modificación --- ')
                        break
                    except ValueError:
                        print(f'Hubo un error en su ingreso.')
            if sel == 3:
                nuevotitulo = ""
                while True:
                    try:
                        while len(nuevotitulo)<1 or len(nuevotitulo)>30:
                            nuevotitulo = input("\nIngrese el titulo nuevo: ").upper()
                            if len(nuevotitulo)<1 or len(nuevotitulo)>30:
                                print("\nEl nuevo titulo debe tener entre 1 y 30")
                        break
                    except ValueError:
                        print("\nDebe ingresar los parametros solicitados.")
                libromodificar[1] = nuevotitulo
                nuevoautor = ""
                while True:
                    try:
                        while len(nuevoautor)<1 or len(nuevoautor)>30:
                            nuevoautor = input("\nIngrese autor nuevo: ").title()
                            if len(nuevoautor)<1 or len(nuevoautor)>30:
                                print("\nEl nuevo autor debe tener entre 1 y 30")
                        break
                    except ValueError:
                        print("\nDebe ingresar los parametros solicitados.")
                libromodificar[2] = nuevoautor
                validar=""
                while True:
                    try:
                        while validar!="SI" and validar!="NO":
                            validar=input(f'''\nSe Modificará el autor y el titulo del libro ISBN: "{libromodificar[0]}":
                    Titulo: "{libromodificar[1]}"
                    Autor: "{libromodificar[2]}"
                    \nConfirma (Si/No): ''').upper()
                            if validar!="SI" and validar!="NO":
                                os.system('cls')
                                print(f'\nPor favor ingrese Si o No.')
                            if validar=="SI":
                                tabla.actualizarRegistros("Libros","Libro",libromodificar[1],"ISBN",libromodificar[0])
                                tabla.actualizarRegistros("Libros","Autor",libromodificar[2],"ISBN",libromodificar[0])   
                                print('\n    --- Se modificaron los registros exitosamente ---')
                            elif validar=="NO":
                                print('\n           --- Se cancelo la modificación --- ')
                        break
                    except ValueError:
                        print(f'Hubo un error en su ingreso.')
            else:
                print("\n      --- Se salió modificación de libros --- ")
        else:
            print("\nEl ISBN ingresado no se registra en nuestra base de datos.")
    def eliminarLibro(self):
        print(f'               "ELIMINAR LIBRO".')
        isbn = ISBN()
        libroexistente = []
        nuevoISBN = isbn.ingresoISBN()
        if isbn.existeISBN(nuevoISBN):
            libroexistente = tabla.hacerConsulta("Libros","ISBN",nuevoISBN)
        if len(libroexistente)>1:
            if libroexistente[3] != "O":
                validar=""
                while True:
                    try:
                        while validar!="SI" and validar!="NO":
                            validar=input(f'''\nSe Borrará el libro:
                        ISBN: "{libroexistente[0]}"
                        Titulo: "{libroexistente[1]}"
                        Autor: "{libroexistente[2]}"
                        \nConfirma (Si/No): ''').upper()
                            if validar!="SI" and validar!="NO":
                                os.system('cls')
                                print(f'\n Por favor ingrese Si o No.')
                            if validar=="SI":
                                tabla.borrarRegistro("Libros","ISBN",libroexistente[0])
                                print('\n    --- Se modificaron los registros exitosamente ---')
                            elif validar=="NO":
                                print('\n           --- Se cancelo la operación --- ')
                        break
                    except ValueError:
                        print(f'\nHubo un error en su ingreso.')
            else:
                print("\nEl libro que intenta seleccionar está pendiente de devolución. 'NO PUEDE SER ELIMINADO'.")
        else:
            print("\nEl Libro ingresado no se encuentra en nuestra base de datos.")	
    