######Lab 10
######03.09.2020
######


######Ex 1
def count_down(n):
    if n == 0:
        print("Go!")
    else:
        print(n)
        count_down(n-1)


####Test
##count_down(3)


##Ex 2
def copy_string(word): 
    if len(word) == 0:
        return ""
    else:
        first = word[0]
        rest = copy_string(word[1:])
        return first + rest

####Test
##s = 'hello'		
##print(copy_string(s)) #hello

##Ex 3
def reverse_string(word):
    if len(word) == 0:
        return ""
    else:
        first = reverse_string(word[1:])
        rest = word[0]
        return first + rest 
        
##s = 'hello'		
##print(reverse_string(s))
##        
####Ex 4
def print_between(start, end):
    if start == end+1:
        return start
    else:
        print(start, end = " ")
        print_between(start+1, end)
        


####Test
##print_between(1, 5) #1 2 3 4 5
##print()
##print_between(-3, 3)

##Ex 5

def count_consonants(word):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

##    if len(word) == 1:
##        return 1 if word[0] in consonants else 0
##    else:
##        first = 1 if word[0] in consonants else 0
##        rest = count_consonants(word[1:])
##        return first + rest
        
    if len(word) == 1:
        if word[0] in consonants:
            return 1
        else:
            return 0
    else:
        if word[0] in consonants:
            first = 1
        else:
            first = 0
        rest = count_consonants(word[1:])

        return first + rest

    
##print(count_consonants('This is a Test'))
##print(count_consonants('AEIOU'))


##Ex 6
##def get_first_lower_case(word):
##    lower_case = "abcdefghijklmnopqrstuvwxyz"
##    
##    if word.isupper() == True:
##        return None
##    elif word[0] in lower_case:
##        return word[0]
##    else:
##        return get_first_lower_case(word[1:])
##
##
####Test
##s = 'WELL done'
##print(get_first_lower_case(s)) #d
##
##s = 'GREAT'		
##print(get_first_lower_case(s)) #None
    


##Ex 7
##def get_max_list(numbers):
##    if len(numbers) == 1:
##        return numbers[0]
##
##    else:
##        first_num = numbers[0]
##        rest_num = get_max_list(numbers[1:])
##
##        if rest_num > first_num:
##            return rest_num
##        else:
##            return first_num
    
def get_max_list(numbers):
    if len(numbers) == 1:
        return numbers[0]

    else:
        first_num = numbers[0]
        rest_num = get_max_list(numbers[1:])

        if first_num > rest_num:
            return first_num
        else:
            return rest_num


######Test
##lst = [1, 4, 5, -9]
##print(get_max_list(lst)) #5
##
##
##lst = [1]
##print(get_max_list(lst)) #1


##Ex 8
def get_max_len_list(words):
    if len(words) == 1:
        return len(words[0])

    else:
        first_word = len(words[0])
        rest_word = get_max_len_list(words[1:])

        if first_word > rest_word:
            return first_word
        else:
            return rest_word
    

######Test
##lst = ['This', 'is', 'a', 'test']
##print(get_max_len_list(lst)) #4
##
##lst = ['hello']
##print(get_max_len_list(lst)) #5


##Ex 9
def no_evens(numbers):
    first_num = numbers[0]
    
    if len(numbers) == 1 or first_num % 2 == 0:
        return False
    else:
        rest_num = no_evens(numbers[1:])
        
        if rest_num % 2 != 0:
            return False
        else:
            return True

        


    
##print(no_evens([2, 3, 5, 6])) #False
##print(no_evens([2])) #False
##print(no_evens([1, 3, 5, 7])) #True
##



##Ex 10
def evaluate_m(i):
    if i == 0:
        return 0
    else:
        result = 1 / i + evaluate_m(i-1)
        return result


####Test
##print('{} : {}'.format(1, evaluate_m(1))) 
##print('{} : {}'.format(2, evaluate_m(2))) #2 : 1.5
##print('{} : {:.4}'.format(5, evaluate_m(5))) #5 : 2.283
















