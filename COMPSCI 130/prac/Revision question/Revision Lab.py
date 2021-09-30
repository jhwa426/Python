##Revision Lab
##Lab 1A

##Ex 3
##input_user = input("Enter a sentence: ")
##
##for word in range(len(input_user)):
##    word = input_user[word]
##
##    if word.islower():
##        print(word.upper(), end = "")
##    else:
##        print(word.lower(), end = "")
##
####Test
####Michael


##Ex 4
##input_word = input("Enter a word: ")
##input_another = input("Enter another word: ")
##
##word_list = []
##another_list = []
##
##for word in range(len(input_word)):
##    word = input_word[word]
##    word_list.append(word)
##
##word_list.sort()
##
##for word in range(len(input_another)):
##    word = input_another[word]
##    another_list.append(word)
##
##another_list.sort()
##
##if word_list == another_list:
##    result1 = input_word + " and " + input_another + " are anagrams of each other."
##    print(result1)
##else:
##    result2 = input_word + " and " + input_another + " are not anagrams of each other."
##    print(result2)

##Ex 5
##for number in range(200, 300):
##    if number % 3 != 0 and number % 5 == 0:
##        if number == 295:
##            print(number, end ="")
##        else:
##            print(number, end = ",")

##Ex 6
##user_input = int(input("Enter a number: "))
##a_list = []
##
##while user_input != -999:
##    a_list.append(user_input)
##    user_input = int(input("Enter a number: "))
##
##print(a_list)

##Ex 7
##user_input = int(input("Enter number of rows: "))
##
##for row in range(1, user_input + 1):
##    for column in range(1, row + 1):
##        print(column, end = " ")
##    print()

##Ex 8

##user_input = int(input("Enter number of rows: "))
##
##for row in range(1, user_input + 1):
##    if row == 1 or row == user_input:
##        print("*" * user_input)
##    else:
##        for column in range(1, user_input + 1):
##            if column == 1:
##                print("*",end = "")
##            elif column == user_input:
##                print("*",end = "")
##            elif column == row:
##                print("*",end = "")
##            elif column == (user_input - row) + 1:
##                print("*",end = "")
##            else:
##                print(" ",end = "")
##            
##        print("")

##Ex 9
##user_input = int(input("Enter an integer: "))
##a_tuple = ()
##
##for number in range(1, user_input + 1):
##    a_tuple += number,
##
##print(a_tuple)

##Ex 10
##user_input = input("Enter a word: ")
##
##a_list = []
##a_dic = {}
##
##for word in range(len(user_input)):
##    letter = user_input[word]
##    ascii_code = ord(letter)
##    a_dic[letter] = ascii_code
##
##for key in sorted(a_dic):
##    print(key, ":", a_dic[key], sep="")


###Lab 1B

##Ex 1
##input_number = int(input("Enter an integer: "))
##filename = input("Enter a filename: ")
##
##input_file = open(filename, "r")
##contents = input_file.read()
##word_list = contents.split()
##input_file.close()
##
##count =0
##for word in word_list:
##    if int(word) % input_number == 0:
##        count += 1
##
##if count <= 1:
##    print ("There is {} multiple of {} in the '{}' file.".format(str(count),str(input_number),filename))
##else:
##    print("There are {} multiple of {} in the '{}' file.".format(str(count),str(input_number),filename))

    
##Test
##basic_numbers.txt

##Ex 2
##filename = input("Enter filename: ")
##input_file = open(filename, "r")
##contents = input_file.read()
##word_list = contents.split()
##input_file.close()
##
##length = 0
##
##for word in word_list:
##    if len(word) >= length:
##        length = len(word)
##        letter = word
##
##result = 'The longest word is "'"{}"'"'.format(letter)
##print(result)

##Ex 3
##def get_first4(items):
##    return (items[:4])
##
##def get_first4(items):
##    a_list = []
##    for number in items:
##        if len(a_list) <= 3:
##            a_list.append(number)
##
##    return a_list
##
####Test
##print(get_first4([15,14,31,20,8,23,34,42,22,26])) #[15, 14, 31, 20]


