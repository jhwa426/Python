
    
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
class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right
        
    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinarySearchTree(new_data)
        else:
            t = BinarySearchTree(new_data, left=self.__left)
            self.__left = t
            
    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinarySearchTree(new_data)
        else:
            t = BinarySearchTree(new_data, right=self.__right)
            self.__right = t
            
    def get_left(self):
        return self.__left
    
    def get_right(self):
        return self.__right
    
    def set_left(self, left):
        self.__left = left
        
    def set_right(self, right):
        self.__right = right
        
    def set_data(self, data):
        self.__data = data
        
    def get_data(self):
        return self.__data

    ##Ex 4
    def __contains__(self, value):
        if self.__data == value:
            return True
        ##left
        elif value < self.__data and self.__left != None:
            return self.__left.__contains__(value)

        ##right
        elif value > self.__data and self.__right != None:
            return self.__right.__contains__(value)

        else:
            return False

    ##Ex 5
    def search(self, value):
        if self.get_data() == value:
            return self
        
        ##left
        elif value < self.__data and self.__left != None:
            return self.__left.search(value)

        ##right
        elif value > self.__data and self.__right != None:
            return self.__right.search(value)
        
        else:
            return None

    
    ##Ex 6
    def insert(self, value):
        if value == self.__data:
            return
        elif value < self.__data:
            if self.__left == None:
                self.__left = BinarySearchTree(value)
            else:
                self.__left.insert(value)
        else:
            if self.__right == None:
                self.__right = BinarySearchTree(value)
            else:
                self.__right.insert(value)
            

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right
        
    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinaryTree(new_data)
        else:
            tree = BinaryTree(new_data, left=self.__left)
            self.__left = tree
            
    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinaryTree(new_data)
        else:
            tree = BinaryTree(new_data, right=self.__right)
            self.__right = tree
            
    def get_left(self):
        return self.__left
    
    def get_right(self):
        return self.__right
    
    def set_data(self, data):
        self.__data = data
        
    def get_data(self):
        return self.__data
    
    def set_left(self, left):
        self.__left = left
        
    def set_right(self, right):
        self.__right = right



##Ex 1
class SimpleHashTable:
    def __init__(self, size = 7):
        self.__size = size
        self.__slots = [None] * self.__size
        self.__count = 0

    def __str__(self):
        return str(self.__slots)

    def get_hash_code(self, key):
        return key % (self.__size)

    def get_size(self):
        return self.__size



##Ex 2
    def put(self, key):
        if self.__size == self.__count:
            raise IndexError("ERROR: The hash table is full.")
        

        position = self.get_hash_code(key) ##position = key % (self.__size)
        
        if self.__slots[position] != None:
            slot = self.get_new_hash_code_linear_probing(position)
            self.__slots[slot] = key
            self.__count += 1
        else:
            self.__slots[position] = key
            self.__count += 1
            

##Ex 3
##getting slot
    def get_new_hash_code_linear_probing(self, index):
        slot = self.get_hash_code(index)
        while self.__slots[slot] != None:
            slot = (slot + 1) % self.__size

        return slot        



##Ex 4
    def clear(self):
        while len(self.__slots) > 0:
            self.__slots.pop()
            
    def is_empty(self):
        if len(self.__slots) == 0:
            return True
        return False


##Ex 5
    def rehashing(self, new_size):
        
        a_list = []
        for element in self.__slots:
            if element != None:
                a_list.append(element)
                
        self.__size = new_size
        self.__slots = [None] * self.__size
        for index in a_list:
            self.put(index)

##EX 1
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







    





