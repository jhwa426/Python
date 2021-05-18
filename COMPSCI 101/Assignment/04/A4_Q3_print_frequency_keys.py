""" Use this file to develop and test your Assignment 4 function 3"""

#--------------------------------------------------
#33333333333333333333333333333333333333333333333333
# print_highest_frequency_keys()
#--------------------------------------------------
def print_highest_frequency_keys(frequency_dict, key_length):
    print_list = []
    biggest_so_far = 0
    for key in frequency_dict:
        value = frequency_dict[key]
        if len(key) == key_length:
            if value > biggest_so_far:
                biggest_so_far = value
                print_list.append(key)
            elif value == biggest_so_far:
                print_list.append(key)
                
    print_list.sort()          
    print(key_length,"letter keys:",print_list,biggest_so_far)
                   
def main():
    print_header(3, "print_highest_frequency_keys()")
    word_frequencies = {"fish":9,  "parrot":8,  "frog":9,  "cat":9,  "stork":1,  "dog":4, "bat":9,  "rat":3}
    print_highest_frequency_keys(word_frequencies, 3)
    print_highest_frequency_keys(word_frequencies, 4)
    print_highest_frequency_keys(word_frequencies, 7)

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
