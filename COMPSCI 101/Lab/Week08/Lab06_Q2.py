"""
Lab 6:

"""

def main():
    numbers = [9, 0, 2, 5, 6, 4, 5]
    print(numbers) #[9, 0, 2, 5, 6, 4, 5]
    swap_elements(numbers, 2, 4)
    print(numbers) #[9, 0, 4, 5, 6, 2, 5]
    print()

    numbers = [9, 0, 9, 5, 6, 6, 5]
    print(numbers) #[9, 0, 9, 5, 6, 6, 5]
    swap_elements(numbers, 9, 6)
    print(numbers) #[6, 0, 9, 5, 9, 6, 5]
    print()

    numbers = [9, 8, 11, 5, 6, 7, 5]
    print(numbers)
    swap_elements(numbers, 6, 4)
    print(numbers)


##def swap_elements(numbers_list, number1, number2):
##    if number1 in numbers_list and number2 in numbers_list:
##        position1 = numbers_list.index(number1)
##        position2 = numbers_list.index(number2)
##
##        numbers_list[position1] = number2
##        numbers_list[position2] = number1
##
##    return numbers_list


main()
    
##Q2_revision
def swap_elements(numbers_list, number1, number2):
    if number1 in numbers_list and number2 in numbers_list:
        num_pos1 = numbers_list.index(number1)
        num_pos2 = numbers_list.index(number2)
        numbers_list[num_pos1], numbers_list[num_pos2] = numbers_list[num_pos2], numbers_list[num_pos1]
    else:
        return numbers_list




