#myEtchASketch program

from tkinter import *

canvas_height=400
canvas_width=600
canvas_color="black"

p1_x=0
p1_y=0
p1_color="white"
line_width=5
line_length=5

#user_control
def p1_move_N(event):
    global p1_y

    canvas.create_line(p1_x, p1_y, p1_x, p1_y-line_length, width=line_width, fill=p1_color)
    p1_y=p1_y-line_length

def p1_move_S(event):
    global p1_y

    canvas.create_line(p1_x, p1_y, p1_x, p1_y+line_length, width=line_width, fill=p1_color)
    p1_y=p1_y+line_length

def p1_move_E(event):
    global p1_x

    canvas.create_line(p1_x, p1_y, p1_x+line_length, p1_y, width=line_width, fill=p1_color)
    p1_x=p1_x+line_length

def p1_move_W(event):
    global p1_x

    canvas.create_line(p1_x, p1_y, p1_x-line_length, p1_y, width=line_width, fill=p1_color)
    p1_x=p1_x-line_length

def erase_all(event):
    canvas.delete(ALL)

#main
window=Tk()
window.title("MyEtchASketch")
canvas=Canvas(bg=canvas_color, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

#move when pressing a key
window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Right>", p1_move_E)
window.bind("<Left>", p1_move_W)
window.bind("u", erase_all)

window.mainloop()

