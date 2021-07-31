######Lab 9
######01.09.2020
######


######Ex 1 - 2
class Book:
    def __init__(self, code, title):
        self.__code = code
        self.__title = title
        self.__status = True
        
    def get_book_code(self):
        return self.__code

    def get_book_title(self):
        return self.__title

    def is_available(self):
        return self.__status

##Ex 2
    def borrow_book(self):
        self.__status = False

    
    def return_book(self):
        self.__status = True


    def __str__(self):
        if self.__status == True:
            return "{}, {} (Available)".format(self.__title,self.__code)
        else:
            return "{}, {} (On Loan)".format(self.__title,self.__code)
        

######Ex 3 - 4
class Member:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.__on_loan_books_list = []

    def get_name(self):
        return self.__name

    def get_member_id(self):
        return self.__member_id

    def get_on_loan_books(self):
        return self.__on_loan_books_list
    
##Ex 4
    def borrow_book(self, book):
        self.__on_loan_books_list.append(book)
        
    def return_book(self, book):
        self.__on_loan_books_list.remove(book)
        
    def __str__(self):
        if len(self.__on_loan_books_list) != 0 :
            book_list = [book.get_book_title() for book in self.__on_loan_books_list]
            
##            book_list = []
##            for book in self.__on_loan_books_list:
##                book_list.append(book.get_book_title())
                
            titles = "\n".join(book_list)
            return "{}\nOn loan book(s):\n".format(self.__name) + titles

        else:
            return "{}\nOn loan book(s):\n".format(self.__name) + "-"


######Ex 5 - 6

class Record:
    def __init__(self, book, member, date):
        self.__book = book
        self.__member = member
        self.__issue_date = date
        self.__is_on_loan = True
        
        self.__book.borrow_book()
        self.__member.borrow_book(book)
        

    def get_member_id(self):
        return self.__member.get_member_id()

    def get_book_code(self):
        return self.__book.get_book_code()

    def get_issue_date(self):
        return self.__issue_date

    def is_on_loan(self):
        if self.__is_on_loan != False:
            return True
        else:
            return False

######Ex 6
    def return_book(self):
        self.__is_on_loan == False
        self.__book.return_book()
        self.__member.return_book(self.__book)
            

    def __str__(self):
        return "{}, {}, issued date={}".format(self.__member.get_name(),str(self.__book),self.__issue_date)




######Ex 7 - 10
class MyLibrary:
    def __init__(self,filename):
        self.__books_list = []
        self.__on_loan_records_list = []
        
        try:
            input_file = open(filename,"r")
            contents = input_file.read().split("\n")
            input_file.close()

            for word in contents:
                line = word.split(",")
                code = line[0]
                title = line[1]
                new_book = Book(code,title)
                self.__books_list.append(new_book)

            count = len(self.__books_list)
            print("{} books loaded.".format(count))
                
        except FileNotFoundError:
            print("ERROR: The file '{}' does not exist.".format(filename))
        

    def show_all_books(self):
        for book in self.__books_list:
            print(book)
        

##Ex 8
    def find_book(self, code):
        for book in self.__books_list:
            if code == book.get_book_code() and book.is_available():
                return book
            
        return None


    def borrow_book(self, book, member, issue_date):
        if book is not None:
            book.borrow_book()            
            member.borrow_book(book)
            
            print("{} is borrowed by {}.".format(book.get_book_title(), member.get_name()))
        else:
            print("ERROR: could not issue the book.")
        
            
    def show_available_books(self):
        for book in self.__books_list:
            if book.is_available():
                print(book)
            
        
##Ex 9
    def find_record(self, code):
        for record in self.__books_list:
            print(record)
            if code == record.get_book_code() and not record.is_available():
                return record
          
        return None


    def return_book(self, record):
        if record is not None:
            record.return_book()
            print("{} is returned successfully.".format(record.get_book_code()))
            
        else:
            print("ERROR: could not return the book.")

            


        



####Test Ex 9
library = MyLibrary('simple_books.txt')
print()
b1 = library.find_book('QS12.02.003')
m1 = Member(1001, "Michael")
b2 = library.find_book('QK12.04.002')
library.borrow_book(b1, m1, "2020-08-12")
print()
library.borrow_book(b2, m1, "2020-08-15")
print()
r1 = library.find_record('QK12.04.002')
library.return_book(r1)
print()
library.show_available_books()
print()
print(m1)
print()
print(b2)
##


