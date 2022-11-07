# Biblioteca-POO
Biblioteca POO

## Presentación
Bibliteca-POO es un proyecto presentado por la matería de programación orientado a objetos correspondiente a la institución: IFTS N° 4 ubicada en CABA, Buenos Aires Argentina.
Para el mismo se solicita crear una base de datos en mariaDB con dos tablas una de "Clientes" y otra de "Libros".
La programación debe ser en su totalidad utilizando el paradigma de POO y parte de un trabajo final del cuatrimestre pasado en el que se realizó el mismo ejercicio en programación estructurada con manejo de archivos. Utilizando dos archivos ".txt" como reemplazo  a base de datos.

# Para su uso:
Ejecutar archivo 17-biblioteca.py que es el que posee el acceso a toda la lógica.
Considerar que la base de datos está configurada en el puerto 4005, usuario root y sin contraseña. Si se está utilizando ese puerto en otro proyecto puede haber inconvenientes. Se recomienda cambiar el puerto en la configuración del archivo "Tablas" en el __init__ y en el metodo "conectarBaseDeDatos()"

# Funcionalidades princiaples.
El programa permite:

1- Consultar disponibilidad de libros: Imprime una tabla que puede llegar hasta 100 registros en donde muestra ISBN (Código de identificación del libro), título, autor, disponibilidad y en caso de no estar disponible el DNI del cliente al cual se encuentra prestado.

2- Prestamo de libro: Permite registrar prestamo y devolución. Es necesario para esto constatar que el ISBN del libro que se desea tomar en prestamo existe en la base de datos y que se encuentra disponible. Esto se puede ver en el menu de gestión de libro que desarrollaré en el punto 4. Las devoluciones deben ser hechas por el cliente que tomo el libro en prestamo ya que se evalúa que coincida el DNI ingresado con el guardado en cada registro que figure ocupado en la tabla de "Libros".
Cada cliente puede tener solo un libro en prestamo.

3- Gestión de cliente: Permite consultar el estado del cliente, registrar nuevo cliente, modificar cliente y eliminar cliente.
La consulta de cliente luego de ingresar un DNI valido y registrado nos mostrará: DNI, Nombre, Apellido, Telefono, Direccion y Disponibilidad.
                      
No se pueden crear clientes con un DNI que ya está registrado.
Modificar cliente solo permite cambiar el telefono y la dirección.
No se pueden eliminar clientes que poseen devoluciones pendientes para evitar inconsistencias.
  
4- Gestión libro: Permite consultar el estado del libro, registrar nuevo libro, modificar libro y eliminar libro.
La consulta de libro luego de ingresar un ISBN valido y registrado nos mostrará: ISBN ,TITULO ,AUTOR y DISPONIBILIDAD.

No se pueden crear libros con un ISBN que ya está registrado.
Modificar libro permite, luego de validar la existencia del ISBN, modificar el autor, el título o ambos.
No se pueden eliminar libros pendientes de devolución para evitar inconsistencias.

El menu pricipal se armo considerando que podría estar todo el tiempo abierto por lo cual una vez finalizada una tarea preguntará si "desea realizar algo más?" y al escribir que "SI" nos vuelve a mandar al menu de inicio y si se escribe "NO" el programa finaliza.
  
Muchas de las partes correspondientes a la estructura del programa poseen validaciones en cuanto a lo que son los parametros que recibe, por lo cual, cuando no se recibe uno deseado el programa nos avisará que no se ingreso un parametro valido y nos solicitará volver a intentarlo. Los invito a que si utilizan este programa desde su prespectiva me comenten que modificaciones les parecerían convenientes.


## Guía de Inicio
### Requisitos de Instalación.
- Requerimiento 1 : Debe tenerse instalado mariaDB y HeidiSQL recordar hacer la actualizacion desde "pip" para los paquetes de python, la configuracion en cuanto a lo que son las conexiones y el puerto utilizado se veran en el archivo de "Tablas", no se posee configuración de contraseña y el usuario es root. Se deben modificar los parámetros necesarios en el archivo tablas para llevar a cabo la correcta conexión.
- Requerimiento 2: Se utiliza la version de python 3.10.7, puede generar conflictos con versiones anteriores.

### Conocimientos requeridos.
- Conocimiento 1: Python.
- Conocimiento 2: Sql - mariaDB.
- Conocimiento 3: Editor de codigo VSC o similares.

### Procedimiento de Instalación.
- Procedimiento 1: Se necesita tener instalado Python en el ordenador V 3.10.7 o superior enlace: https://www.python.org/
- Procedimiento 2: Se debe instalar mariaDB enlace: https://mariadb.org/
- Procedimiento 3: Actualizar los paquetes correspondientes a mariadDB con PIP desde el path de python.
- Procedimiento 4: Realizar la configuracion correspondiente en el archivo "Tablas" para generar la conexión con la configuracion de base de datos.(Usuario,contaseña y puerto)
- Procedimiento 5: Ejecutar el archivo desde la terminal de python o desde la terminal de VSC con la configuración correspondiente para ejecutar archivos de python.


# Aspectos pendientes de mejora.
A continuación se definen aspectos que requieren tenerse en cuenta para próximas actualizaciones:
  - La clase OpcMenu debería permitir configurar la cantidad de opciones aparte del print para poder volverlo más dinamico.
  - Agregar opciones de salir en todos los menus para permitir salir en cualquier momento de una opción ingresada por error.
  - Configurar un alta masiva que permita decir cuantos clientes o libros se quieren dar de alta e ir almacenandonos en memoria para darlos de alta una vez finalizado el correcto ingreso
  
# Licencia de uso.
software libre no protegido con copyleft.
