"""
Draws a mirrored right-angle triangle pattern
Date-written: Semester 1, 2020.
Author:
"""

def main():
    print_mirrored_right_angle_triangle(5, '*')
    print_mirrored_right_angle_triangle(3, 1)
    print_mirrored_right_angle_triangle(5, 3)

    
def print_mirrored_right_angle_triangle(number_of_rows, style):
    ##number version
    if str(style).isdigit() == True:
        for row in range(number_of_rows):
            print(" " * (number_of_rows-row-1),end ="")
            for index in range(row+1):
                print(index+style, end="")
            print()
            
    ##    ##String version
    else:
        for row in range(1, number_of_rows + 1):
            for index in range(1, number_of_rows + 1):
                if(index <= number_of_rows - row):
                    print(" ", end = "")
                else:
                    print(style, end = "")
            print()

        
main()

###Outcome

##  1
## 12
##123

##
##    3
##   34
##  345
## 3456
##34567


##    *
##   **
##  ***
## ****
##*****
