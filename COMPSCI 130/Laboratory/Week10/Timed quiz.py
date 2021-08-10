##Week 9 Timed quiz

##Ex 1
class OrderedLinkedList:
    def __init__(self):
        self.__head = Node(None)
        self.__count = 0

    def is_empty(self):
        if self.__count == 0:
            return True
        return False

    def add(self, value):
        previous = None
        current = self.__head
        stop = False
        while current != None and not stop:
            if str(current.get_data()) > str(value):
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(value)
        if previous == None:
            temp.set_next(self.__head)
            self.__head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)


    def __str__(self):
        return str(self.__head)



def add(self,item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
        if current.getData() > item:
            stop = True
        else:
            previous = current
            current = current.getNext()

    temp = Node(item)
    if previous == None:
        temp.setNext(self.head)
        self.head = temp
    else:
        temp.setNext(current)
        previous.setNext(temp)




        
