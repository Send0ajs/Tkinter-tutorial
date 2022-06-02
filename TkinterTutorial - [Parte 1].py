## Parte 1 ###########################################################
############################ Introducción ############################

#¡Hola! Esta aplicación es creada a modo tutorial y almacenada aquí como apuntes. Para esta aplicación usare el modulo "Tkinter"
# un modulo en el que profundizare y explicare con varias anotaciones a lo largo del documento. (Esto es la 1º y mas basica parte)

# tkinter es un modulo que esta orientado a objetos. Con esto estaremos llamando a este modulo: 

from tkinter import Tk, Label, Button 

############################ Tutorial ############################

# Tk() Esto te permite crear la ventana principal donde ira colocado todos los widwets que pongamos.

# pack() Ubica los widgets en una posición que podemos cabiar a través de los atributos.

# mainloop() Con esto establecemos la interaccion del unsuario con el programa. Se iniciara un bucle que permitira monitorear la
# interaccion del usuario a traves del ratón o teclado. Por ejemplo cuando se produce el evento de dar click al boton cerrar, se
# responde cerrando la aplicación.


############################ Funcion a ejecutar ############################

#Este programa cumple con la simple función de mostrarnos este texto por consola cada vez que el usuario pulse el
# boton que mas adelante pondremos, por ello definimos esta simple funcion en la que tendra simplemente un "Print" con el texto que 
# que se nos mostrara por consola.

def mensaje():
    print("¡Click!")


#Configuración de la ventana
ventana = Tk() 
ventana.geometry("400x280")
ventana.title("Ventana de ejemplo")

#Configuración
lbl = Label(ventana, text="Pulsa click para que sucedan cosas magicas.")
lbl.pack()

btn = Button(ventana, text="Click", command=mensaje)
btn.pack()

ventana.mainloop()

