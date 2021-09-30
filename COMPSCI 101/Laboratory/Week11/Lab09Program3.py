"""
Draws a pattern of red squares and green ovals.
Date-written: Semester 1, 2020.
Author:
"""

from tkinter import *

def main():
    window = Tk()  
    window.title("Jeff's Red and Green pattern")   #replace it with your UPI
    window.config(background = 'white')   
    window.geometry("500x350+10+20") 
    a_canvas = Canvas(window) 
    a_canvas.config(background = "white")   
    a_canvas.pack(fill = BOTH, expand = True)
    draw_grid(a_canvas)
    draw_pattern_in_canvas(a_canvas, 4) 
    window.mainloop()

def draw_grid(canvas):
    for row in range(50, 350, 50):
        canvas.create_line(-1, row, 501, row, fill = "lightblue")
    for column in range(50, 500, 50):
        canvas.create_line(column, -1, column, 351, fill = "lightblue")

def draw_pattern_in_canvas(a_canvas, number_of_rows):
    size = 50  #gridsize of 50
    top = 0
    
    for oval in range(1,number_of_rows + 1):
        left_hand_side = 0
        for index in range(1, number_of_rows + 1):
            #rectangle
            if index <= number_of_rows - oval:
                a_canvas.create_rectangle(left_hand_side, top, left_hand_side + size, top + size,
                                          fill = "red", outline = "black", width = 3)
            #Oval
            else:      
                a_canvas.create_oval(left_hand_side, top, left_hand_side + size , top + size,
                                     fill = "green", outline = "black", width = 3)
            left_hand_side = left_hand_side + size
            
        top = top + size

            

main()
