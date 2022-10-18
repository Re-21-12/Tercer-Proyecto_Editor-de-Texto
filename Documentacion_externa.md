# __Tercer Proyecto__ 
## ___Victor Macario 7690-22-5042___
***
## __[GitHub]__
>[Repositorio en GitHub](https://github.com/Re-21-12/Tercer-Proyecto_Editor-de-Texto)
[![imagen_screen](WhatsApp%20Image%202022-10-17%20at%2010.44.03%20PM.jpeg)](https://github.com/Re-21-12/Tercer-Proyecto_Editor-de-Texto "captura_de_git")
## ___Video___
>[Video en YouTube](https://www.youtube.com/watch?v=sdogOLSP0M0&t=8s&ab_channel=VictorMacario)
[![imagen_screen](WhatsApp%20Image%202022-10-17%20at%2010.42.02%20PM.jpeg)](https://www.youtube.com/watch?v=sdogOLSP0M0&t=8s&ab_channel=VictorMacario "captura_de_Video")
# ___Documentacion Externa___
## ___Editor de texto en Python___
## Librerias
- FileType 
- Tkinter
- webbrowser
    ~~~
    import webview
    from argparse import FileType
    from tkinter import *
    from tkinter import filedialog as Fd
    ~~~
- __Fyletype__ Se usa para indicar la extension del archivo a traves de su tamaño en el buffer.
- __Tkinter__ Es una binging de la biblioteca grafica que viene integrado en la instalacion de Microsoft Windos propiamente utilizada en Python.
- __Tkinter-filedialog__ Es utilizada para la gestion y manejo de archivos en python a partir de sus extensiones, clases y funciones para la implementacion a traves de una interfaz grafica configurable para  establecer herramientas utiles.
- __webbrowser__ usa una funcion que habre una url en el buscador por defecto del sistema.
***  
## **_Funciones_**
### __Funciones para gestion de archivos__
Funciones utilizadas para la realizacion del programa:
1. nuevo
   - Primero englobaremos nuestra variable _Ruta_ para que se pueda acceder a ella, luego al nosotros ingresar la ruta y el programa ya haberla recibido le inidicaremos que la limpiaremos y que elimine todo en el campo _texto_.
        ~~~
        def nuevo():
        global ruta
        info.set('Nuevo Archivo')
        ruta = ""#limpiar la ruta del archivo
        texto.delete(1.0, 'end')
        raiz.title('Editanto ando')# en float es un salto '1.0'
        ~~~
2. _abrir_
   - Ahora siguiendo las indicaciones que nos pide nuestro proyecto crearemos una opcion o funcio de abrir, para elloa englobaremos ruta y a traves de asignarle, un _filedialog_ con la funcion _askopenfilename_ que nos preguntara bien sea la ruta de nuestro archivo o el nombre del archivo.
   Cosas a tomar en cuenta.
       - initial dir: nos sirve para indicar donde se iniciara nuestra busqueda en este caso le diremos en donde estamos parados con un __"."__ 
       - filetypes: a traves de este parametro de _filedialog_ le indicaremos que tipos de archivos seran abiertos a traves de una _tupla_ como nuestro proyecto nos indica que todo tipo debera ser accesible usamos __".*"__ para indicar que todos los archivos con extension _. [formato]_ sera usado.
        ~~~
        def abrir():
        # volvemos globl ruta por que los comandos solo detectan variables externas que son widgets
        global ruta
        info.set('Abrir Archivo')
        # creamos una ventana de busqueda
        # especificar la ruta del archivo para encoontrarlo
        ruta = Fd.askopenfilename(
            initialdir='.',
            filetypes=(
                ("Ficheros de texto", ".*"), 
            ),
            title="Abrir un Archivo"
        )
        ~~~
        Luego a traves de una validacion si el espacio de ruta no se encuentra vacio:
        ~~~
        if ruta != "":
        ~~~
        Le diremos que abra nuestra ruta en formato de lectura y que nos lea desde la primera fila, luego limpiaremos pantalla con _delete_ y para insertar el nuevo contenido usaremos la funcion _insert_ que agrega datos a una lista.
        ~~~
        with open(ruta, 'r+') as archivo:
            contenido = archivo.read()
        # salto de linea y lee hasta el final para limpiar pantalla para ver si esta vacio
            texto.delete(1.0, 'end')
            texto.insert('insert', contenido)  # aniade un item a la lista
            raiz.title(ruta + "Editando un texto")
        ~~~
3. _guardar_
   - Para guardar un archivo lo primero que debemos hacer es validar si nuestro espacio de ruta no se encuentra vacio, luego para obtener lo que haya escrito o editado utilizaremos el metodo _get_ para obtener desde la primera fila hasta la ultima eliminando el ultimo salto de linea, para ello usaremos en nuestros parametros en el segundo _"end1-c"_.
        ~~~
        def guardar():
        info.set('Guardar Archivo')
        # global ruta  # para que se pueda acceder
        if ruta != "":
            # obtener el texto y hacemos un salto del principio hasta el final
            contenido = texto.get(1.0, 'end-1c')#para eliminar el salto de linea al final le restamos 1 al end
        ~~~
        Luego para escribir o remplazar el texto que queremos sobreescribir en el archivo debemos utilizar la funcion _With open_ y la daremos como parametro de escritura _"W+"_ para que pueda leer los archivos y escribir en ellos por ultimo escribiremos en la variable contenido que fue anteriormente declarada.
        ~~~
        with open(ruta, 'w+') as archivo:
            archivo.write(contenido)
            info.set('Archivo Guardado Exitosamente!')
            
        else: guardar_como()
        ~~~
4. *guardar_como*
    - En la realizacion de *guardar_como* crearemos una lista que estara formada por tuplas, que identifiquen el tipo de documento con su tipo de extension respectiva o utilizaremos el formato _"All Files(*)"_, _'*.*'_ para guardar los archivos en su extension acorde; Similar a cuando abrimos un archivo con el metodo *askopenfile* usaremos el metodo *asksaveasfile* que nos permite guardar un archivo con la extension y nombre que querramos, ademas le daremos un parametro de modo _'w+'_ para que de existir el archivo lo sobreescriba en el al ser de su misma extension, y le daremos una extension default o por defecto de la variable _"extension"_ para poder guardar nuestro archivos de cualquier tipo.
  
        ~~~
        def guardar_como():
        info.set('Guardar Archivo Como')
        global ruta
        #Guarda el archivo, lo lee y puede escribir en el asksaveasfile
        extension = [('All Files(*.*)', '*.*'),
                 ('Python Files', '*.py'),
                 ('Text Document', '*.txt')]
    
            archivo = Fd.asksaveasfile(title="Guardar Archivo", mode ='w+', defaultextension= extension)
            #volvemos por default la extension txt
        ~~~

        Luego de ello a traves de una validacion si el archivo contiene algo, obtendremos los datos de nuestro archivo en ruta con la funcion _get_.

        ~~~
         if archivo is not None: #si el archivo tiene algo
        ruta = archivo.name #ruta del archivo
        contenido = texto.get(1.0,'end-1c')#obtenemos el text
        ~~~

        Para escribir los datos y leer nuestro archivo usaremos de nuevo la funcion _with open_ junto cocn un parametro de _'w+'_ para poder leer y escribir en el archivo, por ultimo escribiremos en nuestro campo _'contenido'_ que contiene lo que habremos ingresado.

        ~~~
         with open(ruta,'w+') as archivo:
            archivo.write(contenido)#escibir lo que hay en pantalla
            info.set('Se ha guardado el archivo exitosamentne!')
        ~~~
        De no ser lo anterior entonces nos devolvera un error, y limpiaremos la ruta.

        ~~~
         else:
        info.set('Ha ocurrido un error!')
        ruta = ""
        ~~~

5. _Salir_
   - Por ultimo crearemos una opcion de salida utilizando un metodo propio de _Tkinter_ 
        ~~~
        _File_menu.add_command(label="Salir", command=raiz.quit)
        ~~~
***
### **Funciones para manejar texto dentro del editor de texto**

1. _Deshacer_
   - En __Deshacer o Undo__ accederemos a traves de la funcion de tkinter ya establecida para utilizar un macro como: _"Ctrl + Z"_ para deshacer lo escrito, copiado o cortado en el campo de texto, _texto_; Se podra acceder a traves de el macro o en opciones de editar.
        ~~~
        _File_menu_edit.add_command(label="Deshacer",accelerator="Ctrl + Y",command=texto.edit_undo)#Deshacer 
        ~~~ 
2. _Rehacer_
   - En __Rehacer o Redo__ similar a la opcion _deshacer_ accederemos a traves de una funcion ya establecida en tkinter y nos dara acceso a el macro _"Ctrl + Y"_.
        ~~~
        _File_menu_edit.add_command(label="Rehacer", accelerator="Ctrl + Z", command=texto.edit_redo)#Rehacer
        ~~~ 
        Todo lo anteior sera realizado a traves de un menu en cascada agregado al campo superior, para ello se creo un menu llamado *_File_menu_edit_* utilizando el mismo campo que la variable **_Menu** de esta manera:
        ~~~
        _File_menu_edit = Menu(_Menu, tearoff=0)
        _File_menu_edit.add_separator()
        _Menu.add_cascade(label="Editar", menu=_File_menu_edit)
        ~~~
***
### **Funciones de ayuda o informacion desplegable**
Para el apartado de __Manual de usuario__ se uso el modulo _webbrowser_ para renderizar html o links por que _tkinter_ nativamente no cuenta con uno.

- Agregado a ello se uso el modulo _messagebox_ para desplegar un cuadro de informacion para las opciones __Informacion__ e __Integrantes__ ambas siendo llamadas con funciones.
  
_Opciones integradas de ayuda:_
   - Informacion
        > Muestra un resumen de las acciones realizadas por la aplicacion y su funcionamiento.
        >~~~
        >
        >def informacion():
        > info.set('Desplegando informacion del programa')
        > #usamos messagebox para mostrar una alertbox con la informacion
        ># por default contiene la opcion ok
        >mb.showinfo('Informacion', "Version:1.0.\nPython: 3.10.4. >\nLibrerias: Tkinter, Fyletype, Pywebview")
        >
        >~~~
        
   - Manual de usuario
        > Muestra la documentacion del proyecto este contiene:
        >1. Documentacion:
        >    - Interna 
        >    - Externa
        >2. Link de github
        >3. Nombre del autor
        >4. Video explicativo
        >
        >~~~
        >
        >def manual_de_usuario():
        >info.set('Abriendo documentacion')
        > webbrowser.open('https://github.com/Re-21-12')
        >
        >~~~
   - Integrantes
        > Muestra informacion acerca de los integrantes del proyecto:
        > 1. El nombre
        > 2. No. Carne
        > 3. No. Grupo
        >~~~
        >def integrantes():
        >mb.showinfo('Integrantes', 'Nombre: Victor Alfredo Macario Enriquez.\nNo Carne:7690-22-5042.\nSeccion:A.\nUniversidad: Universidad Mariano Galvez.\nSede:Boca del Monte.')
        >
        >~~~
***
### **Clases, atributos y metodos de Tkinter**
En esta seccion se mostraran las partes o funciones utilizadas para la estructura del objeto de la libreria __Tkinter__
1._raiz_
   - En __raiz__ realizaremos una base sobre los componentes que debera contener nuestro programa, se encuentra definido dentro del codigo como:
        ~~~
        #-_-_-_-_-_-_-_-_-_-_-_-_-_CONFIGS_-_-_-_-_-_-_-
        # Creamos una raiz
        raiz = Tk()
        raiz.title("Mi Tercer Proyecto")
        raiz.config(bd=10)
        raiz.config(bg='#4C6988')
        raiz.config(relief='raised')
        raiz.resizable(0,0)
        ~~~
        Estableceremos nuestro menu a una variable asignada con las opciones y campos que contendra __menu__
        ~~~
        raiz.config(menu=_Menu)
        ~~~
        En __mainloop()__ Estableceremos que escuche todas las acciones o bien dicho reciba todos los inputs que se realicen en este campo de _Raiz_ a traves de un metodo de objeto, hasta que seleccionemos una opcion de salir o detengamos el programa.
        ~~~
        raiz.mainloop()
        ~~~
2. *_Menu*
    - En el __Menu__ Establecemos a partir de tkinter un cuadro o serie de opciones a agregar como opciones a seleccionar, donde podemos agregar botones y cuadros de dialogo que cumplan funciones que deseemos.
        ~~~
        _Menu = Menu(raiz)
        # -_-_-_-_-_-_-_-_MENU-_-_-_-_-_-_-_-_-_-_-_-_
        # asiganmos nuestro menu
        _Menu = Menu(raiz)
        # para mostrar la ventana flotante del menu en cascada
        _File_menu = Menu(_Menu, tearoff=0)
        # aniadimos opciones
        # Crear y abrir
        _File_menu.add_command(label="Nuevo", command=nuevo)
        _File_menu.add_command(label="Abrir", command=abrir)
        _File_menu.add_separator()
        # Guardados
        _File_menu.add_command(label="Guardar", command=abrir)
        _File_menu.add_command(label="Guardar Como", command=guardar_como)
        _File_menu.add_separator()
        # Salida
        _File_menu.add_command(label="Salir", command=raiz.quit)
        _Menu.add_cascade(label="Archivo", menu=_File_menu)
        ~~~
3. _texto_
    - En __texto__ indicaremos el diseño de nuestro campo de texto y funciones debe contener dentro de el siempre trabajando a traves del componente base llamado raiz. En este caso tambien habilitaremos el _undo_ para poder realizar actividades como _deshacer_ o _rehacer_ a traves de funciones indicadas.
        ~~~
        # -_-_-_-_-_-_-_-_TEXTO-_-_-_-_-_-_-_-_-_-_-_-_
        # asignamos una variable a nuestro raiz en texto

        texto = Text(raiz, undo=True)
        # empaquetamos texto en raiz
        # le indicamos donde lo queremos
        texto.pack(fill='both', expand=1)
        texto.config(cursor="tcross")
        texto.config(bg = "#bbbbbb")
        # configuracion del texto
        texto.config(padx=5, pady=5, bd=0, font=("Comic Sans MS", 10, "bold"))
        ~~~
4. _info_
   - En __info__ asignaremos una variable de control para asi en funcion almacenar una cadena en este caso el modo a traves de funciones _.set_ y la informacion que se estara mostrando en pantalla.
        ~~~
        # -_-_-_-_-_-_-_-_Mostrando texto abajo del campo-_-_-_-_
        # funcion actualizable con setter y getter metodos para informacion dinamica
        info = StringVar()
        info.set('Bienvenido')
        ~~~
        A traves de una variable en este caso llamada __monintor__ establaceremos un _Label_ o etiqueta donde se mostrara en nuesta base _raiz_ la variable de texto o cadena _info_ y la justificaremos a la   izquierda inferior.
        ~~~
        info = StringVar()
        info.set('Bienvenido')
        monitor = Label(raiz, textvar=info, justify='left')
        monitor.pack(side='left')
        ~~~
5. _frame_
    - En __Frame__ establaceremos a traves de nuestra base _raiz_ un cuadro donde se mostrara el diseño o marco que tendra a manera de diseño, en el podremos cambiar opciones como estilos de cuadro, cursores entre otras opciones para darle una mejor vista a nuestro programa.
        ~~~
        frame = Frame(raiz)
        #empaquetamos el frame en nuestra raiz
        frame.pack(fill='both', expand=1)
        # fondo
        frame.config(bg='#ffbcda')
        # bold o negrita del marco
        frame.config(bd=15)
        frame.config(cursor='tcross')
        # marco
        frame.config(relief="groove")
        ~~~
# Codigo Fuente
~~~
'''
Tercer Proyecto
Victor Macario7690-22-5042
'''

# -_-_-_-_-_-_LIBRERIAS-_-_-_-_-_-_-_-_-_-_-_-_
# importamos todo
from argparse import FileType
from re import T
from tkinter import *
# indexador de archivos
from tkinter import filedialog as Fd
# para mostrar mensajes de alerta
from tkinter import messagebox as mb
# para abrir ventanas de busqueda en tkinter usando webrowser y nuestro navegador por defecto
import webbrowser

# ///////////////RUTA//////////////
ruta = ''
#-_-_-_-_-_-_-_-_-_-_-_-_-_CONFIGS_-_-_-_-_-_-_-

# Creamos una raiz

raiz = Tk()
raiz.title("Mi Tercer Proyecto")
raiz.config(bd=10)
raiz.config(bg='#4C6988')
raiz.config(relief='raised')
raiz.resizable(0,0)

# -_-_-_-_-_-_-_-_Mostrando texto abajo del campo-_-_-_-_
# funcion actualizable con setter y getter metodos para informacion dinamica
info = StringVar()
info.set('Bienvenido')
monitor = Label(raiz, textvar=info, justify='right')
monitor.config(bg='#4C6988')
monitor.pack(side='bottom')

# -_-_-_-_-_-_-_-_TEXTO-_-_-_-_-_-_-_-_-_-_-_-_
# asignamos una variable a nuestro raiz en texto

texto = Text(raiz, undo=True)
# empaquetamos texto en raiz
# le indicamos donde lo queremos
texto.pack(fill='both', expand=1)
texto.config(cursor="tcross")
texto.config(bg = "#bbbbbb")
# configuracion del texto
texto.config(padx=5, pady=5, bd=0, font=("Times New Roman", 12, "bold","normal"))

# -_-_-_-_-_-_-_-_-_-_-_-_Funciones-_-_-_-_-_-_-_-_-_-_


def nuevo():
    global ruta
    info.set('Nuevo Archivo')
    ruta = ""#limpiar la ruta del archivo
    texto.delete(1.0, 'end')
    raiz.title('Editanto ando')# en float es un salto '1.0'


def abrir():
    # volvemos globl ruta por que los comandos solo detectan variables externas que son widgets
    global ruta
    info.set('Abrir Archivo')
    # creamos una ventana de busqueda
    # especificar la ruta del archivo para encoontrarlo
    ruta = Fd.askopenfilename(
        initialdir='.',
        filetypes=(
            ("Ficheros de texto", ".*"), 
        ),
        title="Abrir un Archivo"
    )
    if ruta != "":
        with open(ruta, 'r+') as archivo:
            contenido = archivo.read()
        # salto de linea y lee hasta el final para limpiar pantalla para ver si esta vacio
            texto.delete(1.0, 'end')
            texto.insert('insert', contenido)  # aniade un item a la lista
            raiz.title(ruta + "Editando un texto")

#-_-_-_-_-_-_-_-_FUNCIONES DE GUARDADO-_-_-_-_-_-_-_-_-_-_-_-_-_-_
def guardar():
    info.set('Guardar Archivo')
   # global ruta  # para que se pueda acceder
    if ruta != "":
        # obtener el texto y hacemos un salto del principio hasta el final
        contenido = texto.get(1.0, 'end-1c')#para eliminar el salto de linea al final le restamos 1 al end
        with open(ruta, 'w+') as archivo:
            archivo.write(contenido)
            info.set('Archivo Guardado Exitosamente!')
            
    else: guardar_como()


def guardar_como():
    info.set('Guardar Archivo Como')
    global ruta
    #Guarda el archivo, lo lee y puede escribir en el asksaveasfile
    extension = [('All Files(*.*)', '*.*'),
                 ('Python Files', '*.py'),
                 ('Text Document', '*.txt')]
    
    archivo = Fd.asksaveasfile(title="Guardar Archivo", mode ='w+', defaultextension= extension)
    #volvemos por default la extension txt
    
    if archivo is not None: #si el archivo tiene algo
        ruta = archivo.name #ruta del archivo
        contenido = texto.get(1.0,'end-1c')#obtenemos el text
        with open(ruta,'w+') as archivo:
            archivo.write(contenido)#escibir lo que hay en pantalla
            info.set('Se ha guardado el archivo exitosamentne!')
    else:
        info.set('Ha ocurrido un error!')
        ruta = ""
#-_-_-_-_-_-_-_-_FUNCIONCES DE AYUDA-_-_-_-_-_-_-_-_-_-_
def informacion():
    info.set('Desplegando informacion del programa')
    #usamos messagebox para mostrar una alertbox con la informacion
    # por default contiene la opcion ok
    mb.showinfo('Informacion', "Version: 1.0.\nPython: 3.10.4. \nLibrerias: Tkinter, Fyletype & Pywebview")
        
def manual_de_usuario():
    info.set('Abriendo documentacion')
    webbrowser.open('https://github.com/Re-21-12/Tercer-Proyecto_Editor-de-Texto')

def integrantes():
    mb.showinfo('Integrantes', 'Nombre: Victor Alfredo Macario Enriquez.\nNo Carne:7690-22-5042.\nSeccion:A.\nUniversidad: Universidad Mariano Galvez.\nSede:Boca del Monte.')
    
    
# -_-_-_-_-_-_-_-_MENU-_-_-_-_-_-_-_-_-_-_-_-_
# asiganmos nuestro menu
_Menu = Menu(raiz)
# para mostrar la ventana flotante del menu en cascada
_File_menu = Menu(_Menu, tearoff=0)
# aniadimos opciones
# Crear y abrir
_File_menu.add_command(label="Nuevo", command=nuevo)
_File_menu.add_command(label="Abrir", command=abrir)
_File_menu.add_separator()
# Guardados
_File_menu.add_command(label="Guardar", command=guardar)
_File_menu.add_command(label="Guardar Como", command=guardar_como)
_File_menu.add_separator()
# Salida
_File_menu.add_command(label="Salir", command=raiz.quit)
_Menu.add_cascade(label="Archivo", menu=_File_menu)

# -_-_-_-_-_-_-_-_MENU-Atajos_-_-_-_-_-_-_-_-_-_-_-_
# Rehacer y Deshacer
_File_menu_edit = Menu(_Menu, tearoff=0)
_File_menu_edit.add_command(label="Rehacer", accelerator="Ctrl + Z", command=texto.edit_redo)#Rehacer
_File_menu_edit.add_command(label="Deshacer",accelerator="Ctrl + Y",command=texto.edit_undo)#Deshacer 
_File_menu_edit.add_separator()
_Menu.add_cascade(label="Editar", menu=_File_menu_edit)

#-_-_-_-_-_-_-_-_-_-_APARTADO DE AYUDA-_-_-_-_-_-_-_-_-_-_
#ayuda
_File_menu_help = Menu(_Menu, tearoff=0)
_File_menu_help.add_command(label="Informacion(!)", command=informacion)
_File_menu_help.add_command(label="Manual de usuario", command=manual_de_usuario)#agregar link
_File_menu_help.add_command(label="Integrantes", command=integrantes)
_Menu.add_cascade(label="Ayuda", menu=_File_menu_help)
# -_-_-_-_-_-_-_-_raiz loop-_-_-_-_-_-_-_-_-_-_
raiz.config(menu=_Menu)
raiz.mainloop()

~~~