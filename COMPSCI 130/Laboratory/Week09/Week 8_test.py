###Week 8_Lecture

##numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##primes = [2, 3, 5, 7]
##my_list = [x+x for x in numbers if x not in primes]
####print(my_list)
##
##phrase = 'The quick brown fox jumps over the lazy dog'
##vowels = 'aeiouAEIOU'
##my_list = [c for c in phrase if c not in vowels]
##
##for c in my_list:
####    print(c, end = '')


class Node:
   def __init__(self, init_data):
       self.data = init_data
       self.next = None

   def get_data(self):
       return self.data

   def get_next(self):
       return self.next

   def set_data(self, new_data):
       self.data = new_data

   def set_next(self, new_next):
       self.next = new_next


first = Node(2)
second = Node(4)
third = Node(8)
first.set_next(second)
second.set_next(third)

class Numbers:
    def __init__(self, low, high):
        self.__low = low
        self.__high = high
    def __iter__(self):
        return NumbersIterator(self.__low, self.__high)

class NumbersIterator:
    def __init__(self, low, high):
        self.__current = low
        self.__high = high
    def __next__(self):
        if self.__current > self.__high:
            raise StopIteration
        else:
            self.__current += 1
            return self.__current - 1

example = [1, 2, 3, 4, 5]
it = iter(example)
print(next(it))
print(next(it))
print(next(it))


my_numbers = Numbers(5, 9)
for n in my_numbers:
    print(n)










        
