"""
Lab 4:
"""

def main():
    print_even_numbers(6, 20)
    print()

    print_even_numbers(7, 20)
    print()

    print_even_numbers(-9, 5)
    print()

    print_even_numbers(21, 4)

def print_even_numbers(first_num, last_num):
    while first_num <= last_num:
        if first_num % 2 == 0:
            print(first_num, end = " ")
            first_num = first_num + 2
        else:
            first_num = first_num + 1


main()








