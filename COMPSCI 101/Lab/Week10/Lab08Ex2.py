"""
Lab 8 Ex 2
Author:
Date: May, 2020
This program creates a baby names dictionary 
"""
def main():
    filename = get_filename_from_user()
    names = get_list_of_names(filename)
    baby_names_dictionary = create_baby_names_dict(names)
    display_baby_names(baby_names_dictionary)

##def get_filename_from_user():
##    filename = input("Enter a filename: ")
##    return filename
##
##def get_list_of_names(filename):
##    input_file = open(filename, "r")
##    contents = input_file.read()
##    input_file.close()
##    word_list = contents.split()
##    return word_list
##
##def create_baby_names_dict(names_list):
##    name_dic = {}
##
##    for index in range(len(names_list)):
##        value_name = names_list[index]
##        key = value_name[0]
##        name_dic[key] = value_name
##
##    return name_dic
##
##def display_baby_names(baby_names_dictionary):
##    for key in baby_names_dictionary:
##        print(key,baby_names_dictionary[key] + ", ", end = "")

##Q2_revision
def get_filename_from_user():
    user_input = input("Enter a letter: ")
    return user_input


def get_list_of_names(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split()
    input_file.close()
    return contents

def create_baby_names_dict(names_list):
    name_dic = {}
    for name in names_list:
        key = name[0]
        value = name
        name_dic[key] = value
    return name_dic

def display_baby_names(baby_names_dictionary):
    for key in baby_names_dictionary:
        print(key, baby_names_dictionary[key],end = ", ")
        
main()

## baby_boy_names.txt
