############################ Parte 2 ############################
# Extensión para visual studio recomendada: "Tkinter Snippets"

from tkinter import * #Esta vez importamos todas las funciones que tkinter nos ofrece a traves de "*"

app = Tk()
app.geometry("499x499")
app.title("Aplicación gráfica: Parte 2")

############################ Textos #############################

# Escribir texto dentro de nuestra aplicación: 
# Label() -> Label nos permite la introducción de textos graficos en nuestra app.

Label(app, text="Soy un texto por defecto").pack() #Texto por defecto(Centrado).
Label(app, text="Soy un texto centrado").pack(anchor=CENTER) #Texto por centrado.
Label(app, text="Izquierda").pack(anchor=NW) # Texto a la izquierda.
Label(app, text="Derecha").pack(anchor=SE) # Texto a la derecha.

# Dar color y formato a nuestro texto:

label = Label(app, text="Texto colorino") 
label.pack(anchor=CENTER)
label.config(fg="red",               # Color del texto.
            bg="black",              # Color del fondo. 
            font=("Verdeta", 24))    # Formato y tamaño de texto.

############################ Imagenes #############################

imagen = PhotoImage(file="1.gif") #Desde file indicamos cual va a ser la imagen a improtar.
Label(app, image=imagen, bd=0).pack() # Aquí importamos la imagen a nuestra app.


app.mainloop()