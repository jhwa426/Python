##Lab 4
##11.08.2020

##Ex 1

def is_valid_radius(radius):
    try:
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError()
        elif radius <= 0:
            raise ValueError()
        return True
    except TypeError:
        return "ERROR: Invalid radius!"
    except ValueError:
        return "ERROR: Invalid radius!"
##
##
####Test
##print(is_valid_radius(16)) #True
##print(is_valid_radius(-1)) #ERROR: Invalid radius!
##print(is_valid_radius('12')) #ERROR: Invalid radius!
##print(is_valid_radius([16, 12])) #ERROR: Invalid radius!
##print(is_valid_radius(2.5)) #True
##print(is_valid_radius(0)) #ERROR: Invalid radius!


##Ex 2

def is_valid_score(score):
    try:
        if not isinstance(score, int) and not isinstance(score, float):
            raise TypeError()
        elif score > 100 or score < 0:
            raise ValueError()
        return True
    except TypeError:
        return "ERROR: Invalid score!"
    except ValueError:
        return "ERROR: Invalid score!"
##
####Test
##print(is_valid_score(85.5)) #True
##print(is_valid_score(-1)) #ERROR: Invalid score!
##print(is_valid_score([16, 12])) #ERROR: Invalid score!
##print(is_valid_score(123)) #ERROR: Invalid score!
##print(is_valid_score(0)) #True
##print(is_valid_score(100)) #True
##print(is_valid_score('sixteen')) #ERROR: Invalid score!

##Ex 3

def count_consonants(word):
    try:
        consonants = "bcdfghjklmnpqstuvwxyzBCDFGHJKLMNPQSTUVWXYZ"
        count = 0
        for letter in word:
            if letter in consonants:
                count = count + 1
        return count
        
    except TypeError:
        return "ERROR: Invalid input!"
##
##
####Test
##print(count_consonants('abcdef')) #4
##print(count_consonants('123')) #0
##print(count_consonants(123))  #ERROR: Invalid input!
##print(count_consonants(''))  #0
##print(count_consonants([123])) #ERROR: Invalid input!


##Ex 4
def set_list_element(a_list, index, value):
    try:
        a_list[index] = value

    except IndexError:
        print("ERROR: Invalid index: {}.".format(index))
    except TypeError:
        print("ERROR: Invalid input.")
##
##
######Test
##list1 = [1, 2, 3]
##set_list_element(list1, 1, 10);
##print(list1) #[1, 10, 3]
##
##list1 = [1, 2, 3]
##set_list_element (list1, 4, 10);
##print(list1) #ERROR: Invalid index: 4.
###[1, 2, 3]
##
##list1 = [1, 2, 3]
##set_list_element(list1, 'two', 10);
##print(list1) #ERROR: Invalid input.
###[1, 2, 3]


##Ex 5

def get_max(numbers):
    try:
        biggest_number = max(numbers)
        return float(biggest_number)
 
    except TypeError:
        return "ERROR: Invalid number!"
    except ValueError:
        return "ERROR: Invalid number!"
##        
##
####Test
##print(get_max([3, -2, 1, 4])) #4.0
##print(get_max([3, -2, 'two', 4, 'one'])) #ERROR: Invalid number!
##print(get_max([12, 2.5, 45, 99])) #99.0
##print(get_max(['NA']))

##Ex 6
def get_sum_even(numbers):
    try:
        a_list = []
        for number in numbers:
            if type(number) == int and number % 2 == 0:
                a_list.append(number)
                
        result = sum(a_list)
        return result

    except TypeError:
        return reuslt
    except ValueError:
        return result
##
##
####Test
##my_list = [1, 2, 3.5, 4, -1, 2]
##print(get_sum_even(my_list)) #8
##
##my_list = [1, 2, 3, 4, "two", 2]
##print(get_sum_even(my_list)) #8
##
##print(get_sum_even([])) #0
##print(get_sum_even(['NA'])) #0

##Ex 7

def get_valid_input():
    number = -1 
    while not 1 <= number <= 10:
        try:
            user_input = input("Enter a number between 1 and 10 inclusive: ")
            number = float(user_input)
            if not(number > 10 or number < 1):
                return number
        except ValueError:
            continue
        except TypeError: 
            continue

                


