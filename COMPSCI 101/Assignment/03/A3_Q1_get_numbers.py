""" Assignment 3 function 1"""

import random

def main():
    print_header(1, "get_numbers()")
    list1 = [23, 3, 6, 5, 12, 9, 7, 4]
    list2 = get_numbers(list1)
    print(list1, "=>", list2)
    print()

    list1 = [87, 77, 49, 21, 4, 80, 51]
    print(list1, "=>", get_numbers(list1))
    print()

    list1 = [9, 30, 27, 36]
    print(list1, "=>", get_numbers(list1))
    print()

    list1 = []
    print(list1, "=>", get_numbers(list1))
    
#--------------------------------------------------
# 11111111111111111111111111111111111111111111111111
# Returns the list of odd numbers which are not exactly
# divisible by 3 from the parameter list of
# numbers
#--------------------------------------------------
def get_numbers(a_list):
    new_list = []
    
    for number in a_list:
        if number % 3 != 0 and number % 2 != 0:
            new_list.append(number)

    return new_list

#--------------------------------------------------
#Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()

