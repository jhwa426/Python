""" Assignment 3 function 2"""

def main():
    print_header(2, "get_funny_average()")
    print("1.  [3, 12, 0, 25, 1] =>", get_funny_average([ 3, 12, 0, 25, 1]))
    print("2.  [-6, -32, 2, 0, -51, 1, 0, 0] =>", get_funny_average([-6, -32, 2, 0, -51, 1, 0, 0]))
    print("3.  [56, 0, 2, 0, 22] =>", get_funny_average([56, 0, 2, 0, 22]))
    print("4.  [56, 6, 0, -21, 0, 3, 4] =>", get_funny_average([-56, -3, 0, -21, 0, 6, 5]))

#--------------------------------------------------
# 22222222222222222222222222222222222222222222222222
# Returns the average of a list of numbers (excluding
# all zeroes and the minimum and maximum numbers)
#--------------------------------------------------
def get_funny_average(numbers):
    
    remove_0 = []
    for number in numbers:
        if number != 0:
            remove_0.append(number)

    if remove_0 == []:
        return 0

    largest_num = max(remove_0)
    smallest_num = min(remove_0)
    new_list = []
    
    for average_num in remove_0:
        if(average_num != largest_num and average_num != smallest_num):
            new_list.append(average_num)



    average = sum(new_list) / len(new_list)

    return round(average)       

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


