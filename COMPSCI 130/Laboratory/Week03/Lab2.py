##Lab2_A
 
##Ex 1
##def read_content(filename):
##    input_file = open(filename, "r")
##    contents = input_file.read().split("\n")
##    input_file.close()
##        
##    return contents


####Test
##lines = read_content('two_lines.txt')
##print(lines)
##print(len(lines))

##Ex 2
##def get_tag_words(line):
##    position = line.find(":")
##    first_word = line[:position]
##    second_word = line[position+1:].split()
##    second_word.sort()
##
##    return (first_word, second_word)


####Test
##line='CD:five one seven'
##print(get_tag_words(line))

##Ex 3

##def create_tags_dictionary(filename):
##    input_file = read_content(filename)
##    new_dic = {}
##    for word in input_file:
##        a_dic = get_tag_words(word)
##        key = a_dic[0]
##        value = a_dic[1]
##        new_dic[key] = value
##    return new_dic
        
        

##Test
##tags = create_tags_dictionary('two_lines.txt')
##for key in sorted(tags):
##    print(key, tags[key])


##Ex 4
######## double check!!!!!!!!!
##def get_sorted_unique_words_list(sentence):
##    word_list = sentence.lower()
##    word_list = word_list.split()
##    a_list = []
##    
##    for word in word_list:
##        if word not in a_list:
##            a_list.append(word)
##
##    return sorted(a_list)
##
####Test
##print(get_sorted_unique_words_list('Summer IS over'))
##print(get_sorted_unique_words_list('His father was a shoemaker and his mother a washerwoman'))
##['a', 'and', 'father', 'his', 'mother', 'shoemaker', 'was', 'washerwoman']

##Ex 5
##def get_word_tag_tuple(tags_dictionary, search_word):
##    for word,word_list in tags_dictionary.items():
##        if search_word in word_list:
##            return search_word,word


####Test
##tags_dictionary = {'CC': ['and', 'but', 'or'], 'CD': ['five', 'one', 'seven'], 'DT': ['a', 'all', 'the'], 'IN': ['after', 'around', 'at', 'for', 'in', 'of', 'over', 'that', 'with'], 'JJ': ['brown', 'dry', 'first', 'hot', 'last', 'other', 'poor', 'ready', 'real', 'rough', 'strange', 'tiny'], 'JJS': ['nest'], 'MD': ['would'], 'NN': ['closing', 'denmark', 'doll', 'dreamer', 'everything', 'father', 'fun', 'grass', 'hole', 'lanky', 'mother', 'odense', 'play', 'rain', 'room', 'shoemaker', 'spring', 'summer', 'theatre', 'tortoise', 'town', 'toy', 'washerwoman', 'yard', 'year'], 'NNS': ['books', 'boys', 'bushes', 'days', 'dolls', 'duties', 'eggs', 'hans', 'hours', 'legs', 'plays', 'shrubs', 'stories', 'trees', 'waits'], 'PDT': ['half'], 'PRP': ['he', 'him', 'it', 'she', 'them', 'they'], 'PRP$': ['her', 'his'], 'RB': ['alone', 'carefully', 'even', 'fully', 'magic', 'never', 'not', 'now', 'only', 'so'], 'RP': ['up'], 'TO': ['to'], 'VB': ['be', 'bother', 'hatch', 'make', 'sit'], 'VBD': ['did', 'had', 'invented', 'left', 'liked', 'made', 'prepared', 'saw', 'was', 'were'], 'VBG': ['autumn', 'being', 'concealing', 'playing', 'reading'], 'VBN': ['been', 'born', 'developed', 'ended', 'entranced', 'found', 'gone', 'loved', 'parched', 'played'], 'VBP': ['are'], 'VBZ': ['hans', 'has', 'is'], 'WRB': ['when']}
##print(get_word_tag_tuple(tags_dictionary, 'summer')) ##('summer', 'NN')


##Ex 6
##def get_tag_tuple_list(tags_dictionary, sentence):
##    a_list = []
##    word_list = get_sorted_unique_words_list(sentence) #['summer']
##
##    for word in word_list:
##        tag = get_word_tag_tuple(tags_dictionary, word)
##        a_list.append(tag)
##
##    return a_list
    
    
            

