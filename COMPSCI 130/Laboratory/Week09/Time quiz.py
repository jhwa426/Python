##Week 8 Timed quiz

##Ex 1
class Deque:
    def __init__(self):
        self.__items = []

    def __items(self):
        return self.__items

    def __str__(self):
        return "Deque: {}".format(self.__items[::-1])

    def __len__(self):
        return len(self.__items)

    def clear(self):
        while len(self.__items) > 0 :
            self.__items.pop()

    def is_empty(self):
        if len(self.__items) == 0:
            return True
        return False


##Ex 2
    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0,item)

##Ex 3
    def remove_front(self):
        if self.is_empty():
            raise IndexError("ERROR: The deque is empty!")
        return self.__items.pop()
    
    def remove_rear(self):
        if self.is_empty():
            raise IndexError("ERROR: The deque is empty!")
        return self.__items.pop(0)
    
##Ex 4
    def peek_front(self):
        if self.is_empty():
            raise IndexError("ERROR: The deque is empty!")
        return self.__items[len(self.__items)-1]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("ERROR: The deque is empty!")
        return self.__items[0]

try:
  a_deque = Deque()
  a_deque.add_front(1)
  a_deque.add_front(2)
  print(a_deque.remove_front())
  print(a_deque.remove_front())
  print(a_deque.peek_front())
except IndexError as error:
  print(error)




