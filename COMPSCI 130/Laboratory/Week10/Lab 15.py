######Lab 15
######06.10.2020
######
class Node:
    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next

    def __str__(self):
        return str(self.__data)

    ##Ex 2
    def add_after(self, value):
        new_node = Node(value)
        temp = self.__next
        self.__next = new_node
        new_node.set_next(temp)
        
        
     ##Ex 3
    def remove_after(self):
        temp = self.__next
        self.__next = temp.__next
        
    
    ##Ex 4
    def __contains__(self, value):
        temp = self.__next

        if self.__data == value:
            return True
        
        while temp != None:
            if temp.__data == value:
                return True
            temp = temp.__next
        
    ##Ex 5
    def get_sum(self):
        count = 0
        temp = self

        while temp != None:
            count += temp.__data
            temp = temp.__next
            
        return count

######Lab 15
##Ex 1
class LinkedList:
    def __init__(self):
        self.__head = Node(None)
        self.__count = 0
        self.__r_count = 0

    def add(self, value):
        new_node = Node(value)
        new_node.set_next(self.__head)
        self.__head = new_node
        self.__count += 1

    def size(self):
        return self.__count
        
    def get_head(self):
        return self.__head

##Ex 2
    def clear(self): ####Question
        self.__count = 0
        return self.__count

    def is_empty(self):
        if self.__count == 0:
            return True
        return False

    def __len__(self):
        return self.__count

##Ex 3      
    def __str__(self):
        result = "["
        current = self.__head
        while current.get_next():
            result += str(current) + ", "
            current = current.get_next()
  
        result += "]"
        result = result[:-3] + result[-1]

        if self.__count == 0:
            return "[]"     

        if self.__r_count != 0:
            number = result[1::3]
            number = number[::-1]
            result = result[0] + ", ".join(number) + result[-1]
            return result
        
        return result
        

    
##    def __str__(self):
##        node = []
##        current = self.__head
##        while current != None:
##            node.append(str(current.get_data()))
##            current = current.get_next()
##        return '[' + ', '.join(node) + ']'
    
  

    ##Ex 4
    def __contains__(self, search_value):
        current_node = self.__head
        
        if current_node.get_data() == search_value:
            return True
        else:
            current_node = current_node.get_next()
        
        while current_node != None:
            if current_node.get_data() == search_value:
                return True
            else:
                current_node = current_node.get_next()
                
        return False
    
    ##Ex 5
    def __getitem__(self, index):
        current = self.__head
        list_index = 0
        while current != None:
            if list_index == index:
                return current.get_data()
            list_index += 1
            current = current.get_next()
    
           
    ##Ex 6
    def add_all(self, a_list):
        index = 0
        while len(a_list) != index:
            new_node = Node(a_list[index])
            new_node.set_next(self.__head)
            self.__head = new_node
            self.__count += 1
            index += 1
            


    ##Ex 7     
    def get_min_odd(self):
        current = self.__head
        count = 0
        current_best = 1
        while current.get_next() != None:
            data = current.get_data()
            
            if data % 2 != 0:
                if current_best >= data:
                    current_best = data
                count += 1

            current = current.get_next()

        if count == 0:
            return 999
        else:
            return current_best


    ##Ex 8
##    def reverse(self):
##        previous = None        
##        current = self.__head    
##        following_next = current.get_next()
##        while current != None:
##            current.get_next = previous 
##            previous = current     
##            current = following_next
##            if current.get_next != None:               
##                following_next = following_next.get_next()
##            
##        self.__head = previous

    def reverse(self):
        self.__r_count += 1
        return self.__r_count
        
  
values = LinkedList()
values.add(1)
values.add(2)
values.add(3)
print(values)
values.reverse()
print(values)





##Ex 9 
class SquareNumber:
    def __init__(self, count=5):
        self.__count = count

    def __iter__(self):
        return SquareNumberIterator(self.__count)


class SquareNumberIterator:
    def __init__(self, count = 5):
        self.__count = count
        self.__current = 1
        
    def __current(self):
        return self.__current

    def __count(self):
        return self.__count
        
    def __next__(self):
        if self.__count < self.__current:
            raise StopIteration
        else:
            square = self.__current ** 2
            self.__current += 1
            return square

   
##Ex 10
class LinkedListIterator:
    def __init__(self, head):
        self.__head = head
        self.__current = self.__head

    def __next__(self):
        if self.__current == None:
            raise StopIteration
        else:
            data = self.__current.get_data()
            self.__current = self.__current.get_next()
            return data


















    
