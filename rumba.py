from tkinter import *
root = Tk()
root.geometry("600x600")

def MenuPrincipal():
    tittle_text = Label(root, text="Roomba")
    tittle_text.config(font=18)
    tittle_text.pack(pady=2)
    main_text = Label(root, text="¿Cuantas zonas hay que limpiar?")
    main_text.pack(pady=80)
    main_text.config(font=16)

    s = Spinbox(root, from_=0, to=100000, increment=1)
    s.config()
    s.pack(pady=10)

    boton = Button(root, text="Next", command=lambda: operaciones(s.get()))
    boton.pack(pady=10)

def operaciones(numero):
    numero = int(numero)
    root.destroy()

    if numero == 0:
        return 0

    new = Tk()
    new.geometry("600x800")

    zones = []

