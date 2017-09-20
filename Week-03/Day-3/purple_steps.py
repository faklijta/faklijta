from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def step_drawer(size):
    start_point = 10 - size/2  
    end_point = 10 + size/2  
    square = canvas.create_rectangle(start_point, start_point, end_point, end_point, fill = "purple")
    while start_point < 300:
        start_point = start_point + size
        end_point = end_point + size
        square = canvas.create_rectangle(start_point, start_point, end_point, end_point, fill = "purple")
step_drawer(20)
root.mainloop()