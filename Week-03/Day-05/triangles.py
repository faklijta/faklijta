from tkinter import *
import math

root = Tk()
canvas = Canvas(root, width=500, height=500)

canvas.pack()

def triangle(x, y, size):
    height = math.sqrt(3) / 2 * size
    canvas.create_polygon(x, y, x + size, y, x + size /2, y + height, fill = "", outline = "black")
    canvas.create_polygon(x + size / 2, y, x + size / 4, y + height /2, x + size / 4*3, y + height /2, fill = "", outline = "black")

def draw_traingle(x, y, size):
    if size < 10:
         return
    else:
        height = math.sqrt(3) / 2 * size
        triangle(x, y, size)
        draw_traingle(x, y, size / 2)
        draw_traingle(x + size/2, y, size / 2)
        draw_traingle(x + size/4, y + height / 2, size / 2)



draw_traingle(10,10,400)
root.mainloop()