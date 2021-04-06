"""
Lab 5:
"""

def main():
    print("[313, 636, 2042, 40, 447] - ", end = "")
    count_same_start_end = get_count_same_start_end([313, 636, 2042, 40, 447])
    print(count_same_start_end)
    print("[101, 4559, 241, 124, 9249] - ", end = "")
    print(get_count_same_start_end([101, 4559, 241, 124, 9249]))
    print("[101, 45594, 1241, 9, 929] - ", end = "")
    print(get_count_same_start_end([101, 45594, 1241, 9, 929]))

##def get_count_same_start_end(numbers_list):
##    
##    count = 0
##    for number in range(len(numbers_list)):
##        convert_str = str(numbers_list[number])
##        if convert_str[0] == convert_str[-1]:
##            count = count + 1
##
##    return count


##def get_count_same_start_end(numbers_list):
##
##    count = 0
##    for number in range(len(numbers_list)):
##        convert_str = str(numbers_list[number])
##        if convert_str[0] == convert_str[-1]:
##            count = count + 1
##        elif len(numbers_list) == 1:
##            count = count + 1
##
##    return count


Q4
def get_count_same_start_end(numbers_list):
    count = 0
    str_list = []

    for index in range(len(numbers_list)):
        str_number = str(numbers_list[index])
        if str_number[0] == str_number[-1]:
            count +=1

    return count

main()








