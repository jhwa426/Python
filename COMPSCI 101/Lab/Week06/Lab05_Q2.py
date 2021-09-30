"""
Lab 5:
"""

def main():
    
    print_numbers(10, 25)
    print()
    print_numbers(25, 20)
    print()
    print_numbers(9, 33)
    print()

def print_numbers(number1, number2):
    for number in range(1, 100):
        if number % number1 == 0 or number % number2 == 0:
            print(number, end =" ")
            

main()







