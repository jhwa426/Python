##30.07.2020
##Lab01_B

##Ex 1
##input_number = int(input("Enter an integer: "))
##filename = input("Enter a filename: ")
##
##input_file = open(filename, "r")
##contents = input_file.read()
##word_list = contents.split()
##input_file.close()
##
##count = 0
##for number in word_list:
##    if int(number) % input_number == 0:
##        count = count + 1
##
###print
##if count <= 1:
##    result = "There is " + str(count) + " multiple of " + str(input_number) + " in the " + "'" + filename + "'" + " file."
##    print(result)
##else:
##    result = "There are " + str(count) + " multiples of " + str(input_number) + " in the " + "'" + filename + "'" + " file."
##    print(result)


##Test
#5
#basic_numbers.txt

#7
#numbers.txt


##Ex 2
##filename = input("Enter filename: ")
##input_file = open(filename, "r")
##contents = input_file.read()
##word_list = contents.split()
##input_file.close()
##length = 0
##for word in word_list:
##    if len(word) > length:
##        length = len(word)
##        letter = word
##        
##result = "The longest word is " + '"'+letter+'"'
##print(result)
    

##Test
##test1.txt


##Ex 3
##def get_first4(items):
##    a_list = []
##    for number in items:
##        if len(a_list) <= 3:
##            a_list.append(number)
##
##    return a_list
##        
##    
####Test
##print(get_first4([15,14,31,20,8,23,34,42,22,26])) #[15, 14, 31, 20]


##Ex 4
def get_sum_positive_even(numbers):
    positivie_even_number = [number for number in numbers if number > 0 and number % 2 ==0]
    return sum(positivie_even_number)

##Test
##print (get_sum_positive_even([1,2,3,4,5,-1,-9])) #6
##print (get_sum_positive_even([1,3,5,7])) #0
##print (get_sum_positive_even([]))#0

##def remove_negatives(numbers):
##    a_list = numbers[:]
##    for number in numbers:
##        if number < 0:
##            a_list.remove(number)
##
##    return a_list

##Ex 5
##def get_multiples_of_5(numbers):
##    a_list = []
##    for number in numbers:
##        if number % 5 == 0:
##            a_list.append(number)
##
##    return a_list
##
##
####Test
##print(get_multiples_of_5([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 25])) #[5, 25]
##print(get_multiples_of_5([])) #[]
##print(get_multiples_of_5([4, 5, 2, 22, 71, 30])) #[5, 30]

##Ex 6
##def count_consonants(word):
##    count = 0
##    words = "aeiouAEIOU"
##    for letter in word:
##        if letter not in words:
##            count = count + 1
##    return count
##    
##
####Test
##print(count_consonants('Hello')) #3
##print(count_consonants('Abracadabra')) #6

##Ex 7
##def unique_species(animal_species):
##    a_list = []
##    value = animal_species.values()
##    for letter in value:
##        if letter not in a_list:
##            a_list.append(letter)
##    a_list.sort()
##    
##    return a_list
##
##
####Test
##animal_species={1007:"Meerkat",2091:"Cheetah",13:"Cheetah"}
##result=unique_species(animal_species)
##print(result)


##Ex 8
##def print_keys_values_inorder(dictionary):
##    a_dic = {}
##    keys = dictionary.keys()
##    values = dictionary.values()
##
##    for word in sorted(keys):
##        letter = dictionary[word]
##        letter.sort()
##        a_dic[word] = letter
##
##    for i in a_dic:
##        print(i, " ".join(a_dic[i]))
##
##    
####Test
##my_dict = {6:['monday', 'coffee', 'strong'], 5:['short'], 3:['may', 'and']}
##print_keys_values_inorder(my_dict)

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
##    if ":" in word:
##        position = word.find(":") #name_dic[key]
##        translated_word = word[position+1:] #value
##        name_dic[word[:position]] = translated_word
##        
####print
##if word_name in name_dic.keys():
##    result = "'" + word_name + "'" + " is translated into " + "'" + name_dic[word_name] + "'" + "."
##    print(result)
##    
##elif word_name not in name_dic.keys():
##    result = "Sorry that word doesn't exist in Maori!"
##    print(result)
##
####Test
##
####english_to_maori.txt
####house


##Ex 10
a_dic = {}


input_word = input("Enter a sentence: ")
word_list = set(input_word.split())


for index in word_list:
    key_number = len(index)
    value_word = index

    if key_number not in a_dic:
        a_dic[key_number] = [value_word.lower()]
        a_dic[key_number].sort()
    else:
        a_dic[key_number].append(value_word.lower())
        a_dic[key_number].sort()
        
space = " "
##print
for key in sorted(a_dic.keys()):
    print(key, space.join(a_dic[key]))


   


##Test
##May your coffee be strong and your Monday be short
##Summer is over and the hot days are gone



            
