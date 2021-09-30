##Q3
def print_even_numbers(first_num, last_num):
    while first_num <= last_num:
        if first_num % 2 == 0:
            print(first_num, end = " ")
        first_num += 1


##test
##print_even_numbers(6, 20)
##print()
##print_even_numbers(7, 20)


##Q4
##def remove_spaces(phrase):
##    result = phrase.replace(" ", "")
##    return result

def remove_spaces(phrase):
    new_str = ""
    index = 0
    space = " "

    while index < len(phrase):
        if phrase[index] != space:
            new_str += phrase[index]

        index += 1

    return new_str
            
    



####Test
##print(remove_spaces("programming is such fun, fun, fun"))
##print(remove_spaces("1 5 67 88 "))

##Q5

def get_letter(word):
    print(word)
    
    while True:
        prompt = int(input("Enter index: "))
        if prompt >= 0 and prompt < len(word):
            return word[prompt]

        
        
####Test
##letter = get_letter("Dreams")
##print(letter)


##Q6

def test_number(number):
    if (number % 2 == 0 and number >= 30) and (number % 2 == 0 and number <= 50):
        return True
    else:
        return False

####Test
##print(test_number(28))
##print(test_number(30))


##Q7
def test_string(phrase):
    vowel = "aeiouAEIOU"

    if len(phrase) % 2 == 0 and (phrase[0] in vowel or phrase[-1] in vowel):
        return True
    else:
        return False
    
    
##Test
print(test_string("Anatonis"))
print(test_string("PD"))







