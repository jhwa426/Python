""" Use this file to develop and test your Assignment 4 function 1"""

#--------------------------------------------------
# 1111111111111111111111111111111111111111111111111
# get_dictionary_from_file()
#--------------------------------------------------
def get_dictionary_from_file(filename):
    input_file = open(filename, "r")
    contents = input_file.read()
    input_file.close()
    word_list = contents.split("\n")
    name_dic = {}
    
    for index in word_list:
        position = index.find(" : ")
        key = index[:position]
        name_dic[key] = index[position+3:]

    return name_dic
        



def main():
    print_header(1, "test_get_dictionary_from_file()")
    the_dict = get_dictionary_from_file("WordsAndMeanings1.txt")
    for word in ["lickspittle", "allegator", "lickety-split"]:
        if word in the_dict:
            print(word, "=", the_dict[word])
    print()

    the_dict = get_dictionary_from_file("WordsAndMeanings2.txt")
    for word in ["ranivorous", "cat", "rigmarole"]:
        if word in the_dict:
            print(word, "=", the_dict[word])
    print()

    the_dict = get_dictionary_from_file("WordsAndMeanings3.txt")
    for word in ["gastromancy", "allegator", "gazump"]:
        if word in the_dict:
            print(word, "=", the_dict[word])

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

