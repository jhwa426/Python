""" Use this file to develop and test your Assignment 4 function 5"""

#--------------------------------------------------
# 5555555555555555555555555555555555555555555555555
# remove_nines()
#--------------------------------------------------
def remove_nines(numbers_dict):
    for the_key in numbers_dict:
        new_list = []
        a_list = numbers_dict[the_key] #value
        for nine in a_list:
            if str(9) not in str(nine):
                new_list.append(nine)
        numbers_dict[the_key] = new_list
        
    

def main():
    print_header(5, "remove_nines()")
    word_numbers_dict = {"fish": [9, 89, 76],  "rat":[2, 891, 4], 'dog' : []}
    remove_nines(word_numbers_dict)
    print_dict_in_key_order(word_numbers_dict)
    print()

    word_numbers_dict = {"bird": [9, 8770, 79],  "parrot":[9, 492, 7691],  "bat":[24, 839, 16],  "cat":[2, 871, 4]}
    remove_nines(word_numbers_dict)
    print_dict_in_key_order(word_numbers_dict)

    word_numbers_dict = {"fish": [2],  "parrot":[9, 429, 9, 9],  "bull":[3],  "cat":[],  "stork":[6, 14, 2]}
    remove_nines(word_numbers_dict)
    print_dict_in_key_order(word_numbers_dict)
#--------------------------------------------------
# A helper function
#--------------------------------------------------
def print_dict_in_key_order(a_dict):
    all_keys = list(a_dict.keys())
    all_keys.sort()
    for key in all_keys:
        print(key, ":", a_dict[key])
#--------------------------------------------------
#Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()
