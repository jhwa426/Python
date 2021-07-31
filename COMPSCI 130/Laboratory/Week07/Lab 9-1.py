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
        return self.__status
    
    def return_book(self):
        self.__status = True
        return self.__status

    def __str__(self):
        if self.__status == True:
            return "{}, {} (Available)".format(self.__title,self.__code)
        else:
            return "{}, {} (On Loan)".format(self.__title,self.__code)
        
        
####Test Ex 1
##b1 = Book("QS12.03.001", "The Lord Of The Rings")
##print(b1.get_book_code(), b1.get_book_title(), b1.is_available()) #QS12.03.001 The Lord Of The Rings True
##                 
##b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
##print(b2.get_book_code(), b2.get_book_title(), b2.is_available()) #QK12.04.002 The Hitchhiker's Guide To The Galaxy True


####Test Ex 2
                 
##b1 = Book("QS12.03.001", "The Lord Of The Rings") #The Lord Of The Rings, QS12.03.001 (Available)
##print(b1)
##b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy") #The Hitchhiker's Guide To The Galaxy, QK12.04.002 (Available)
##print(b2)
##b2.borrow_book() #The Hitchhiker's Guide To The Galaxy, QK12.04.002 (On Loan)
##print()
##print(b2)


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


####Test Ex 3 
##m1 = Member(1001, "Michael") #Michael 1001
##print(m1.get_name(), m1.get_member_id())
##m2 = Member(1002, "Paul") #Paul 1002
##print(m2.get_name(), m2.get_member_id())

####Test Ex 4
##m1 = Member(1001, "Michael")
##m2 = Member(1002, "Paul")
##
##b1 = Book("QS12.03.001","The Lord Of The Rings")
##b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
##b3 = Book("QS12.02.003", "The Dune Chronicles")
##m1.borrow_book(b1)
##m1.borrow_book(b2)
##m1.borrow_book(b3)
##m1.return_book(b1)
##print(m1)
##
##
###Michael
####On loan book(s):
####The Hitchhiker's Guide To The Galaxy
####The Dune Chronicles
##
##print()
##print(m2)
####Paul
####On loan book(s):
####-


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


    
########Test 5
##m1 = Member(1001, "Michael")
##b1 = Book("QS12.03.001","The Lord Of The Rings")
##b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
##b3 = Book("QS12.02.003", "The Dune Chronicles")
##r1 = Record(b1, m1, "2020-08-12")
##print(r1.get_member_id(), r1.get_book_code(), r1.get_issue_date(), r1.is_on_loan())
##print()
##print(m1)
##print()
##print(b1)

########Test 6
####
##m1 = Member(1001, "Michael")
##b1 = Book("QS12.03.001","The Lord Of The Rings")
##b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
##b3 = Book("QS12.02.003", "The Dune Chronicles")
##r1 = Record(b1, m1, "2020-08-12")
##print(r1) ##Michael, The Lord Of The Rings, QS12.03.001 (On Loan), issued date=2020-08-12
##r2 = Record(b3, m1, "2020-08-15")
##print(r2) ##Michael, The Dune Chronicles, QS12.02.003 (On Loan), issued date=2020-08-15
##r1.return_book()
##print() ##
##print(r1) ##Michael, The Lord Of The Rings, QS12.03.001 (Available), issued date=2020-08-12
##print() ##
##print(b1) ##The Lord Of The Rings, QS12.03.001 (Available)
##print() ##
##print(m1)
####Michael
####On loan book(s):
####The Dune Chronicles, QS12.02.003 (On Loan)
##
##
####m1 = Member(1001, "Michael")
####b1 = Book("QS12.03.001","The Lord Of The Rings")
####b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
####b3 = Book("QS12.02.003", "The Dune Chronicles")
####r1 = Record(b1, m1, "2020-08-12")
####print(r1)
####r2 = Record(b3, m1, "2020-08-15")
####print(r2)
####r1.return_book()
####print()
####print(b1.is_available())


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
        self.__code = code
        if self.__code in self.__books_list:
            return self.__book.get_book_title()
        else:
            return None

    def borrow_book(self, book, member, issue_date):
        



####Test Ex 7
##library = MyLibrary('simple_books.txt')
##print()
##library.show_all_books()


####Test ex 8
##library = MyLibrary('simple_books.txt')
##print()
##b1 = library.find_book('003')
##m1 = Member(1001, "Michael")
##library.borrow_book(b1, m1, "2020-08-12")
##print()
##print(m1)


        
library = MyLibrary('simple_books.txt') 
print()
b1 = library.find_book('QS12.02.003') 
m1 = Member(1001, "Michael")
library.borrow_book(b1, m1, "2020-08-12")
print()
##b2 = library.find_book('QA12.04.004')
##library.borrow_book(b2, m1, "2020-08-12")
##print()
##library.show_available_books()
##print()
##print(m1)

##################5 books loaded.
##################
##################The Dune Chronicles is borrowed by Michael.
##################
##################A Song Of Ice And Fire Series is borrowed by Michael.
##################
##################The Lord Of The Rings, QS12.03.001 (Available)
##################The Hitchhiker's Guide To The Galaxy, QK12.04.002 (Available)
##################The Foundation Trilogy, QS12.01.005 (Available)
##################
##################Michael
##################On loan book(s):
##################The Dune Chronicles
##################A Song Of Ice And Fire Series




















