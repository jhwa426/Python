##COMPSCI 101 Test 1 S1 2020


#Ex 1

##def print_greeting(name):
##    user_result = "Hello " + name + " how are you?"
##    
##    return print(user_result)
##
##
###Test
##print_greeting("Damir")
##print_greeting("Ann")


#Ex 2

##def do_multiplication(num1, num2):
##
##    result = int(num1) * int(num2)
##
##    return result
##
##
###Test
##print("2 * 3 =",do_multiplication(2,3))
##print("5 * 4 =",do_multiplication(5,4))


#Ex 3

##def to_the_power_of():
##    user_num1 = int(input("Number 1: "))
##    user_num2 = int(input("Number 2: "))
##
##    total = user_num1 ** user_num2
##    result = str(user_num1) + " to the power of " + str(user_num2) + " is " + str(total)
##    
##    return result
##
###Test
##print(to_the_power_of())

#Ex 4

##def get_ordered_words(word1, word2):
##    if len(word1) > len(word2):
##        return word1 + " " + word2
##    else:
##        return word2 + " " + word1
##
###Test
##print(get_ordered_words("out", "dinner")) #dinner out
##print(get_ordered_words("dinner", "out")) #dinner out
##print(get_ordered_words("bb", "a")) #bb a


#Ex 5

##def get_number(number1, number2):
##
##    first_num = str(number1)
##    last_num = str(number2)
##
##    result = first_num[0] + last_num[-1]
##
##    return int(result)
##
###Test
##print(get_number(76325, 321)) #71
##print(get_number(3, 2)) #32
##print(get_number(50004, 2)) #52


#Ex 6

#Test
def print_pattern(number):
    for each in range(number,0,-1):
        result = str(number) * each
        print(result)
        number = number - 1

#Result      
def print_pattern(number):
    for each in range(number, 0, -1):
        for reverse in range(number, 0, -1):
            if each < reverse:
                print(" ", end = "")
            else:
                print(each, end = "")

        print()     

#Test
print_pattern(6)


#Ex 7

##def get_list_of_four_letter_words(words_list):
##    new_list = []
##    for each in range(len(words_list)):
##        if len(words_list[each]) == 4:
##            new_list.append(words_list[each].lower())
##
##    return new_list

#Method 2
##def get_list_of_four_letter_words(words_list):
##    new_list = []
##    for each in words_list:
##        if len(each) == 4:
##            new_list.append(each.lower())
##
##    return new_list

###Test
##words = get_list_of_four_letter_words(['into', 'elephant', 'room', 'the'])
##print(words) #['into', 'room']
##
##print(get_list_of_four_letter_words(['hole', 'down', 'the', 'goes', 'rabbit']))
###['hole', 'down', 'goes']
##
##print(get_list_of_four_letter_words(['WATER', 'POND', 'OUT', 'FISH']))
###['pond', 'fish']


#Ex 8

##def get_count_containing_9(numbers_list):
##    count = 0
##    containing_number = str(9)
##    
##    for number in range(len(numbers_list)):
##        convert_str = str(numbers_list[number])
##        if containing_number in convert_str:
##            count = count + 1
##
##        
##    return count
##
##
##
###Test
##count_contain_9 = get_count_containing_9([393, 6369, 2042, 40, 9447])
##print(count_contain_9) #3
##print(get_count_containing_9([191, 45594, 1241, 9, 929])) #4
##print(get_count_containing_9([465, 383, 282])) #0


#Ex 9

##def contains_mostly_vowel_ending_words(words_list):
##    vowels = "aeiouAEIOU"
##    count_list = []
##    for word in words_list:
##        if len(word) >= 2 and word[-1] in vowels:
##            count_list.append(word)
##        elif len(word) == 2 and word[-1] not in vowels:
##            count_list.append(word)
##            
##    if len(count_list) == len(words_list):
##        return True
##    else:
##        return False
##
##
###Test
##print(contains_mostly_vowel_ending_words(['file', 'barrel', 'like', 'shoo', 'sh', 'pi'])) #False
##print(contains_mostly_vowel_ending_words(['file', 'barre', 'like', 'shoo', 'so', 'pi'])) #True
##print(contains_mostly_vowel_ending_words(['do', 'he', 'in', 'go', 'to', 'it'])) #True



