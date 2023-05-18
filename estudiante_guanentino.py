#--------------------------------
# Desktop app No. 1- Estudiante
#--------------------------------

# se importa la libreria tkinder con todas sus funciones
from tkinter import*
from tkinter import messagebox 

#-----------------------------
# funciones de la app
#-----------------------------


# abrir toplevel_nota definitiva 
def abrir_toplevel_nota_definitiva():
    global toplevel_nota_definitiva
    toplevel_nota_definitiva = Toplevel()
    toplevel_nota_definitiva.title("nota definitiva")
    toplevel_nota_definitiva.resizable(False, False)
    toplevel_nota_definitiva.geometry("300x200")
    toplevel_nota_definitiva.config(bg="white")


#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sharol Tatiana Lopez Villegas")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="white")

barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

menu = Menu(tearoff=0)
menu.add_command(label="menu", )
menu.add_separator()
menu.add_command(label="Borrar", )

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", )

barra_menu.add_cascade(label="menu", menu=menu)
barra_menu.add_cascade(label="Salir", menu=menu_salir)


#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=500, height=500)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=50,y=40)

logo2 = PhotoImage(file="img/estudiantes.png")
lb_logo2 = Label(frame_entrada, image=logo2, bg="white")
lb_logo2.place(x=200,y=0)


#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=500, height=500)
frame_operaciones.place(x=10, y=160)

# titulo de la app
titulo = Label(frame_entrada, text="ESTUDIANTES")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=240,y=10)

# etiqueta para el dato
lb_c = Label(frame_operaciones, text = " Nombre = ")
lb_c.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
lb_c.place(x=10, y=100)

# caja de texto 
entry_c = Entry(frame_operaciones)
entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=30)
entry_c.focus_set()
entry_c.place(x=110,y=100)

lb_c = Label(frame_operaciones, text = " Edad = ")
lb_c.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
lb_c.place(x=10, y=150)

# caja de texto 
entry_o = Entry(frame_operaciones)
entry_o.config(bg="white", fg="blue", font=("Times New Roman", 18), width=30)
entry_o.focus_set()
entry_o.place(x=110,y=150)

lb_o = Label(frame_operaciones, text = " Grado = ")
lb_o.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
lb_o.place(x=10, y=200)

# caja de texto 
entry_c = Entry(frame_operaciones)
entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=30)
entry_c.focus_set()
entry_c.place(x=110,y=200)


# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()



