from tkinter import *

root = Tk()
canvas_width = 400
canvas = Canvas(root, width=canvas_width, height=canvas_width)

canvas.pack()
canvas_width = 400

# def main_square(x, y, size, border):
#     canvas.create_rectangle(x,y, x+size, y+size, outline="black", width=border, fill="")

def squares(x, y, size, border):
    if size < 20:
        return
    else:
        canvas.create_rectangle(x + size/4, y+size/4, x+size/4*3, y+size/4*3, outline="black", width=border, fill="")
        squares(x, y, size/2, border/2)
        squares(x+size/2, y, size/2,border/2)
        squares(x, y+size/2, size/2,border/2)
        squares(x+size/2, y+size/2, size/2,border/2)


squares(0, 0, 400, 15)
root.mainloop()