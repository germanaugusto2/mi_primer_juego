from tkinter import *
import random
from tkinter import Tk, Canvas, PhotoImage



BASE = 460
ALTURA = 220
radio = 10

ventana_principal = Tk()
ventana_principal.title("Mi primer juego")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

# frame graficacion
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

c = Canvas(frame_graficacion,width=BASE, height=ALTURA)
c.config(bg="gray")
c.place(x=10,y=10)

linea_central_horizontal = c.create_line(0,ALTURA/2,BASE,ALTURA/2, fill="gold")
linea_central_horizontal = c.create_line(0,ALTURA/1.6,BASE,ALTURA/1.6, fill="gold")




img_carrito = PhotoImage(file="img/carrito.png")
nave = c.create_image(BASE/4-50,ALTURA/4,image=img_carrito)


img_carrito2 = PhotoImage(file="img/carrito2 (1).png")
nave1 = c.create_image(BASE/4-50,ALTURA/1.3,image=img_carrito2)


rect_1 = c.create_rectangle(BASE/1.2,ALTURA/9,BASE/1.1,ALTURA/1.1, fill="red")
rect_2 = c.create_rectangle(BASE/4,ALTURA/9,BASE/3,ALTURA/1.1, fill="ivory2")




frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

# desplegar ventana
ventana_principal.mainloop()