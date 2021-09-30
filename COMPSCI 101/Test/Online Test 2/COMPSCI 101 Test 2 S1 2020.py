##COMPSCI 101 Test 2 S1 2020
##Jeff Hwang (jhwa426)

##Ex 1
def print_first_last(a_list):
    first_letter = str(a_list[0])
    last_letter = str(a_list[-1])

    return print(first_letter + " to " + last_letter)


#Test
print_first_last([1, 6, 5]) #1 to 5
print_first_last(["one", "two", "three", "four", "and", "so", "on", "hundred"]) #one to hundred
print_first_last(["front", "middle", "back"]) #front to back


##Ex 2
def get_first_letters(word1, word2, word3):
    first_word1 = word1[0].upper()
    first_word2 = word2[0].upper()
    first_word3 = word3[0].upper()

    result = first_word1+first_word2+first_word3
    return result
    

##Test
print(get_first_letters("be", "back", "soon")) #BBS
print(get_first_letters("before", "anyone", "else")) #BAE
print(get_first_letters("random", "Access", "memory")) #RAM


##Ex 3

def get_unique_3_letter_words(text):
    contents = text.split()
    a_list = []
    for word in contents:
        if len(word) == 3 and word not in a_list:
            a_list.append(word.lower())

    a_list.sort()
    
    return a_list
            

#Test
sentence = "In the not too distant future technology may provide a solution to the problem"
words_list = get_unique_3_letter_words(sentence)
print(words_list) #['may', 'not', 'the', 'too']
words_list = get_unique_3_letter_words("I could agree with you but then we would both be wrong")
print(words_list) #['but', 'you']
words_list = get_unique_3_letter_words("I have nothing to declare except my genius")
print(words_list) #[]
words_list = get_unique_3_letter_words("Inn ABC DDA")
print(words_list) #[]


##Ex 4

def print_latitude_longitude(city_name, city_lat_lng_dictionary):

    for word in city_lat_lng_dictionary:
        if city_name == word:
            print("The latitude-longitude of",word.upper(), "is ",end ="")
            print(city_lat_lng_dictionary[word],end="")
            print(".")
                

#Test
cities = {'shanghai':(31.2165,121.4365), 'beijing':(39.928,116.3883), 'seoul':(37.5663,126.9997), 'adelaide':(-34.935,138.6), 'newcastle':(-32.8453,151.815), 'christchurch':(-43.535,172.63), 'hamilton':(-37.7783,175.2896), 'auckland':(-36.8481,174.763)}
city_name = 'beijing'
print_latitude_longitude(city_name , cities)

##Ex 5

def get_two_highest_marks(names_marks_list):
    num_list = []
    for mark in names_marks_list:
        score = mark[-1]
        num_list.append(score)

    num_list.sort()
    result = []
    result.append(num_list[-2])
    result.append(num_list[-1])

    return result
    

##Test
names_marks = [("Ian", 78), ("Siggy", 88), ("Andy", 68), ("Irene", 90), ("Gio", 59)]
top_two = get_two_highest_marks(names_marks)
print(top_two) #[88, 90]
names_marks = [("Isa", 88), ("Bro", 92), ("Bella", 88), ("Lee", 68), ("Teo", 60)]
top_two = get_two_highest_marks(names_marks)
print(top_two) #[88, 92]
names_marks = [("David", 88), ("Lee", 68), ("Teo", 60), ("Jo", 91)]
top_two = get_two_highest_marks(names_marks)
print(top_two) #[88, 91]

##Ex 6

def remove_all_repeats(numbers_list):
    numbers_list.sort()
    index = len(numbers_list)-1
    while index > -1: 
        if numbers_list[index] == numbers_list[index-1]:
            numbers_list.pop(index)
           
             
        index = index - 1

    return numbers_list

def remove_all_repeats(numbers_list):
    numbers_list.sort()
    for number in range(len(numbers_list)-1,-1,-1):
        if number == len(numbers_list)-1:
            numbers_list == numbers_list
        elif numbers_list[number] == numbers_list[number+1]:
            numbers_list.pop(number)

    return numbers_list
        


##Test
numbers = [3, 71, 71, 3, 99, 3, 67, 88]
remove_all_repeats(numbers)
print(numbers) #[3, 67, 71, 88, 99]

numbers = [71, 71, 71, 71, 71, 71, 71, 71, 71, 71]
remove_all_repeats(numbers)
print(numbers) #[71]

numbers = [9, 71, 71, 9, 71, 9]
remove_all_repeats(numbers)
print(numbers) #[9, 71]

##Ex 7

def get_common_elements(list1, list2):
    a_list = []
    for number1 in list1:
        for number2 in list2:
            if number1 == number2:
                a_list.append(number1)

    a_list.sort()
    return a_list

def get_common_elements(list1, list2):
    a_list = []
    for number1 in list2:
        for number2 in list1:
            if number1 == number2:
                a_list.append(number1)

    a_list.sort()
    return a_list



##Test
numbers1 = [3, 78, 785, 4, 99, 677, 23, 9]
numbers2 = [3, 2, 9, 4]
print(get_common_elements(numbers1, numbers2)) #[3, 4, 9]
print(get_common_elements([3, 23, 99, 4], [4, 99, 7, 5, 23, 3])) #[3, 4, 23, 99]
print(get_common_elements([], [3, 23, 77, 4])) #[]


