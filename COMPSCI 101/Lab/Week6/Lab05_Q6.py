"""
Lab 5:
"""

def main():
    print([117, -241, -171, 112, 317, 290, 77, 394], "- ", end = "")
    result = contains_only_3_digit_numbers([117, -241, -171, 112, 317, 290, 77, 394])
    print(result)
    print([-491, -375, -65, -348], "- ", end = "")
    print(contains_only_3_digit_numbers([-491, -375, -65, -348]))
    print([830, 466, -641, 820, -437, 875, -677], "- ", end = "")
    print(contains_only_3_digit_numbers([830, 466, -641, 820, -437, 875, -677]))



##def contains_only_3_digit_numbers(numbers):
##    empty = []
##    for check in numbers:
##        convert_abs = abs(check)
##        if convert_abs >= 100 and convert_abs < 1000:
##            empty.append(convert_abs)
##            
##    if len(empty) == len(numbers):
##        return True
##    else:
##        return False


##Q6_revision
def contains_only_3_digit_numbers(numbers):
    pass_list = []

    for index in range(len(numbers)):
        number = str(abs(numbers[index]))
        if len(number) == 3:
            pass_list.append(number)
    print(pass_list)
    if len(pass_list) == len(numbers):
        return True
    else:
        return False            

main()
    








