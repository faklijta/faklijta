from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=600)

canvas.pack()

def square(x, y, size):
    canvas.create_rectangle(x, y, x + size, y + size, fill="black")


def draw_square(x, y, size):
    if size < 2:
        return
    else:
        square(x, y, size)
        size = size/3
        draw_square(x - size*2, y + size, size)
        draw_square(x + size , y - 2 * size, size)
        draw_square(x + 4 * size , y + size, size)
        draw_square(x + size , y + 4 * size, size)
        draw_square(x + 4 * size , y + 4 * size, size)
        draw_square(x + 4 * size , y - 2 * size, size)
        draw_square(x - 2 * size , y - 2 * size, size)
        draw_square(x - 2 * size , y + 4 * size, size)


draw_square(200,200,200)
root.mainloop()