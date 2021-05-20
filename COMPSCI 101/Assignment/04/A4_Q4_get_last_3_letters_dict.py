""" Use this file to develop and test your Assignment 4 function 4"""

#--------------------------------------------------
# 4444444444444444444444444444444444444444444444444
# get_last_three_letters_dict(text)
#--------------------------------------------------
def get_last_three_letters_dict(text):
    a_dic = {}
    there_letters_list = []
    contents = text.split()

    for letter in contents:
        if len(letter) > 2:
            there_letters_list.append(letter[-3:])
        
    for three in there_letters_list:
        if three not in a_dic.keys():
            a_dic[three] = 1
            
        else:
            a_dic[three] = a_dic[three] + 1
            
    return a_dic


def main():
    print_header(4, "get_last_three_letters_dict()")
    text = 'nubile singer linger finger juvenile tiger turnstile mobile tile'
    a_dict = get_last_three_letters_dict(text)
    remove_less_than_2(a_dict)
    print_dict_in_key_order(a_dict)
    print()

    text = 'west best worst first tapping snapping in a pest the straining singing forest living'
    a_dict = get_last_three_letters_dict(text)
    remove_less_than_2(a_dict)
    print_dict_in_key_order(a_dict)
    print()

    text = 'to do or a at'
    a_dict = get_last_three_letters_dict(text)
    remove_less_than_2(a_dict)
    print_dict_in_key_order(a_dict)

#--------------------------------------------------
# Two helper functions
#--------------------------------------------------
def print_dict_in_key_order(a_dict):
    all_keys = list(a_dict.keys())
    all_keys.sort()
    for key in all_keys:
        print(key, ":", a_dict[key])

def remove_less_than_2(a_dict):
    all_keys = list(a_dict.keys())
    for key in all_keys:
        if a_dict[key] == 1:
            del a_dict[key]
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
