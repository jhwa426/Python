""" Assignment 3 function 4"""

def main():
    print_header(4, "get_every_third_even_element()")
    list1 = [23, 12, 6, 5, 8, 9, 7, 4]
    list2 = get_every_third_even_element(list1)
    print(list1, " => ", list2)
    print()

    list1 = [22, 3, 6, 5, 12, 9, 7, 4]
    list2 = get_every_third_even_element(list1)
    print(list1, " => ", list2)
    print()

    list1 = [4]
    list2 = get_every_third_even_element(list1)
    print(list1, " => ", list2)
    print()

    list1 = [24, 3, 6, 5, 12, 0, 7, 4, 8, 8, 2, 1]
    list2 = get_every_third_even_element(list1)
    print(list1, " => ", list2)

#--------------------------------------------------
# 4444444444444444444444444444444444444444444444444
# Returns a list containing every third even number
# element of the parameter list starting
# from the last element.
#--------------------------------------------------
def get_every_third_even_element(list1):
    empty_list = []
    
    for each in range(len(list1)-1,-1,-3):
        if list1[each] % 2 == 0:
            empty_list.append(list1[each])

    return empty_list
#--------------------------------------------------
# Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()
