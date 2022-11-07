import mariadb

class Tablas(object):
    def __init__(self):
        self.bd = mariadb.connect(
        host="localhost",
        port=4005,
        user="root",
        password="",
        autocommit=True
        )
        self.cursor = self.bd.cursor()
    def crearBase(self):
        try:
            self.cursor.execute("CREATE DATABASE Biblioteca")
        except mariadb.Error:
            return(f"\nLa base de datos Biblioteca, ya habia sido creada.")
    def conectarBaseDeDatos(self):
        self.bd =mariadb.connect(
        host="localhost",
        port=4005,
        user="root",
        password="",
        db = "Biblioteca"
        )
        self.cursor = self.bd.cursor()
    def clientesTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Clientes(DNI INT PRIMARY KEY,Nombre VARCHAR(255),Apellido VARCHAR(255),Telefono INT, Direccion VARCHAR(255),Prestados VARCHAR(150),ISBN VARCHAR(255))")
    def librosTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Libros(ISBN BIGINT PRIMARY KEY,Libro VARCHAR(255),Autor VARCHAR(255),Disponibilidad VARCHAR(150),DNI VARCHAR(255))")
    def agregarValores(self):
        sql = "INSERT INTO Clientes (DNI, Nombre, Apellido, Telefono, Direccion, Prestados, ISBN) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = [
            (40123033,'Antonella', 'Lopez',1512345678,'Superi 1111','N','N'),
            (38526847,'Camila', 'Gomez',1599887766,'Superi 1111','N','N'),
            (35554845,'Laura', 'Diaz',1522334455,'Cabildo 3333','N','N'),
            (36345584,'Luis', 'Ruiz',1154585978,'Juramento 1300','O','1234567891234'),
            ]
        self.cursor.executemany(sql,val)
        self.bd.commit()
        sql = "INSERT INTO Libros (ISBN, Libro, Autor, Disponibilidad, DNI) VALUES (%s, %s, %s, %s, %s)"
        val = [
            (9786123032166,'FRIDA KAHLO','Frida Kahlo','D',''),
            (9786123032562,'LO MEJOR DE CONDORITO','Alberto Briceo','D',''),
            (9786124013737,'MAFALDA','quino caloi','D',''),
            (1234567891234,'PARQUE JURASICO','Espilbergo','O','36345584')
        ]
        self.cursor.executemany(sql,val)
        self.bd.commit()
    def agregarCliente(self,val):
        sql = "INSERT INTO Clientes (DNI, Nombre, Apellido, Telefono, Direccion, Prestados, ISBN) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql,val)
        self.bd.commit()
    def agregarLibro(self,val):
        sql = "INSERT INTO Libros (ISBN, Libro, Autor, Disponibilidad, DNI) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql,val)
        self.bd.commit()
    def verTablaClientes(self):
        self.cursor.execute("SELECT DNI FROM Clientes")
        dni_clientes=[]
        for ind in self.cursor:
            dni_clientes.append(ind)
        if len(dni_clientes) > 0:
            return True
        else:
            return False
    def verTablaLibros(self):
        self.cursor.execute("SELECT ISBN FROM Libros")
        isbn_libros=[]
        for ind in self.cursor:
            isbn_libros.append(ind)
        if len(isbn_libros)> 0:
            return True
        else:
            return False
    def hacerConsulta(self,tabla,campo,dato):
        self.cursor.execute(f"SELECT * FROM {tabla} where {campo} = {dato}")
        resultado = self.cursor.fetchone()
        if not (resultado) is None:
            listaResultado = []
            for registro in resultado:
                listaResultado.append(registro)
            return listaResultado
        else:
            return("\nNo hay registros para el dato consultado.")
    def cantidadDeRegistros(self,tabla):
        self.cursor.execute(f"SELECT * FROM {tabla} LIMIT 100")
        registros = self.cursor.fetchall()
        return(registros)
    def actualizarRegistros(self,tabla,campo,datomodificado,campoID,regId):
        self.cursor.execute(f"UPDATE {tabla} SET {campo} = '{datomodificado}' WHERE {campoID} = {regId}")
        self.bd.commit()
    def borrarRegistro(self,tabla,campo,condicion):
        sql = f"DELETE FROM {tabla} WHERE {campo} LIKE '%{condicion}%'"
        self.cursor.execute(sql)
        self.bd.commit()

