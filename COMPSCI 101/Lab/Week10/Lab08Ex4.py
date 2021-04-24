"""
Lab 8 Ex 4
Author:
Date: May, 2020
This program reads in a file of baby names and
prints a list of baby names by initial letter
"""
def main():
    filename = get_filename_from_user()
    names = get_list_of_names(filename)
    baby_name_dictionary = create_baby_names_dictionary(names)
    display_baby_names(baby_name_dictionary)

def get_filename_from_user():
    filename = input("Enter a filename: ")
    return filename
    
##def get_list_of_names(filename):
##    input_file = open(filename, "r")
##    contents = input_file.read()
##    input_file.close()
##    word_list = contents.split()
##    word_list.sort()
##    return word_list
##
##
##def create_baby_names_dictionary(names_list):
##    name_dic = {}
##
##    for value_name in names_list:
##        key_letter = value_name[0]
##
##        if key_letter in name_dic:
##            name_dic[key_letter].append(value_name)
##            
##        elif value_name not in name_dic:
##            name_dic[key_letter] = [value_name]
##            
##    return name_dic
##
##
##def display_baby_names(baby_names_dict):
##    for key in baby_names_dict:
##        print(key,": ",sep="", end="")
##        names_list = baby_names_dict[key]
##        for value in range(len(names_list)):
##            print(names_list[value],end = " ")
##        print()
        
##Q4_revision
def get_list_of_names(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split()
    input_file.close()
    return sorted(contents)

def create_baby_names_dictionary(names_list):
    name_dic = {}
    
    for name in names_list:
        key = name[0]
        if key in name_dic:
            name_dic[key].append(name)
        elif name not in name_dic:
            name_dic[key] = [name]

    return name_dic



def display_baby_names(baby_names_dict):
    for key in baby_names_dict:
        print("{}: ".format(key), sep="", end = "")
        names_list = baby_names_dict[key]
        for value in range(len(names_list)):
            print(names_list[value],end = " ")
        print()
        
## 2019Top_boy_names.txt
        
main()



