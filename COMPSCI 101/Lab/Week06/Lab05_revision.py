"""
Lab 5:
"""
##Q1_revision
def print_even_numbers(first_num, last_num):
    if first_num % 2 == 0:
        for index in range(first_num, last_num+1, 2):
            print(index, end = " ")
    else:
        first_num += 1
        for index in range(first_num, last_num+1, 2):
            print(index, end = " ")
            
    




##Test
##print_even_numbers(2, 14)
##print()
##print_even_numbers(5, 16)
##print_even_numbers(14, 2)


##Q2_revision
def print_numbers(number1, number2):
    for index in range(1, 100):
        if index % number1 == 0 or index % number2 == 0:
            print(index, end = " ")
        



####Test
##print_numbers(10, 25)
##print()
##print_numbers(25, 20)
##print()
##print_numbers(9, 33)
##print()


##Q3_revision
def get_list_of_non_negative_evens(numbers_list):
    new_list = []
    for index in range(len(numbers_list)):
        if numbers_list[index] >= 0 and numbers_list[index] % 2 == 0:
            new_list.append(numbers_list[index])

    return new_list


##Test
##print(get_list_of_non_negative_evens([51, -55, 56, 23, 23, 54]))
##print(get_list_of_non_negative_evens([46, 26, 24, -44, -20]))


##Q4_revision
def get_count_same_start_end(numbers_list):
    count = 0
    str_list = []

    for index in range(len(numbers_list)):
        str_number = str(numbers_list[index])
        if str_number[0] == str_number[-1]:
            count +=1

    return count


        



##Test
##print(get_count_same_start_end([313, 636, 2042, 40, 447]))
##print(get_count_same_start_end([101, 4559, 241, 124, 9249]))

##Q5_revision
def print_longest_word(word_list):
    update_str = ""

    for index in range(len(word_list)):
        word = word_list[index]
        if len(word) >= len(update_str):
            update_str = word
            
    print(update_str)
            



##Test
##print_longest_word(['fish', 'barrel', 'like', 'shooting', 'in', 'a'])
##print_longest_word(['cat', 'the', 'the', 'bag', 'let', 'out', 'of'])
##print_longest_word(['the', 'the', 'bag', 'let', 'out', 'of', 'cat'])



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
    



##Test
print(contains_only_3_digit_numbers([117, -241, -171, 112, 317, 290, 77, 394]))
print(contains_only_3_digit_numbers([-491, -375, -65, -348]))
print(contains_only_3_digit_numbers([-716, -948, -636, 595, 179, -708, 867, -173]))