##Ex 4
##def get_sum_positive_even(numbers):
##    even_sum = 0
##    for number in numbers:
##        if number >= 0 and number % 2 ==0:
##            even_sum += number
##    return even_sum
##
##
##
####Test
##print (get_sum_positive_even([1,2,3,4,5,-1,-9])) #6
##print (get_sum_positive_even([1,3,5,7]))
##print (get_sum_positive_even([]))
 

##Ex 5
##def get_multiples_of_5(numbers):
##    a_list = []
##    for number in numbers:
##        if number % 5 == 0:
##            a_list.append(number)
##    return a_list
##
##
####Test
##print(get_multiples_of_5([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 25])) #[5, 25]
##print(get_multiples_of_5([4, 5, 2, 22, 71, 30]))

##Ex 6
##def count_consonants(word):
##    vowel = "aeiouAEIOU"
##    count = 0
##    for letter in word:
##        if letter not in vowel:
##            count += 1
##    return count
##
##
####Test
##print(count_consonants('Hello')) #3
##print(count_consonants('Abracadabra')) #6

##Ex 7
##def unique_species(animal_species):
##    a_list = []
##    values = animal_species.values()
##
##    for word in values:
##        if word not in a_list:
##            a_list.append(word)
##    return sorted(a_list)
##
####Test
##animal_species={1007:"Meerkat",2091:"Cheetah",13:"Cheetah"}
##result=unique_species(animal_species)
##print(result)

##Ex 8
##def print_keys_values_inorder(dictionary):
##    for word in sorted(dictionary):
##        key = word
##        value = dictionary[word]
##        print(key, " ".join(value))
##
####Test
##my_dict = {6:['monday', 'coffee', 'strong'], 5:['short'], 3:['may', 'and']}
##print_keys_values_inorder(my_dict)
####3 and may
####5 short
####6 coffee monday strong

##Ex 9
##filename = input("Enter the English to Maori dictionary filename: ")
##word_name = input("Enter an English word: ")
##
##input_file = open(filename, "r")
##contents = input_file.read()
##word_list = contents.split()
##input_file.close()
##
##name_dic = {}
##
##for word in word_list:
##    position = word.find(":")
##    initial_word = word[:position]
##    translated_word = word[position+1:]
##    
##    name_dic[initial_word] = translated_word
##
##if word_name in name_dic.keys():
##    print("'"'{}'"' is translated into '"'{}'"'.".format(word_name,name_dic[word_name]))
##elif word_name not in name_dic.keys():
##    print("Sorry that word doesn't exist in Maori!")
##
##    
##
####Test
#####english_to_maori.txt
######house


##Ex 10
##a_dic = {}
##input_word = input("Enter a sentence: ")
##word_list = set(input_word.split())
##
##for word in word_list:
##    key = len(word)
##    if key not in a_dic:
##        a_dic[key] = [word.lower()]
##    else:
##        a_dic[key].append(word.lower())
##
##   
##for key in sorted(a_dic):
##    print(key," ".join(a_dic[key]))
##
##
####Test
######May your coffee be strong and your Monday be short


#####Lab 2

####Ex 1
##def read_content(filename):
##    input_file = open(filename, "r")
##    contents = input_file.read().split("\n")
##    input_file.close()
##    return contents


####Test
##lines = read_content('two_lines.txt')
##print(lines)
##print(len(lines))

####Ex 2
##def get_tag_words(line):
##    position = line.find(":")
##    key = line[:position]
##    value = line[position+1:].split(" ")
##
##    return (key, value)


####Test
##line='CD:five one seven'
##print(get_tag_words(line)) #('CD', ['five', 'one', 'seven'])

####Ex 3
##def create_tags_dictionary(filename):
##    a_dic = {}
##    input_file = read_content(filename)
##
##    for word in input_file:
##        word = get_tag_words(word)
##        key = word[0]
##        value = word[1]
##        a_dic[key] = value
##    return a_dic


##tags = create_tags_dictionary('two_lines.txt')
##for key in sorted(tags):
##    print(key, tags[key])

####Ex 4
##def get_sorted_unique_words_list(sentence):
##    sentence = sentence.lower()
##    sentence = set(sentence.split())
##    return sorted(sentence)


