"""
Lab 5:
"""

def main():
    print_even_numbers(2, 14)
    print_even_numbers(5, 16)
    print_even_numbers(65, 20)

def print_even_numbers(first_num, last_num):
    if first_num % 2 == 0:
        for number in range(first_num, last_num+1, 2):
            print(number, end = " ")

    elif first_num % 2 != 0:
        first_num = first_num + 1
        for number in range(first_num, last_num+1, 2):
            print(number, end = " ")

    elif first_num < last_num:
        return
        
    

main()








