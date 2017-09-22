from tkinter import *

root = Tk()
canvas_width = 500
canvas = Canvas(root, width=canvas_width, height=canvas_width, bg = "yellow")

canvas.pack()
canvas_width = 500
size = canvas_width/3

def lines(x, y, size):
    if size < 2:
        return
    else:
        x_new = x + size
        y_new = y + size
        canvas.create_line(x_new, y, x_new, y + size*3)
        canvas.create_line(x_new + size, y, x_new + size, y + size*3)
        canvas.create_line(x_new - size, y + size, x_new + size*2, y + size)
        canvas.create_line(x_new - size, y + size*2, x_new + size*2, y + size*2)
        lines(x_new, y, size/3)
        lines(x, y_new, size/3)
        lines(x_new + size, y_new, size/3)
        lines(x_new, y_new + size, size/3)


lines(0, 0, size)
root.mainloop()