####Test
##print(get_sorted_unique_words_list('Summer IS over')) #['is', 'over', 'summer']
##print(get_sorted_unique_words_list('Summer is over and the hot days are gone The grass is brown'))

###Ex 5
##def get_word_tag_tuple(tags_dictionary, search_word):
##    for key, value in tags_dictionary.items():
##        if search_word in value:
##            return search_word, key

##Test
##tags_dictionary = {'NN': ['dreamer', 'father', 'fun', 'grass', 'mother', 'odense', 'rain',
##                          'shoemaker', 'spring', 'summer', 'tortoise', 'toy', 'washerwoman']}
##print(get_word_tag_tuple(tags_dictionary, 'summer')) ##('summer', 'NN')

###Ex 6
##def get_tag_tuple_list(tags_dictionary, sentence):
##    a_list = []
##    word_list = get_sorted_unique_words_list(sentence)
##    
##    for word in word_list:
##        tag = get_word_tag_tuple(tags_dictionary,word)
##        a_list.append(tag)
##        
##    return a_list
        
##Test
####Test
##tags_dictionary = {'CC': ['and', 'but', 'or'], 'CD': ['five', 'one', 'seven'], 'DT': ['a', 'all', 'the'], 'IN': ['after', 'around', 'at', 'for', 'in', 'of', 'over', 'that', 'with'], 'JJ': ['brown', 'dry', 'first', 'hot', 'last', 'other', 'poor', 'ready', 'real', 'rough', 'strange', 'tiny'], 'JJS': ['nest'], 'MD': ['would'], 'NN': ['closing', 'denmark', 'doll', 'dreamer', 'everything', 'father', 'fun', 'grass', 'hole', 'lanky', 'mother', 'odense', 'play', 'rain', 'room', 'shoemaker', 'spring', 'summer', 'theatre', 'tortoise', 'town', 'toy', 'washerwoman', 'yard', 'year'], 'NNS': ['books', 'boys', 'bushes', 'days', 'dolls', 'duties', 'eggs', 'hans', 'hours', 'legs', 'plays', 'shrubs', 'stories', 'trees', 'waits'], 'PDT': ['half'], 'PRP': ['he', 'him', 'it', 'she', 'them', 'they'], 'PRP$': ['her', 'his'], 'RB': ['alone', 'carefully', 'even', 'fully', 'magic', 'never', 'not', 'now', 'only', 'so'], 'RP': ['up'], 'TO': ['to'], 'VB': ['be', 'bother', 'hatch', 'make', 'sit'], 'VBD': ['did', 'had', 'invented', 'left', 'liked', 'made', 'prepared', 'saw', 'was', 'were'], 'VBG': ['autumn', 'being', 'concealing', 'playing', 'reading'], 'VBN': ['been', 'born', 'developed', 'ended', 'entranced', 'found', 'gone', 'loved', 'parched', 'played'], 'VBP': ['are'], 'VBZ': ['hans', 'has', 'is'], 'WRB': ['when']}
##print(get_tag_tuple_list(tags_dictionary, 'SUMMER'))
##print(get_tag_tuple_list(tags_dictionary, 'Summer IS over'))
##print(get_tag_tuple_list(tags_dictionary, 'His father was a shoemaker and his mother a washerwoman'))


##Ex 7
##def get_tags_frequency(list_of_tuples):
##    values = []
##    a_dic = {}
##    for word in range(len(list_of_tuples)):
##        value = list_of_tuples[word][1]
##        values.append(value)
##
##    count = 1
##
##    for check in values:
##        if check in a_dic:
##            a_dic[check] += count
##        else:
##            a_dic[check] = count
##            
##    return a_dic
    

##Test
##list_of_tuples = [('summer', 'NN'), ('the', 'DT'), ('hot', 'JJ')]
##freq_dict = get_tags_frequency(list_of_tuples)
##for key in sorted(freq_dict.keys()):
##    print(key, freq_dict[key])
##
####DT 1
####JJ 1
####NN 1
    
##list_of_tuples = [('a', 'DT'), ('and', 'CC'), ('father', 'NN'), ('his', 'PRP$'), ('mother', 'NN'), ('shoemaker', 'NN'), ('was', 'VBD'), ('washerwoman', 'NN')]
##freq_dict = get_tags_frequency(list_of_tuples)
##for key in sorted(freq_dict.keys()):
##    print(key, freq_dict[key])
    
