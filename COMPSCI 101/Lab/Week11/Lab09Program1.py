"""
Draws an ox pattern
Date-written: Semester One, 2020.
Author:
"""

def main():
    print_ox_xo_pattern(5, 4)
    print()
    
##def print_ox_xo_pattern(number_of_rows, number_of_columns):
##    for row in range(number_of_rows):
##        for column in range(number_of_columns):
##            if (row+column) % 2 == 0:
##                print("o",end = "")
##            else:
##                print("x",end = "")
##        print()

##Q1_revision
def print_ox_xo_pattern(number_of_rows, number_of_columns):
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if (row+column) % 2 == 0:
                print("o",end = "")

            print("x",end = "")
        print()
        
main()
    

    
            
    
#Outcome

##oxox
##xoxo
##oxox
##xoxo
##oxox