##def get_valid_input():
##    number = -1 #default
##    while not 1 <= number <= 10:
##        user_input = input("Enter a number between 1 and 10 inclusive: ")
##        number = float(user_input)
##    return number



##Test
##print("Valid input: {}".format(get_valid_input()))
##Enter a number between 1 and 10 inclusive: 20
##Enter a number between 1 and 10 inclusive: 10
##Valid input: 10.0

##Ex 8
##Method 1
def get_volume(radius, height):
    import math
    try:
        if (not type(radius) == int or not type(height) == int) and (not type(radius) == float or not type(height) == float):
            raise TypeError()
        elif radius < 0 and height > 0:
            return "ERROR: Radius must be positive."
        elif height < 0 and radius > 0:
            return "ERROR: Height must be positive."
        elif radius < 0 and height < 0:
            return "ERROR: Height and radius must be positive."
        elif radius == 0 or height == 0:
            return "ERROR: Not a cylinder."
        else:
            result = math.pi * (radius**2) * height
            return int(round(result))
            
        
    except TypeError:
        return "ERROR: Invalid input."


##Method 2 (used)
def get_volume(radius, height):
    import math
    
    try:
        if (not isinstance(radius, int) or not isinstance(radius, int)) and (not isinstance(radius, float) or not isinstance(radius, float)):
            raise TypeError()
        elif radius < 0 and height > 0:
            return "ERROR: Radius must be positive."
        elif height < 0 and radius > 0:
            return "ERROR: Height must be positive."
        elif radius < 0 and height < 0:
            return "ERROR: Height and radius must be positive."
        elif radius == 0 or height == 0:
            return "ERROR: Not a cylinder."
        else:
##            pi = 3.141592653589793
            result = math.pi * (radius**2) * height
            return int(round(result))

    except TypeError:
        return "ERROR: Invalid input."
##
####Test
##print(get_volume(10, 2)) #628
##print(get_volume(-10, 2)) #ERROR: Radius must be positive.
##print(get_volume(10, -2)) #ERROR: Height must be positive.
##print(get_volume(-10, -2)) #ERROR: Height and radius must be positive.
##print(get_volume(10, 0)) #ERROR: Not a cylinder.
##print(get_volume('ten', 2)) #ERROR: Invalid input.
##print(get_volume(10.5, 2.5)) #866

##Ex 9

def get_maori_word(dictionary, word):
    try:
        return dictionary[word]

    except KeyError:
        return "ERROR: " + word + " is not available."
    

####Test
##dictionary ={'example': 'tauira', 'house': 'whare', 'apple': 'aporo', 'love': 'aroha', 'food': 'kai',
##'hello': 'kiaora', 'work': 'mana', 'weather': 'huarere', 'greenstone': 'pounamu',
##'red': 'whero', 'orange': 'karaka', 'black': 'mangu'}
##print(get_maori_word(dictionary, 'house')) #whare
##print(get_maori_word(dictionary, 'orange')) #karaka
##print(get_maori_word(dictionary, 'tooth')) #ERROR: tooth is not available.

##Ex 10

def get_phone(phones_dictionary, name):
    try:
        if isinstance(name, int):
            raise TypeError()
        elif len(name) > 0:
            return phones_dictionary[name]
        else:
            return "ERROR: Invalid name!"

    except KeyError:
        return "ERROR: " + name + " is not available."
    except TypeError:
        return "ERROR: Invalid input!"

##
####Test
##phones_dictionary = {'Martin':8202, 'Angela':6620, 'Ann':4947, 'Damir':2391, 'Adriana':7113, 'Andrew':5654}
##
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
        return print("ERROR: The file " + "'" + filename + "'" + " does not exist.")
    except ValueError:
        return print("ERROR: The input file contains invalid values.")


    

##Test
##read_scores('eight_marks.txt')
###There are 7 score(s).
###The total is 280.00.
###The average is 40.00.
##read_scores('input_unknown.txt') #ERROR: The file 'input_unknown.txt' does not exist.

##read_scores('empty.txt') #ERROR: No positive scores in the input file.
##read_scores('all_negatives.txt') #ERROR: No positive scores in the input file.

##read_scores('') #ERROR: Invalid filename!
##read_scores(123) #ERROR: Invalid input!

##read_scores('with_invalid.txt') # ERROR: The input file contains invalid values.









