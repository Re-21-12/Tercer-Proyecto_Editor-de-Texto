'''
Tercer Proyecto
Victor Macario7690-22-5042
'''
'''
Tk : raiz de todos los widgets
Frame: mamrco contenedor de widgets
Label: mostrar texto estatico
Entry: Campo para escribir texto corto
Text: Campo multilinea para texto largo
Button: Botoon
Radiobutton: Para marcar opciones
Checkbutton: Se puede chequear
Menu: botones centrados en menus superioroes
Dialogs: muestra informacion al usuaio
'''

#Librerias 
from tkinter import *
# -_-_-_-_-_-_-_-_RAIZ-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# creamos la raiz o donde iran los widgets 'ventana'
raiz = Tk()
# para colocarle un titulo a la ventana
raiz.title("Tercer Proyecto Victor Macario")
# desactivar la redimension de la ventana
raiz.resizable(1,1)

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_WIDGET FRAME-_-_-_-_-_-_-_-_-_-_-_-_
#tiene tamanio propio y puede cambiar de posicion

#creamos un hijo raiz
# la raiz es naturalmente adaptable al tamanio
# le asigngamos unas dimensiones de tamanio
#dimensiones
# '''
frame = Frame(raiz, width=480, height=320)
#empaquetamos el frame en nuestra raiz
frame.pack(fill='both', expand=1)
# fondo
frame.config(bg='#ffbcda')
# bold o negrita del marco
frame.config(bd=15)
# cursor 
frame.config(cursor='tcross')
# marco
frame.config(relief="groove")

#-_-_-_-_-_-_-_-_-_-_ROOT DESIGN-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
raiz.config(cursor='tcross')
raiz.config(bd=10)
raiz.config(bg='#4C6988')
raiz.config(relief='raised')

#-_-_-_-_-_-_-_-_-_-_LABEL-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# creando etiquetas estaticas 
# iniciamos un bucle en la app

##-_-_-_-_-_-_-_-_-_-_WIDGET ENTRY-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

label = Label(raiz, text="Nombre")
label.grid(row=0,column=0, sticky=W, padx=5, pady=5)

entry = Entry(raiz)
entry.grid(row=0,column=1, padx=5, pady=5)
entry.config(justify="right", state="normal")

#-_-_-_-_-_-_-_-_CONFIGS ADICIONALES-_-_-_-_-_-_-_-_-_-_-_-_
show = "*"
#justify=LEFT, CENTER, RIGHT
#state=DISABLED, NORMAL 
raiz.mainloop()