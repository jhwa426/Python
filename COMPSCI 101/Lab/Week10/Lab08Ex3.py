"""
Lab 8 Ex 3
Author:
Date: May, 2020
This program produces a summary of the top 10 baby names
"""
def main():
    filename = get_filename_from_user()
    names = get_list_of_names(filename)
    name_count_dictionary = create_names_count_dictionary(names)
    produce_name_counts_report(name_count_dictionary)

def get_filename_from_user():
    filename = input("Enter a filename: ")
    return filename

def get_list_of_names(filename):
    input_file = open(filename, "r")
    contents = input_file.read()
    input_file.close()
    word_list = contents.split()
    word_list.sort()
    return word_list

####def create_names_count_dictionary(names_list):
####    name_dic = {}
####    count = 0
####    for index in names_list:
####        key_name = index
####        if key_name in names_list:
####            count = names_list.count(key_name)
####            name_dic[key_name] = count
####    return name_dic
##
####Very important
##def create_names_count_dictionary(names_list):
##    name_dic = {}
##
##    for name in names_list:
##        if name not in name_dic.keys():
##            name_dic[name] = 1
##        else:
##            name_dic[name] = name_dic[name] + 1
##     
##    return name_dic
##            
##def produce_name_counts_report(name_counts_dict):
##    print("Report")
##    print("======")
##    for key in name_counts_dict:
##        print(key,"appears", name_counts_dict[key], "times")

##Q3_revision
def get_list_of_names(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split()
    input_file.close()
    return sorted(contents)

def create_names_count_dictionary(names_list):
    name_dic = {}
    
    for name in names_list:
        if name not in name_dic:
            name_dic[name] = 1
        else:
            name_dic[name] += 1

    return name_dic

def produce_name_counts_report(name_counts_dict):
    print("Report")
    print("======")
    for key in name_counts_dict:
        print("{} appears {} times".format(key, name_counts_dict[key]))
        
main()

## top10_boy_names.txt