##Ex 8
##def print_dictionary(tags_dictionary):
##    for key in sorted(tags_dictionary):
##        print(key, tags_dictionary[key])
##    
##
##tags_dictionary = {'DT': 1, 'JJ': 1, 'NN': 1}
##print_dictionary(tags_dictionary)

##Ex 9
##def print_all_phrases(tags_dictionary):
##    for first in tags_dictionary["DT"]:
##        for second in tags_dictionary["JJ"]:
##            for third in tags_dictionary["NN"]:
##                print(first, second, third)
##                
##tags = {'JJ': ['brown'], 'NN': ['grass', 'summer'], 'DT': ['the']}
##print_all_phrases(tags)
##print()
##tags = {'DT': ['a'], 'NN': ['father', 'mother', 'room', 'shoemaker', 'washerwoman'], 'JJ': ['poor']}
##print_all_phrases(tags)



##Ex 10
##import random
##
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
##    return print("{} {} {}".format(key1,key2,key3))
##
##tags = {'JJ': ['brown', 'yellow'], 'NN': ['grass', 'summer'], 'DT': ['the', 'a']}
##print_random_phrase(tags)


#####Lab 3

##Ex 6
##def remove_letters(word1, word2):
##    result = list(word2)
##    for letter in word1:
##        if letter in result:
##            result.remove(letter)
##    return ''.join(result)
##
##
##
##print(remove_letters('hello', 'world')) #wrd
##print(remove_letters('world', 'hello')) #hel


##Ex 7
##def get_index_of_largest(numbers):
##    if len(numbers) == 0:
##        return -1
##    
##    max_value = numbers[0]
##    for num in numbers:
##        if num > max_value:
##            max_value = num
##    return numbers.index(max_value)
##
##print(get_index_of_largest([51, 65, 66, 80, -10, 55])) #3
##print(get_index_of_largest([])) #-1

##Ex 8
##def tuple_append(my_tuple, number):
##    my_tuple = list(my_tuple[:2])
##    my_tuple.append(number)
##    
##    return tuple(my_tuple)
##
##
##my_tuple = tuple_append((1,2,3), 4)
##print(my_tuple) #(1, 2, 4)
##
##my_tuple = tuple_append(([1,2,3], [4,5,6], '2', 'd'), 4)
##print(my_tuple)

##Ex 9
##def append_to(element, values=None):
##    if values == None:
##        values = []
##    values.append(element)
##    return values
##
##
####Test
##my_list = []
##print(append_to(100, my_list))
##print(append_to(-100, my_list))

##Ex 10
##def print_values(dictionary):
##    for key in sorted(dictionary): 
##        print(dictionary[key], end=" ")
##
##print_values({'b':36, 'a':12, 'c':24})
##print_values({97:'a', 65:'A', 43:'+', 48:'0'})


##Ex 11
##def word_len_frequencies(sentence):
##    my_dict = {}
##    my_dict2 = {}
##    
##    sentence = sentence.lower()
##    word_list = sentence.split()
##    
##    for word in word_list:
##        if word not in my_dict:
##            my_dict[word] = 1
##        else:
##            my_dict[word] += 1
##            
##    for key in my_dict:
##        value = my_dict[key]
##        if value not in my_dict2:
##            my_dict2[value] = [key]
##        else:
##            my_dict2[value].append(key)
##    key_list = []
##    
##    for key in my_dict2:
##        my_dict2[key].sort()
##        key_list.append(key)
##        
##    for key in sorted(key_list,reverse=True):
##        line = str(key) + ' ' + str(my_dict2[key])
##        print(line)
##
##word_len_frequencies('the Quick BROWN fox jumps fox fox fox quick')
####4 ['fox']
####2 ['quick']
####1 ['brown', 'jumps', 'the']


