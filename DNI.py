from Tablas import Tablas
from ISBN import ISBN
import os

tabla = Tablas()
tabla.crearBase()
tabla.conectarBaseDeDatos()

class DNI (object):
    def __init__(self):
        self.ingresoStr = '\nIngrese el DNI del cliente: '
        self.ingresoInvalid = '\nEl DNI ingresado es invalido, pruebe con valores entre 10000000 y 9999999999999.'
        self.error = '\nDebe ingresar valores númericos.'
    def ingresoDni(self):
        dni=0
        while True:
            try:
                while dni<10000000 or len(str(dni))>13:
                    dni=int(input(self.ingresoStr))
                    if dni<10000000 or len(str(dni))>13:
                        os.system('cls')
                        print(self.ingresoInvalid)
                break
            except ValueError:
                print(self.error)
        return str(dni)
    def existeDni(self,dni):
        resultado = tabla.hacerConsulta('Clientes','DNI',dni)
        if type(resultado) == str:
            return False
        else:
            return True      
