from Tablas import Tablas


tabla = Tablas()
tabla.crearBase()
tabla.conectarBaseDeDatos()

class ISBN (object):
    def __init__(self):
        self.ingresoStr = '\nIngrese el ISBN correspondiente al titulo del libro: '
        self.ingresoInvalid = '\nPor favor ingrese un indice valido, El ISBN posee 13 números.'
        self.error = '\nDebe ingresar valores númericos.'
    def ingresoISBN(self):
        isbn=0
        while True:                                         
            try:
                while len(str(isbn))!=13:                                                              
                    isbn=int(input(self.ingresoStr))
                    if len(str(isbn))!=13:
                            print(self.ingresoInvalid)
                break
            except ValueError:
                print(self.error)
        return (isbn)
    def existeISBN(self,isbn):
        resultado = tabla.hacerConsulta('Libros','ISBN',isbn)
        if type(resultado) == str:
            return False
        else:
            return True  
    def devolverIsbn(self):
        isbn = int(input(self.ingresoStr))
        resultado = tabla.hacerConsulta('Libros','ISBN',isbn)
        return resultado