#####Lab 4
##Ex 1
##def is_valid_radius(radius):
##    try:
##        if (isinstance(radius, int) or isinstance(radius, float)) and radius > 0:
##            return True
##        elif radius <= 0:
##            return "ERROR: Invalid radius!"
##
##    except ValueError:
##        return "ERROR: Invalid radius!"
##    except TypeError:
##        return "ERROR: Invalid radius!"
##        
##
####Test
##print(is_valid_radius(16))
##print(is_valid_radius(-1)) #ERROR: Invalid radius!
##print(is_valid_radius('12')) #ERROR: Invalid radius!
##print(is_valid_radius([16, 12])) #ERROR: Invalid radius!
##print(is_valid_radius(2.5)) #True
##print(is_valid_radius(0)) #ERROR: Invalid radius!


##Ex 2

##def is_valid_score(score):
##    try:
##        if not isinstance(score, int) and not isinstance(score, float):
##            raise ValueError()
##        elif score < 0 or score > 100:
##            raise ValueError()
##        else:
##            return True
##
##        
##    except ValueError:
##        return "ERROR: Invalid score!"
##
##
##                       
##print(is_valid_score(85.5)) #True
##print(is_valid_score(-1)) #ERROR: Invalid score!
##print(is_valid_score([16, 12])) #ERROR: Invalid score!
##print(is_valid_score(123)) #ERROR: Invalid score!
##print(is_valid_score(0)) #True
##print(is_valid_score(100)) #True
##print(is_valid_score('sixteen')) #ERROR: Invalid score!

##Ex 3
##def count_consonants(word):
##    try:
##        consonants = "bcdfghjklmnpqstuvwxyzBCDFGHJKLMNPQSTUVWXYZ"
##        count = 0
##        for letter in word:
##            if letter in consonants:
##                count += 1
##                
##        return count
##
##    except TypeError:
##        return "ERROR: Invalid input!"
##
##print(count_consonants('abcdef')) #4
##print(count_consonants('123')) #0
##print(count_consonants(123)) #ERROR: Invalid input!
##print(count_consonants(''))  #0
##print(count_consonants([123])) #ERROR: Invalid input!

##Ex 4

##def set_list_element(a_list, index, value):
##    try:
##        a_list[index] = value
##        return a_list
##    
##    except IndexError:
##        print("ERROR: Invalid index: {}.".format(index))
##        return a_list
##    except TypeError:
##        print("ERROR: Invalid input.")
##        return a_list
##        
##
####Test
##list1 = [1, 2, 3]
##set_list_element(list1, 1, 10);
##print(list1) #[1, 10, 3]
##list1 = [1, 2, 3]
##set_list_element (list1, 4, 10);
##print(list1) #ERROR: Invalid index: 4.
###[1, 2, 3]
##list1 = [1, 2, 3]
##set_list_element(list1, 'two', 10);
##print(list1) #ERROR: Invalid input.
###[1, 2, 3]


##Ex 5
##def get_max(numbers):
##    try:
##        return float(max(numbers))
##
##    except TypeError:
##        return "ERROR: Invalid number!"
##    
##
####Test
##print(get_max([3, -2, 1, 4])) #4.0
##print(get_max([3, -2, 'two', 4, 'one'])) #ERROR: Invalid number!
##print(get_max([12, 2.5, 45, 99])) #99.0


##Ex 6
##def get_sum_even(numbers):
##    try:
##        a_list = []
##        for number in numbers:
##            if type(number) == int and number % 2 ==0:
##                a_list.append(number)
##
##        if sum(a_list) % 2 ==0:
##            return sum(a_list)
##    
##    except TypeError:
##        return sum(a_list)
##
##
####Test
##my_list = [1, 2, 3.5, 4, -1, 2]
##print(get_sum_even(my_list)) #8
##my_list = [1, 2, 3, 4, "two", 2]
##print(get_sum_even(my_list)) #8
##print(get_sum_even([])) #0
##print(get_sum_even(['NA'])) #0

##Ex 7

##def get_valid_input():
##    number = -1 #default
##    while not 1 <= number <= 10: ##while not (number >= 1) or not (number <= 10):
##        try:
##            user_input = input("Enter a number between 1 and 10 inclusive: ")
##            number = float(user_input)
##            if not number < 1 or number > 10:
##                return number
##            
##        except ValueError:
##            continue
##
##print("Valid input: {}".format(get_valid_input()))