####Test
##tags_dictionary = {'CC': ['and', 'but', 'or'], 'CD': ['five', 'one', 'seven'], 'DT': ['a', 'all', 'the'], 'IN': ['after', 'around', 'at', 'for', 'in', 'of', 'over', 'that', 'with'], 'JJ': ['brown', 'dry', 'first', 'hot', 'last', 'other', 'poor', 'ready', 'real', 'rough', 'strange', 'tiny'], 'JJS': ['nest'], 'MD': ['would'], 'NN': ['closing', 'denmark', 'doll', 'dreamer', 'everything', 'father', 'fun', 'grass', 'hole', 'lanky', 'mother', 'odense', 'play', 'rain', 'room', 'shoemaker', 'spring', 'summer', 'theatre', 'tortoise', 'town', 'toy', 'washerwoman', 'yard', 'year'], 'NNS': ['books', 'boys', 'bushes', 'days', 'dolls', 'duties', 'eggs', 'hans', 'hours', 'legs', 'plays', 'shrubs', 'stories', 'trees', 'waits'], 'PDT': ['half'], 'PRP': ['he', 'him', 'it', 'she', 'them', 'they'], 'PRP$': ['her', 'his'], 'RB': ['alone', 'carefully', 'even', 'fully', 'magic', 'never', 'not', 'now', 'only', 'so'], 'RP': ['up'], 'TO': ['to'], 'VB': ['be', 'bother', 'hatch', 'make', 'sit'], 'VBD': ['did', 'had', 'invented', 'left', 'liked', 'made', 'prepared', 'saw', 'was', 'were'], 'VBG': ['autumn', 'being', 'concealing', 'playing', 'reading'], 'VBN': ['been', 'born', 'developed', 'ended', 'entranced', 'found', 'gone', 'loved', 'parched', 'played'], 'VBP': ['are'], 'VBZ': ['hans', 'has', 'is'], 'WRB': ['when']}
##print(get_tag_tuple_list(tags_dictionary, 'SUMMER'))

##Ex 7

####Method 1
##def get_tags_frequency(list_of_tuples):
##    a_dic = {}
##    a_list = []
##    
##    for word in range(len(list_of_tuples)):
##        key = list_of_tuples[word][0]
##        value = list_of_tuples[word][1]
##        a_list.append(value)
##
##    for check in a_list:
##        a_dic[check] = a_list.count(check)
##
##    return a_dic


####Method 2
##def get_tags_frequency(list_of_tuples):
##    a_dic = {}
##    a_list = []
##    
##    for word in range(len(list_of_tuples)):
##        value = list_of_tuples[word][1]
##        a_list.append(value)
##
##    count = 1
##        
##    for check in a_list:
##        if check in a_dic:
##            a_dic[check] = a_dic[check] + count
##        else:
##            a_dic[check] = count
##
##    return a_dic

####Test
##list_of_tuples = [('summer', 'NN'), ('the', 'DT'), ('hot', 'JJ')]
##freq_dict = get_tags_frequency(list_of_tuples)
##for key in sorted(freq_dict.keys()):
##    print(key, freq_dict[key])
##print()

##list_of_tuples = [('a', 'DT'), ('and', 'CC'), ('father', 'NN'), ('his', 'PRP$'), ('mother', 'NN'), ('shoemaker', 'NN'), ('was', 'VBD'), ('washerwoman', 'NN')]
##freq_dict = get_tags_frequency(list_of_tuples)
##for key in sorted(freq_dict.keys()):
##    print(key, freq_dict[key])



##Ex 8
##def print_dictionary(tags_dictionary):
##    for key in sorted(tags_dictionary.keys()):
##        print(key, tags_dictionary[key])
        

##Test
##tags_dictionary = {'DT': 1, 'JJ': 1, 'NN': 1}
##print_dictionary(tags_dictionary)

##Ex 9
##def print_all_phrases(tags_dictionary):
##    max_number = 0
##    for max_value in tags_dictionary.values():
##        if len(max_value) > max_number:
##            max_number = len(max_value)
##    print(max_number)

##def print_all_phrases(tags_dictionary):
##    for first in tags_dictionary["DT"]:
##        for second in tags_dictionary["JJ"]:
##            for third in tags_dictionary["NN"]:
##                print(first, second, third)
##
##
####Test
##tags = {'JJ': ['brown'], 'NN': ['grass', 'summer'], 'DT': ['the']}
##print_all_phrases(tags)
##
##tags = {'DT': ['a'], 'NN': ['father', 'mother', 'room', 'shoemaker', 'washerwoman'], 'JJ': ['poor']}
##print_all_phrases(tags)

##Ex 10
import random

##def print_random_phrase(tags_dictionary):
##    for word in sorted(tags_dictionary.items()):
##        value = word[1]
##        position = random.randrange(len(value))
##        print(value[position], end =" ")

def print_random_phrase(tags_dictionary):
    count = 0
    for word in sorted(tags_dictionary.items()):
        value = word[1]
        position = random.randrange(0,len(word[0]))
        
        if count < 3 :
            print(value[position], end =" ")
        count = count + 1

##def print_random_phrase(tags_dictionary):
##    for word in sorted(tags_dictionary):
##        if word == "DT":
##            position = random.randrange(len(tags_dictionary["DT"]))
##            key1 = tags_dictionary["DT"][position]
##            
##        elif word == "JJ":
##            position = random.randrange(len(tags_dictionary["JJ"]))
##            key2 = tags_dictionary["JJ"][position]
##            
##        elif word == "NN":
##            position = random.randrange(len(tags_dictionary["NN"]))
##            key3 = tags_dictionary["NN"][position]
##            
##    space = " "  
##    result = key1 + space + key2 + space + key3
##    
##    print(result)

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


##Test
tags = {'JJ': ['brown', 'yellow'], 'NN': ['grass', 'summer'], 'DT': ['the', 'a']}
print_random_phrase(tags)
##
####tags = {'JJ': ['brown', 'yellow'], 'NN': ['grass', 'summer'], 'DT': ['the', 'a'], "DD" : ["seven", "a"]}
####print_random_phrase(tags)
