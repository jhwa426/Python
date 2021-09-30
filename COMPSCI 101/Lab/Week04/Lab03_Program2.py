"""
Lab 3: Program 2 (Question 6)

"""

def main():
    print("1.", get_first_last_number(74678))
    print("2.", get_first_last_number(-455))
    print("3.", get_first_last_number(1437))
    print("4.", get_first_last_number(-5))

def get_first_last_number(number):
    change_postivie = abs(number)
    change_number = str(change_postivie)
    first_number = change_number[0]
    last_number = change_number[-1]
    result = first_number + last_number

    return int(result)
    
    
main()


