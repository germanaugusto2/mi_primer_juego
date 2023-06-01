from tkinter import *

BASE = 460
ALTURA = 220


ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

c = Canvas(frame_graficacion,width=BASE, height=ALTURA)
c.config(bg="gray")
c.place(x=10,y=10)


linea_central_horizontal = c.create_line(0,ALTURA/2,BASE,ALTURA/2, fill="white")

img_carrito = PhotoImage(file="img/carrito.png")
nave = c.create_image(BASE/4-50,ALTURA/4,image=img_carrito)


img_carrito2 = PhotoImage(file="img/carrito2 (1).png")
nave1 = c.create_image(BASE/4-50,ALTURA/1.5,image=img_carrito2)





frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

# desplegar ventana
ventana_principal.mainloop()