######Lab 11
######22.09.2020
######

class Contact:
    ##Ex 1
    def __init__(self, name, phone_number, email):
        self.__name = name
        self.__phone_number = phone_number
        self.__email = email
        self.__status = True

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def get_email(self):
        return self.__email

    def is_active(self):
        return self.__status


    ##Ex 2
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_email(self, email):
        self.__email = email
        
    def set_active(self, value):
        self.__status = value
            
    def __str__(self):
        if self.__status == False:
            return "{} is an inactive record.".format(self.__name)
        else:
            return "{} ({}), {}".format(self.__name, self.__phone_number, self.__email)


##Ex 3
class PhoneBook:
    def __init__(self):
        self.__phone_book = []

    def load_records(self, filename):
        try:
            input_file = open(filename,"r")
            contents = input_file.read().split()
            input_file.close()

            for word in contents:
                info = word.split(",")
                name = info[0]
                number = info[1]
                email = info[2]
                new_book = Contact(name, number, email) ###Key point
                self.__phone_book.append(new_book)
                
            count = len(self.__phone_book)
            print("{} records loaded.".format(count))        

        except FileNotFoundError:
            print("ERROR: The file '{}' does not exist.".format(filename))


    def show_all_records(self):
        for word in self.__phone_book:
            print(word)

    def __len__(self):
        return len(self.__phone_book)


    ##Ex 4
    def find_record(self, search_name):
        for name in self.__phone_book:
            if search_name == name.get_name():
                return name

        return None

    def update_phone(self, search_name, phone_number):
        for element in self.__phone_book:
            if search_name == element.get_name():
                element.set_phone_number(phone_number)
                return print("{}'s contact is updated.".format(search_name))

        return print("ERROR: {} is not found.".format(search_name))
    
    def set_active(self, search_name):
        for name in self.__phone_book:
            contact = name.get_name()
            if search_name == contact:
                name.set_active(True)
                return print("{} is active from now on.".format(search_name))

        return print("ERROR: {} is not found.".format(search_name))
    
##    def set_active(self, search_name):
##        record = self.find_record(search_name)
##        if record != None:
##            record.set_active(True)
##            print("{} is active from now on.".format(search_name))
##
##        else:
##            print("ERROR: {} is not found.".format(search_name))

    def set_inactive(self, search_name):
        for name in self.__phone_book:
            contact = name.get_name()
            if search_name == contact:
                name.set_active(False)
                return print("{} is inactive from now on.".format(search_name))
         
        return print("ERROR: {} is not found.".format(search_name))
    
    def show_active_records(self):
        for word in self.__phone_book:
            if word.is_active() == True:
                print(word)






##Ex 5
def get_sum_ascii(word):
    if word == "":
        return 0
    else:
        return ord(word[0]) + get_sum_ascii(word[1:])

##Test
##print(get_sum_ascii('This is a Test'))


##Ex 6
def get_sum_digits(number):
    if number < 10:
        return number
    else:
        numbers = number // 10
        last_number = number % 10
        return get_sum_digits(numbers) + last_number


##Test
##print(234, ":", get_sum_digits(234)) #234 : 9
##print(106, ":", get_sum_digits(106)) #106 : 7

##Ex 7
def get_min_odd(numbers):
    if len(numbers) == 1 and numbers[0] % 2 == 0:
        return 9999

    else:
        if numbers[0] % 2 != 0:
            return numbers[0]
    return get_min_odd(numbers[1:])




####Test
##lst = [6, 4, 5, 9]
##print(get_min_odd(lst))
##
##print(get_min_odd([2]))


##Ex 8
def get_odds_list(numbers):
    if not numbers:
        return []
    elif numbers[0] % 2 != 0:
        return [numbers[0]] + get_odds_list(numbers[1:])
    
    return get_odds_list(numbers[1:])
    
    
##Test
##print(get_odds_list([2, 3, 5, 6]))
##print(get_odds_list([2, 4, 6, 8]))

##Ex 9
##def get_merge_list(list_of_lists):
##    if len(list_of_lists) > 0:
##        first_number = list_of_lists[0]
##        rest_num = get_merge_list(list_of_lists[1:])
##        if len(first_number) > 0:
##            return first_number + rest_num
##        else:
##            return rest_num
##    else:
##        return []

def get_merge_list(list_of_lists):
    if len(list_of_lists) == 0:
        return []
    else:
        first_number = list_of_lists[0]
        rest_number = get_merge_list(list_of_lists[1:])

        return first_number + rest_number
    

########Test
##print(get_merge_list([[1, 2, 3], [2, 3, 5, 6], [7, 8, 9]]))
####[1, 2, 3, 2, 3, 5, 6, 7, 8, 9]
##print(get_merge_list([[1, 2, 3], [], [7, 8, 9]]))


##Ex 10
def palindrome_filter(sentence):
    if len(sentence) > 0:
        first_word = sentence[0]
        rest_word = palindrome_filter(sentence[1:])
        if first_word.isalpha() == True:
            return first_word.lower() + rest_word
        else:
            return rest_word
    else:
        return ""

##print(palindrome_filter("Able was I ere I saw Elba."))


def is_palindrome(sentence):
    if len(sentence) > 1:
        first_word = sentence[0]
        last_word = sentence[-1]
        
        if first_word == last_word:
            return is_palindrome(sentence[1:-1])
        else:
            return False
    else:
        return True

print(is_palindrome(palindrome_filter("Able was I ere I saw Elba.")))

##Test
##print(is_palindrome(palindrome_filter("Able was I ere I saw Elba.")))
##print(is_palindrome(palindrome_filter("Ebla was I ere I saw Elba.")))


##Ex 11
def get_gcd(m, n):
    if m > n:
        if m % n == 0:
            return n
        else:
            return get_gcd(n, m % n)
    elif m <= n:
        if n % m == 0:
            return m
        else:
            get_gcd(m, n % m)

####Test
##print(get_gcd(100, 70)) #10
##print(get_gcd(2, 6)) #2












