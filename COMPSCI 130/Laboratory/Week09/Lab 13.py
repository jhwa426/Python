######Lab 13
######29.09.2020
######
class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        while len(self.__items) > 0:
            self.__items.pop()


    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) == 0:
            raise IndexError("ERROR: The stack is empty!")
        return self.__items.pop()

    def peek(self):
        if len(self.__items) == 0:
            raise IndexError("ERROR: The stack is empty!")
        return self.__items[len(self.__items) - 1]

    ##Ex 2
    def __str__(self):
        return "Stack: {}".format(self.__items)

    def size(self): ##def __len__(self):
        return len(self.__items)
    
    def clear(self):
        self.__items = []
        return self.__items


    ##Ex 3
    def push_list(self, a_list):
        for word in a_list:
            self.__items.append(word)

    ##Ex 4
    def multi_pop(self, number):
        index = number
        if len(self.__items) >= index:
            for word in range(index):
                self.__items.pop()
            return True
        else:
            return False

    ##Ex 5
    def copy(self):
        new_stack = Stack()
        for element in self.__items:
            new_stack.push_list([element])

        return new_stack

    ##Ex 6
    def __eq__(self, other):
        if not isinstance(other, Stack):
            return False

        return self.__items == other.__items


##Ex 1
class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        while len(self.__items) > 0:
            self.__items.pop()

    def enqueue(self, item):
        self.__items.insert(0,item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.__items[len(self.__items)-1]


    ##Ex 2
    def __str__(self):
        return "Queue: {}".format(self.__items[::-1])

    def  __len__(self):
        return self.size()

    def clear(self):
        self.__items = []
        return self.__items

    ##Ex 3
    def enqueue_list(self, a_list):
        for word in a_list:
            self.enqueue(word)

    ##Ex 4
    def multi_dequeue(self, number):
        index = number
        if len(self.__items) >= number:
            for word in range(index):
                self.__items.pop()
            return True

        else:
            return False


##Ex 5
def mirror_queue(a_queue):
    new_queue = Queue()
    new_stack = Stack()

    while not a_queue.is_empty():
        temp = a_queue.dequeue()
        new_stack.push(temp)
        new_queue.enqueue(temp)

    while not new_queue.is_empty():
        a_queue.enqueue(new_queue.dequeue())

    while not new_stack.is_empty():
        a_queue.enqueue(new_stack.pop())



    
####Test
##q1 = Queue()
##q1.enqueue(1)
##q1.enqueue(2)
##q1.enqueue(3)
##print(q1) #Queue: [1, 2, 3]
##mirror_queue(q1)
##print(q1) #Queue: [1, 2, 3, 3, 2, 1]



##Ex 6
def is_palindrome(word):
    forward_queue = Queue()
    reverse_stack = Stack()

##insert and push each element 
    for letter in word:
        forward_queue.enqueue(letter)
        reverse_stack.push(letter)

##then checking each elemnet while dequeue and pop
    for check in range(len(word)):
        if forward_queue.dequeue() != reverse_stack.pop():
            return False
    
    return True
        
        
####Test
##print(is_palindrome("abcdef"))
##print(is_palindrome("nonon"))

##Ex 7
class CircularQueue:
    def __init__(self, value = 8):
        self.__value = value
        self.__items = [None] * value ###self.__items = [None for i in range(value)]
        self.__front = 0
        self.__count = 0
        self.__back = value - 1

    def __items(self):
        return self.__items

    def __front(self):
        return self.__front

    def __back(self):
        return self.__back
    
    def __count(self):
        return self.__items.count(not None)

    def is_empty(self):
        if self.__count == 0:
            return True
        return False
    
    def __str__(self):
        return "{}, front:{}, back:{}, count:{}".format(self.__items, self.__front, self.__back, self.__count)
  

    ##Ex 8
    def is_full(self):
        if self.__value == self.__count:
            return True
        else:
            return False
        
    def enqueue(self, item):
        if self.__value == self.__count:
            raise IndexError("ERROR: The queue is full.")
        else:
            self.__back = (self.__back + 1) % self.__value
            self.__items[self.__back] = item
            self.__count += 1


    ##Ex 9
    def dequeue(self):
        if self.__count == 0:
            raise IndexError("ERROR: The queue is empty.")
        else:
            self.__front = (self.__front + 1) % self.__value
            self.__items[self.__front]
            self.__count -= 1

            return self.__front


    ##Ex 10
    def print_all(self):
        for number in range(self.__count):
            print(self.__items[self.__front], end = " ")
            self.__front = (self.__front + 1) % self.__value


        if self.__value == self.__count:
            print()



##q1 = CircularQueue(4)
##q1.enqueue(1)
##q1.enqueue(2)
##q1.enqueue(3)
##q1.enqueue(4)
##q1.print_all()
##print(q1.dequeue())
##q1.print_all()




q1 = CircularQueue(5)
q1.enqueue(1)
q1.dequeue()
q1.enqueue(2)
print(q1)
q1.print_all()












    