#Ex 10

def get_unusual_average(numbers_list):
    avg_list = []

    for number in range(len(numbers_list)):
        if numbers_list[number] > 0: 
            if numbers_list[number] <= 100:
                avg_list.append(numbers_list[number])
            else:
                return round(sum(avg_list)/len(avg_list))
        
        elif numbers_list[0] > 0 and numbers_list[1] > 0:
            if numbers_list[number] <= 100:
                if numbers_list[number] > 0:
                    avg_list.append(numbers_list[number])
            else:
                return round(sum(avg_list)/len(avg_list))

        elif numbers_list[0] < 0 and numbers_list[1] < 0:
            if numbers_list[2] > 0 and numbers_list[2] <= 100:
                avg_list.append(numbers_list[number+2])
            elif numbers_list[2] > 100:
                return 0
            else:
                return round(sum(avg_list)/len(avg_list))

    return round(sum(avg_list)/len(avg_list))
        

##Test
result = get_unusual_average([5, 10, 15, 120, 2, 88, 22])
print(result) #10
print(get_unusual_average([20, 100, 60])) #60
print(get_unusual_average([-66, -100, 800, 20, 60])) #0
print(get_unusual_average([-4, -42, 6, 10, 120])) #8
print(get_unusual_average([42, 50, -600, -595, -179, -708, -867, -2])) #46
print(get_unusual_average([6, 2, 4, -6, -8, 90])) #26



#Ex 11

##def check_password(password):
##    symbol_list = [".",";","!","*","?"]
##    
##    if len(password) >= 8 and password.isalpha() == False and password.isdigit() == False:
##        for each in range(len(password)):
##            if password[each] in symbol_list:
##                return True
##
##        else:
##            return False
##    else:
##        return False
##
##
####Test
##password = "abc012"
##print("Is",password,"valid:",check_password(password)) #Is abc012 valid: False
##
##password = "abcd0123"
##print("Is",password,"valid:",check_password(password)) #Is abcd0123 valid: False
##
##password = "dAmIr007!"
##print("Is",password,"valid:",check_password(password)) #Is dAmIr007! valid: True



#Ex 12

##def fiddle_string(text):
##
##    #odd
##    if len(text) % 2 != 0:
##        middle_word = round(len(text) / 2)
##
##        text = text[middle_word+1:] + text[middle_word] + text[:middle_word]
##
##    #even
##    elif len(text) % 2 == 0:
##        middle_word = round(len(text) / 2)
##
##        text = text[middle_word:] + text[:middle_word]
##
##    return text
##        
##
###Test
##word = "Damir"
##print("Original word:",word,"\nNew word:",fiddle_string(word)) #Original word: Damir New word: irmDa
##
##word = "barbeque"
##print("Original word:",word,"\nNew word:",fiddle_string(word)) #Original word: barbeque  New word: equebarb


#Ex 13

##def update_guess(answer, guess, character):
##    new_str = ""
##    
##    if len(answer) == len(guess):
##        for word in range(len(answer)):
##            if answer[word] == character:
##                new_str = new_str + answer[word]
##            else:
##                new_str = new_str + guess[word]
##                
##        return new_str
##
###Test
##answer = "ladder"
##guess = "******"
##guess = update_guess(answer, guess, "d")
##print(guess) #**dd**
##
##guess = update_guess(answer, guess, "e")
##print(guess) #**dde*
##
##answer = "explosion"
##guess = "#########"
##
##guess = update_guess(answer,guess,"o")
##print(guess) ####o##o#
##
##guess = update_guess(answer,guess,"x")
##print(guess) #x##o##o#





#Ex 14

##def process_code(code_str):
##
##    mid_point = round(len(code_str)/2) #4 #3
##    index_front = code_str[:mid_point] #2455 #123
##    index_end = code_str[mid_point:] #90000 #456
##    
##    result = int(index_end) + int(index_front[1:-1])
##    
##    return result
##
##
####Test
##code = "245590000"
##print("Code:", code, "Result:", process_code(code)) #Code: 245590000 Result: 90045
##
##code = "123456"
##print("Code:", code, "Result:", process_code(code)) #Code: 123456 Result: 458
##
##code = "12345678910"
##print("Code:", code, "Result:", process_code(code))








    
    