##Ex 8
##def get_volume(radius, height):
##    import math
##    
##    try:
##        if (not isinstance(radius, int) or not isinstance(radius, int)) and (not isinstance(radius, float) or not isinstance(radius, float)):
##            raise TypeError()
##        elif radius < 0 and height > 0:
##            return "ERROR: Radius must be positive."
##        elif height < 0 and radius > 0:
##            return "ERROR: Height must be positive."
##        elif radius < 0 and height < 0:
##            return "ERROR: Height and radius must be positive."
##        elif radius == 0 or height == 0:
##            return "ERROR: Not a cylinder."
##        else:
####            pi = 3.141592653589793
##            result = math.pi * (radius**2) * height
##            return int(round(result))
##
##    except TypeError:
##        return "ERROR: Invalid input."

##Ex 9
##def get_maori_word(dictionary, word):
##    try:
##        return dictionary[word]
##
##    except KeyError:
##        return "ERROR: {} is not available.".format(word)
##
####Test
##dictionary ={'example': 'tauira', 'house': 'whare', 'apple': 'aporo', 'love': 'aroha', 'food': 'kai',
##'hello': 'kiaora', 'work': 'mana', 'weather': 'huarere', 'greenstone': 'pounamu',
##'red': 'whero', 'orange': 'karaka', 'black': 'mangu'}
##print(get_maori_word(dictionary, 'house')) #whare
##print(get_maori_word(dictionary, 'orange')) #karaka
##print(get_maori_word(dictionary, 'tooth')) #ERROR: tooth is not available.


##Ex 10
##def get_phone(phones_dictionary, name):
##    try:
##        if isinstance(name, int):
##            return "ERROR: Invalid input!"
##        elif name == "":
##            return "ERROR: Invalid name!"
##        else:
##            return phones_dictionary[name]
##        
##    except KeyError:
##        return "ERROR: {} is not available.".format(name)



##Test
##phones_dictionary = {'Martin':8202, 'Angela':6620, 'Ann':4947, 'Damir':2391, 'Adriana':7113, 'Andrew':5654}
##print(get_phone(phones_dictionary , 'Ann')) #4947
##print(get_phone(phones_dictionary , 'Daniel')) #ERROR: Daniel is not available.
##print(get_phone(phones_dictionary , 123)) #ERROR: Invalid input!
##print(get_phone(phones_dictionary , '')) #ERROR: Invalid name!


##Ex 11
def read_scores(filename):
    try:
        if isinstance(filename, str) and len(filename) > 0:
            input_file = open(filename, "r")
            scores = input_file.read().split()
            numbers = [float(score) for score in scores if float(score) >= 0 ]
            input_file.close()
            number_of_marks = len(numbers)
            total_marks = sum(numbers)
            
            if total_marks <= 0:
                return print("ERROR: No positive scores in the input file.")
            else:
                print("There are {} score(s).".format(number_of_marks))
                print("The total is {:.2f}.".format(total_marks))
                print("The average is {:.2f}.".format(total_marks/number_of_marks))
                
        elif isinstance(filename, str) and len(filename) == 0:
            return print("ERROR: Invalid filename!")
        
        elif isinstance(filename, int):
            return print("ERROR: Invalid input!")
    
    except FileNotFoundError:
        return print("ERROR: The file '{}' does not exist.".format(filename))



##Test
##read_scores('eight_marks.txt')
####There are 7 score(s).
####The total is 280.00.
####The average is 40.00.
##read_scores('input_unknown.txt') #ERROR: The file 'input_unknown.txt' does not exist.
##read_scores('empty.txt') #ERROR: No positive scores in the input file.
##read_scores('all_negatives.txt') #ERROR: No positive scores in the input file.
##read_scores('') #ERROR: Invalid filename!
##read_scores(123) #ERROR: Invalid input!


