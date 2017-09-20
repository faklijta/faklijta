from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def step_drawer():
    start_point = 10
    end_point = 10
    size = 10
    for i in range(0, 6):
        new_start_point = start_point + size
        new_end_point = end_point + size
        square = canvas.create_rectangle(start_point, start_point, end_point + size, end_point + size, fill = "purple")
        size += 10
        start_point = new_start_point
        end_point = new_end_point
step_drawer()
root.mainloop()