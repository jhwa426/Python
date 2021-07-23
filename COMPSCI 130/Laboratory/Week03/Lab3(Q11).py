##Ex 11

##From Ex1
def read_content(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split("\n")
    input_file.close()
        
    return contents

##From Ex2
def get_tag_words(line):
    position = line.find(":")
    first_word = line[:position]
    second_word = line[position+1:].split()
    second_word.sort()

    return (first_word, second_word)

##From Ex3
def create_tags_dictionary(filename):
    input_file = read_content(filename)
    new_dic = {}
    for word in input_file:
        a_dic = get_tag_words(word)
        key = a_dic[0]
        value = a_dic[1]
        new_dic[key] = value
    return new_dic

##From Ex4
def get_sorted_unique_words_list(sentence):
    word_list = sentence.lower()
    word_list = word_list.split()
    a_list = []
    
    for word in word_list:
        if word not in a_list:
            a_list.append(word)

    return sorted(a_list)

##From Ex5
def get_word_tag_tuple(tags_dictionary, search_word):
    for word,word_list in tags_dictionary.items():
        if search_word in word_list:
            return search_word,word
        
##From Ex6
def get_tag_tuple_list(tags_dictionary, sentence):
    a_list = []
    word_list = get_sorted_unique_words_list(sentence) #['summer']

    for word in word_list:
        tag = get_word_tag_tuple(tags_dictionary, word)
        a_list.append(tag)

    return a_list

##From Ex7
def get_tags_frequency(list_of_tuples):
    a_dic = {}
    a_list = []
    
    for word in range(len(list_of_tuples)):
        value = list_of_tuples[word][1]
        a_list.append(value)

    count = 1
        
    for check in a_list:
        if check in a_dic:
            a_dic[check] = a_dic[check] + count
        else:
            a_dic[check] = count

    return a_dic

##From Ex8
def print_dictionary(tags_dictionary):
    for key in sorted(tags_dictionary.keys()):
        print(key, tags_dictionary[key])
        
##From Ex10
import random

def print_random_phrase(tags_dictionary):
    for word in sorted(tags_dictionary):
        if word == "DT":
            position = random.randrange(len(tags_dictionary["DT"]))
            key1 = tags_dictionary["DT"][position]
            
        elif word == "JJ":
            position = random.randrange(len(tags_dictionary["JJ"]))
            key2 = tags_dictionary["JJ"][position]
            
        elif word == "NN":
            position = random.randrange(len(tags_dictionary["NN"]))
            key3 = tags_dictionary["NN"][position]
            
    space = " "  
    result = key1 + space + key2 + space + key3
    
    print(result)

##def print_random_phrase(tags_dictionary):
##
##    position = random.randrange(len(tags_dictionary["DT"]))
##    key1 = tags_dictionary["DT"][position]
##            
##    position = random.randrange(len(tags_dictionary["JJ"]))
##    key2 = tags_dictionary["JJ"][position]
##            
##    position = random.randrange(len(tags_dictionary["NN"]))
##    key3 = tags_dictionary["NN"][position]
##            
##    space = " "  
##    result = key1 + space + key2 + space + key3
##    print(result)
    

##Ex 11
        
##Test        
##simple_tags.txt
##The grass is brown the grass is dry
        
text_input = input("Enter a filename: ")
read_contents = create_tags_dictionary(text_input) #Q3
sentence_input = input("Enter a sentence: ")
tag_tuple = get_tag_tuple_list(read_contents, sentence_input) #Q6
counting_number = get_tags_frequency(tag_tuple) #Q7
print_dictionary(counting_number) #Q8
print_random_phrase(read_contents) #Q10




