""" Assignment 3 function 3"""

def main():
    print_header(3, "get_fail_pass_average()")
    print("1.", get_fail_pass_average([63, 65, 33]))
    print("2.", get_fail_pass_average([63, 62, 100, 100]))
    print("3.", get_fail_pass_average([33, 42, 20, 10]))
    print("4.", get_fail_pass_average([50, 50, 100, 0]))

#--------------------------------------------------
# 3333333333333333333333333333333333333333333333333
# Returns a Python list containing the average fail
# mark and the average pass mark.
#--------------------------------------------------
def get_fail_pass_average(a_list):

    list_below = []
    list_pass = []
    result = []

    for number in a_list:
        if number < 50:
            list_below.append(number)
            
        elif number >= 50:
            list_pass.append(number)

    if list_below != []:
        average_str1 = round(sum(list_below) / len(list_below))
        result.append(average_str1)
    elif list_below == []:
        result.append(-1)
        
    if list_pass != []:
        average_str2 = round(sum(list_pass) / len(list_pass))
        result.append(average_str2)
    elif list_pass == []:
        result.append(-1)
    
    return result

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