####Lab 7
##Ex 5
##def get_middle_number_from_file(filename):
##    try:
##        input_file = open(filename, "r")
##        contents = input_file.read().split()
##        input_file.close()
##        numbers = []
##        alpabet = "abcdefghijklmnopqrstuvwxyz"
##
##        for number in contents:
##            if "." in number:
##                number = round(float(number))
##                numbers.append(number)
##                print('ERROR: "'"{}"'" contains an invalid value.'.format(filename))
##            elif number in alpabet:
##                print('ERROR: "{}" contains an invalid value.'.format(filename))
##            else:
##                numbers.append(int(number))
##                
##        numbers.sort()
##        middle_num = len(numbers) // 2
##        
##        return numbers[middle_num]
##
##
##    except FileNotFoundError:
##        return 'ERROR: "'"{}"'" does not exist.'.format(filename)
##    except IndexError:
##        return 'ERROR: "{}" is empty.'.format(filename)
##    
##
##    
##print(get_middle_number_from_file('test0.txt')) #ERROR: "test0.txt" does not exist.
##print(get_middle_number_from_file('test1.txt')) #ERROR: "test1.txt" is empty.
##print(get_middle_number_from_file('test2.txt')) #12
##print(get_middle_number_from_file('test8.txt')) #ERROR: "test8.txt" contains an invalid value.
###################################################ERROR: "test8.txt" contains an invalid value.
###################################################6
##print(get_middle_number_from_file('test9.txt')) #ERROR: "test9.txt" contains an invalid value.
#################################################12

##Ex 6
##def linear_search(student_id, students):
##    for index in range(len(students)):
##        if students[index][0] == student_id:
##            return students[index][1]

##Test
##s1 = (7, "Smith")
##s2 = (5, "Brown")
##s3 = (4, "Chan")
##s4 = (2, "Kim")
##s5 = (0, "Lin")
##students = [s1, s2, s3, s4, s5]
##print(linear_search(0, students)) #Lin

##s1 = (1, "Anderson")
##s2 = (2, "Huang")
##s3 = (3, "Ng")
##s4 = (4, "Roberts")
##s5 = (5, "Smith")
##s7 = (7, "Zhou")
##students = [s1, s2, s3, s4, s5, s7]
##print(linear_search(-456, students)) #None


##Ex 7
##Ex 6
##def linear_search(student_id, students):
##    for index in range(len(students)):
##        if students[index][0] == student_id:
##            return students[index][1]

##Test
##s1 = (7, "Smith")
##s2 = (5, "Brown")
##s3 = (4, "Chan")
##s4 = (2, "Kim")
##s5 = (0, "Lin")
##students = [s1, s2, s3, s4, s5]
##print(linear_search(0, students)) #Lin

##s1 = (1, "Anderson")
##s2 = (2, "Huang")
##s3 = (3, "Ng")
##s4 = (4, "Roberts")
##s5 = (5, "Smith")
##s7 = (7, "Zhou")
##students = [s1, s2, s3, s4, s5, s7]
##print(linear_search(-456, students)) #None



##Test
##print(get_unique_letters('hello', 'world')) #dehrw
##print(get_unique_letters('world', 'hello')) #dehrw
##print(get_unique_letters('x', 'aaxxxaa')) #a
##print(get_unique_letters('xa', 'aaxxxaa')) #ax
##print(get_unique_letters('constructionism', 'circles')) #elmnotu


##Ex 8
##def rotate_3(numbers):
##    a_list = []
##    rotate_list = []
##
##    for index in range(len(numbers)):
##        number = numbers[index]
##        if index <= 2:
##            rotate_list.append(number)
##        else:
##            a_list.append(number)
##
##    return a_list + rotate_list
##        
##
######Test
##numbers = [7,72,91,39,30,78,62,52,43,28]
##print(rotate_3(numbers)) #[39, 30, 78, 62, 52, 43, 28, 7, 72, 91]
##
##numbers = [1]
##result = rotate_3(numbers)
##print(result) #[1]
##
##numbers = [58,11,35,83,97,65,96,39,74,18,4]
##print(rotate_3(numbers)) #[83, 97, 65, 96, 39, 74, 18, 4, 58, 11, 35]

##Ex 9
##def get_list_of_odd_maximums(a_list_of_lists):
##    odd_list = []
##
##    for i in a_list_of_lists:
##        a_list = []
##        for j in i:
##            if j % 2 != 0:
##                odd_num = j
##                a_list.append(odd_num)
##
##        if len(a_list) > 0:
##            odd_list.append(max(a_list))
##        else:
##            odd_list.append(None)
##
##    return odd_list


