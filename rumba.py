from tkinter import *
root = Tk()
root.geometry("650x650")

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
