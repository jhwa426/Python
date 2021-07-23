##Lab3

##Ex 6

##def remove_letters(word1, word2):
##    for index in word2:
##        if index in word1:
##            position = word2.find(index)
            
##def remove_letters(word1, word2):
##    result = list(word2)
##    for letter in word1:
##        if letter in result:
##            result.remove(letter)
##    return ''.join(result)
##
####Test
##
##print(remove_letters('hello', 'world')) #wrd
##print(remove_letters('world', 'hello')) #hel


##Ex 7

##def get_index_of_largest(numbers):
##    if len(numbers) == 0:
##        return -1
##    max_value = numbers[0]
##    for num in numbers:
##        if num > max_value:
##            max_value = num
##    return numbers.index(max_value)
##
##
####Test
##print(get_index_of_largest([51, 65, 66, 80, -10, 55])) #3
##print(get_index_of_largest([])) #-1


##Ex 8
##def tuple_append(my_tuple, number):
##    a_list = list(my_tuple)
##    b_list = a_list[:2]
##    b_list.append(number)
##    
##    return tuple(b_list)
##
##
####Test
##my_tuple = tuple_append((1,2,3), 4)
##print(my_tuple) #(1, 2, 4)
##my_tuple = tuple_append(([1,2,3], [4,5,6], '2', 'd'), 4)
##print(my_tuple) #([1, 2, 3], [4, 5, 6], 4)



##Ex 9
##def append_to(element, values=None):
##    if values == None:
##        values = []
##    values.append(element)
##    
##    return values
##
##
####Test
##my_list = [1, 2, 3]
##print(append_to(100, my_list)) #[1, 2, 3, 100]
##print(append_to(-100, my_list)) #[1, 2, 3, 100, -100]
##
##my_list = append_to(12)
##print(my_list) #[12]
##my_other_list = append_to(24)
##print(my_other_list) #[24]
##
##my_list = append_to(12) #[12]
##print(my_list)
##my_other_list = append_to(24) 
##print(my_other_list) #[24]
##
##my_list = append_to(12)
##my_list = append_to(24)
##print(my_list) #[24]

##Ex 10

##def print_values(dictionary):
##    for key in sorted(dictionary.keys()): 
##        print(dictionary[key], end=" ")

##Ex 11
def word_len_frequencies(sentence):
    my_dict = {}
    my_dict2 = {}
    sentence = sentence.lower()
    word_list = sentence.split()
    
    for word in word_list:
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] = my_dict[word] + 1
            
    for key in my_dict:
        value = my_dict[key]
        if value not in my_dict2:
            my_dict2[value] = [key]
        else:
            my_dict2[value].append(key)
            
    key_list = []

    for key in my_dict2:
        my_dict2[key].sort()
        key_list.append(key)
    
    for key in sorted(key_list,reverse=True):
        line = str(key) + ' ' + str(my_dict2[key])
        print(line)



##Test
word_len_frequencies('the Quick BROWN fox jumps fox fox fox quick')
## 4 ['fox']
## 2 ['quick']
## 1 ['brown', 'jumps', 'the']

word_len_frequencies('this is a really long sentence of words and there will be some repeated words in this really long sentence of words')
## 3 ['words']
## 2 ['long', 'of', 'really', 'sentence', 'this']
## 1 ['a', 'and', 'be', 'in', 'is', 'repeated', 'some', 'there', 'will']
