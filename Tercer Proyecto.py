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
_File_menu.add_command(label="Guardar", command=abrir)
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
# -_-_-_-_-_-_-_-_-_--_--_--_-FRAME-_-_-_-_-_--_--_-
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
# -_-_-_-_-_-_-_-_raiz loop-_-_-_-_-_-_-_-_-_-_
raiz.config(menu=_Menu)
raiz.mainloop()