##Ex 8

def get_list_of_countries(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split()
    input_file.close()

    return contents

def create_country_code_dictionary(lines_list):
    a_dict = {}
    for word in lines_list:
        position = word.find(":")
        key = word[:position]
        value = word[position+1:]
        a_dict[key] = value
        
    return a_dict


##Test
lines = get_list_of_countries('countries.txt')
countries_dictionary = create_country_code_dictionary(lines)
for key in sorted(countries_dictionary.keys()):
    print(key, countries_dictionary[key])


##Ex 9

def get_average_number_of_vowels(words_list):
    vowels = "aeiouAEIOU"
    count = 0
    if len(words_list) == 0:
        return 0
    else:
        for word in words_list:
            for average in word:
                if average in vowels:
                    count = count + 1

        return round(count/len(words_list),1)

##Test
words = ["Beautiful", "Queen", "scratched", "Queueing"]
print(get_average_number_of_vowels(words)) #3.8
print(get_average_number_of_vowels([])) #0
    
##Ex 10

def has_exactly_2_of_each(a_list):
    new_list = []
    
    if a_list == []:
        return True
    for index in a_list:
        if index not in new_list:
            new_list.append(index)
            if a_list.count(index) != 2:
                return False
    return True
                

##Test
numbers = [3, 78, 78, 3, 99, 67, 67, 99]
print(has_exactly_2_of_each(numbers)) #True
print(has_exactly_2_of_each([9, 9, 9])) #False
print(has_exactly_2_of_each([3, 9, 9, 9, 9, 3])) #False

numbers = [3, 78, 78, 3, 99, 67, 67, 99, 3] # [3, 3, 3, 67, 67, 78, 78, 99, 99]
print(has_exactly_2_of_each(numbers)) #False
print(has_exactly_2_of_each([])) #True
print(has_exactly_2_of_each([3, 3])) #True
print(has_exactly_2_of_each([3])) #False

##Ex 11

def process_marks(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split()
    input_file.close()

    return contents

def print_dict(marks_dict):
    a_dict = {}
    for word in marks_dict:
        
        position_key = word.find(",")
        position_key_back = word.rfind(",")
        position_value = word.find(":")
        position_value_back = word.rfind(":")

        key = word[:position_key]
        value = word[position_value+1:]
        print(key)
        print(value)
        
        

#Test
filename1 = "Input1.txt"
marks_dict = process_marks(filename1)
print_dict(marks_dict)


##Ex 12
def print_board(board):
    for row in board:
        print(row)
        


##Ex 13
def print_inverted_mirrored_right_angle_triangle(symbols, index, number_of_rows):
    
    if len(symbols) > index:
        ##String version
        symbol = symbols[index]
        for row in range(number_of_rows,-1,-1):
            for column in range(1, number_of_rows + 1):
                if(column <= number_of_rows - row):
                    print(" ", end = "")
                else:
                    print(symbol, end = "")
            print()
            
    else:
        ##number version
        symbol = index
        for row in range(number_of_rows-1,-1,-1):
            print(" " * (number_of_rows-row-1),end ="")
            for column in range(row+1):
                print(column+symbol, end="")
            print()


##Test
print_inverted_mirrored_right_angle_triangle(['%', '$', '#', '@', '&', '*'], 2, 4)
####
 ###
  ##
   #

print_inverted_mirrored_right_angle_triangle(['%', '$', '#'], 3, 5)
##34567
## 3456
##  345
##   34
##    3
print_inverted_mirrored_right_angle_triangle(['%', '$', '#', '@', '&', '*'], 5, 5)
print_inverted_mirrored_right_angle_triangle(['%', '$', '#', '@', '&', '*'], 0, 5)
print_inverted_mirrored_right_angle_triangle(['%', '$', '#', '@', '&', '*'], 1, 4)


##Ex 14

def prime_factorization(n):
    a_list = []
    divisible = 2

    while divisible*divisible <= n:
        while (n % divisible) == 0:
            a_list.append(divisible)
            n = n // divisible
        divisible = divisible+ 1
        
    if n > 1:
       a_list.append(n)
       
    return print(a_list)

def prime_factorization(n):
    a_list = []
    divisible = 2

    while divisible*divisible <= n:
        while (n % divisible) == 0:
            a_list.append(divisible)
            n = n // divisible
        divisible = divisible+ 1
        
    if n > 1:
       a_list.append(n)
       
    return a_list

def print_prime_list(a_list):
    for i in range(len(a_list)):
        if i != len(a_list) - 1:
            print(a_list[i],end = " * ")
        else:
            print(a_list[i])
            

##Test

n = 2
prime_list = prime_factorization(n)
print(n,"is the product of the following primes:",end=" ")
print_prime_list(prime_list) ##2 is the product of the following primes: 2

n = 21
prime_list = prime_factorization(n)
print(n,"is the product of the following primes:",end=" ")
print_prime_list(prime_list) ##21 is the product of the following primes: 3 * 7

n = 56
prime_list = prime_factorization(n)
print(n,"is the product of the following primes:",end=" ")
print_prime_list(prime_list) ##56 is the product of the following primes: 2 * 2 * 2 * 7











    




    
