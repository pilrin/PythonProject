from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

canvas.create_polygon(250, 400, 275, 450, 225, 450)
canvas.create_polygon(250, 400, 275, 450, 225, 450)

for i in range(0, 70):
    canvas.move(1, -5, -5)
    canvas.move(2, 5, -5)

    tk.update()
    time.sleep(0.05)