####Test
##a_list_of_lists = [ [3, 42, 678, -5, -5],
##                [-4, -2, -33, -29, 0],
##                [51],
##                [4, 6, -4],
##                [-309, -3, -34] ]
##
##result = get_list_of_odd_maximums(a_list_of_lists)
##print("Odd maximums:", result) #Odd maximums: [3, -29, 51, None, -3]

##a_list_of_lists = [ [4, -4],
##                [-5, -4, -7, 0],
##                [-82],
##                [-5, 5, 3, -2] ]
##result = get_list_of_odd_maximums(a_list_of_lists)
##print("Odd maximums:", result) #Odd maximums: [None, -5, None, 5]


##Ex 11

##def swaps(numbers):
##    count = 0
##    for fill_slot in range(len(numbers) - 1, 0, -1):
##        pos_of_max = 0
##        for location in range(1, fill_slot + 1):
##            if numbers[location] > numbers[pos_of_max]:
##                pos_of_max = location
##        numbers[fill_slot], numbers[pos_of_max] = numbers[pos_of_max], numbers[fill_slot]
##        
##        if numbers[fill_slot] != numbers[pos_of_max] and numbers[pos_of_max] != numbers[fill_slot]:
##            count += 1
##  
##    return count


####Test
##numbers = [0, 4, 2, 7, 5]
##print(swaps(numbers)) #2
##
##numbers = [5, 2, 1, 8, 0, 3, 7]
##print(swaps(numbers)) #4
## 
##numbers = [0, 1, 2, 3, 4, 5]
##print(swaps(numbers)) #0
##
##numbers = [5]
##print(swaps(numbers)) #0


##Ex 12

##def check_count(student_id, students):
##    students.sort()
##    print(students)
##    max_index = len(students) - 1
##    min_index = 0
##    location = 0
##    
##    while (min_index <= max_index):
##        location += 1
##        mid_point = (min_index + max_index) // 2
##        print(mid_point)
##        element = students[mid_point]
##        if student_id == element[0]:
##            return location
##        elif student_id < element[0]:
##            max_index = mid_point - 1
##        else:
##            min_index = mid_point + 1
##
##
##    return -1
##
##
####Test
##s1 = (7, "Smith")
##s2 = (5, "Brown")
##s3 = (4, "Chan")
##s4 = (2, "Kim")
##s5 = (0, "Lin")
##students = [s1, s2, s3, s4, s5]
##print(check_count(0, students)) #2
##
##s1 = (7, "Smith")
##s2 = (5, "Brown")
##s3 = (4, "Chan")
##s4 = (2, "Kim")
##s5 = (0, "Lin")
##students = [s1, s2, s3, s4, s5]
##print(check_count(7, students)) #3
##
##s1 = (7, "Smith")
##s2 = (5, "Brown")
##s3 = (4, "Chan")
##s4 = (2, "Kim")
##s5 = (0, "Lin")
##students = [s1, s2, s3, s4, s5]
##print(check_count(8, students)) #-1
##
##s1 = (70, "Anderson")
##s2 = (60, "Huang")
##s3 = (50, "Ng")
##s4 = (40, "Roberts")
##s5 = (30, "Smith")
##s6 = (20, "Smith")
##s7 = (10, "Zhou")
##students = [s1, s2, s3, s4, s5, s6, s7]
##print(check_count(50, students)) #3
##
##students = []
##print(check_count(1, students)) # -1




def insertion_sort(a_list):	
    for index in range(1, len(a_list)):
        item_to_insert = a_list[index]
        i = index - 1
        while i >= 0 and len(a_list[i]) >= len(item_to_insert):
            a_list[i + 1] = a_list[i]
            i -= 1
        a_list[i + 1] = item_to_insert



d = ['aaa', 'cccc', 'ee', 'bb', 'bbbb', 'd'] #['cccc', 'bbbb', 'aaa', 'ee', 'bb', 'd']
insertion_sort(d)
print(d)


d = ['sculpted', 'eyebolts', 'timarau', 'readout', 'embow']
#['eyebolts', 'sculpted', 'timarau', 'readout', 'embow']
insertion_sort(d)
print(d)


