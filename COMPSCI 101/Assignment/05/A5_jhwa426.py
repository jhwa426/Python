##Name : Jeff Hwang
##User name : jhwa426

from tkinter import *

#-------------------------------------------
#-------------------------------------------
# main() function
#-------------------------------------------
def main():
    size = 50
    start_left = size * 2
    start_down = size * 2
    
    #replace these two lines in step 8
    user_input = input("Enter a palette filename: ")
    a_file = process_file(user_input)
    user_input2 = input("Enter a pattern filename: ")
    a_file2 = process_file(user_input2)
    
    colours_dictionary = create_colours_dict(a_file)
    pattern_list = create_pattern_list(a_file2)
    
    
    number_of_rows = len(pattern_list)	
    number_of_columns = len(pattern_list[0])
    canvas_width = size * number_of_columns +size * 4
    canvas_height = number_of_rows * size + size * 4
    window = Tk() 
    window.title("A5 by jhwa426") 
    geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
    window.geometry(geometry_string)
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill = BOTH, expand = True) #Canvas fills the whole window  
    draw_pattern(a_canvas, colours_dictionary, pattern_list, size, start_left, start_down)
    window.mainloop()

##Ex 3
def split_digits(line):
    a_list = []
    for number in line:
        a_list.append(int(number))
        
    return a_list

##Ex 4
def process_file(line):
    input_file = open(line, "r")
    contents = input_file.read().split()
    input_file.close()
    
    return contents

##Ex 5
def create_colours_dict(lines):
    a_dict = {}
    for name in lines:
        key = name[:1]
        value = name[2:]
        a_dict[int(key)] = value
        
    return a_dict

##Ex 6 
def create_pattern_list(lines):
    a_list = []
    for element in lines:
        line = split_digits(element)
        a_list.append(line)

    return a_list


##Ex 7
def draw_pattern(a_canvas, colours_dictionary, pattern_list, size, left, top):
    possible_digits = "0123456789"      
    down = left
    
    #complete this
    
    for row in pattern_list:
        for digit in row:
            a_canvas.create_rectangle(left,top, left+size, top+size, fill = colours_dictionary[digit])
            left = left + size
        
        left = down
        top = top + size
        



    

main()
##Test
##Iron_man_palette.txt
##Iron_man.txt

##steve_palette.txt
##steve.txt










