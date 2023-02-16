from tkinter import *

root = Tk()
root.title("Roomba")
root.geometry("600x600")
root.config(bg="blue")

def menu_principal():
    titulo = Label(root, text="Roomba", font=("Arial", 18), bg="blue")
    titulo.pack(pady=2)

    texto = Label(root, text="¿Cuántas zonas hay que limpiar?", font=("Arial", 16))
    texto.pack(pady=80)

    spinbox = Spinbox(root, from_=0, to=100000, increment=1)
    spinbox.pack(pady=10)

    boton = Button(root, text="Siguiente", command=lambda: operaciones(int(spinbox.get())))
    boton.pack(pady=10)

def operaciones(numero):
    root.destroy()

    if numero == 0:
        return 0

    ventana = Tk()
    ventana.title("Roomba")
    ventana.geometry("600x800")
    ventana.config(bg='blue')

    zonas = []
    for i in range(numero):
        string = "Zona " + str(i)
        text = Label(ventana, text=string, font=("Arial", 16))
        text.pack(pady=2)

        largo_label = Label(ventana, text="Largo (cm)", font=("Arial", 12))
        largo_label.pack()
        largo = Text(ventana, width=30, height=1)
        largo.pack()

        ancho_label = Label(ventana, text="Ancho (cm)", font=("Arial", 12))
        ancho_label.pack()
        ancho = Text(ventana, width=30, height=1)
        ancho.pack()

        zonas.append((largo, ancho))

    boton = Button(ventana, text="Obtener resultados", command=lambda: mostrar(zonas, ventana))
    boton.pack(pady=15)

def mostrar(zonas, ventana):
    velocidad = 3

    if not validar(zonas):
        mensaje = Label(ventana, text="Valores no válidos", font=("Arial", 25))
        mensaje.pack(pady=40)
        mensaje.after(2000, mensaje.destroy)
        return

    superficie = sum([float(zone[0].get("1.0", END)) + float(zone[1].get("1.0", END)) for zone in zonas])

    tiempo = superficie / velocidad

    final = Tk()
    final.title("Roomba")
    final.geometry("600x300")
    resultado = Label(final, text=("Tiempo: " + str(tiempo) + " segundos"), font=("Arial", 16))
    resultado.pack()

def validar(zonas):
    for zona in zonas:
        try:
            float(zona[0].get("1.0", END))
            float(zona[1].get("1.0", END))
        except:
            return False
    return True

menu_principal()
root.mainloop()



