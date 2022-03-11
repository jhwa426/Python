##Ex 1
def highest_value_word(word1, word2, ordinal_position=1):
    index_position = ordinal_position - 1
    min_pos = min(len(word1), len(word2))

    if ordinal_position > min_pos:
        if len(word1) == len(word2):
            return 0
        elif len(word1) > len(word2):
            return -ordinal_position
        else:
            return ordinal_position
    if min_pos >= ordinal_position:
        if ord(word1[index_position]) == ord(word2[index_position]):
            return highest_value_word(word1, word2, ordinal_position + 1)
        elif ord(word1[index_position]) > ord(word2[index_position]):
            return -ordinal_position
        else:
            return ordinal_position



##Ex 2
class UndoRedo:
    def __init__(self):
        self.__back = Stack()
        self.__forward = Stack()
        self.__current = None
    
    def get_prev(self):
        if self.__back.is_empty():
            return None
        else:
            self.__forward.push(self.__current)
            self.__current = self.__back.pop()
            return self.__current
    
    def get_next(self):
        if self.__forward.is_empty():
            return None
        else:
            self.__back.push(self.__current)
            self.__current = self.__forward.pop()
            return self.__current

    
    def add_item(self, data):
        self.__back.push(self.__current)
        
        while not self.__forward.is_empty():
            self.__forward.pop()
            
        self.__current = data



##Ex 3          
def selection_order(items, interval):
    item_queue = Queue()
    a_list = []
    
    for element in items:
        item_queue.enqueue(element)

    while not item_queue.is_empty():
        for index in range(interval - 1):
            item_queue.enqueue(item_queue.dequeue())
            
        a_list.append(item_queue.dequeue())
    
    return a_list



##Ex 4
class QueueAsLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
        
    def size(self):
        return self.__count

    def enqueue(self, item):
        if self.__head == None:
            self.__head = Node(item)
            self.__tail = self.__head
            self.__count += 1 
        else:
            self.__tail.get_next = Node(item)
            self.__tail = self.__tail.get_next
            self.__count += 1              
            
    def dequeue(self):
        if self.__head == None:
            return None
        else:
            to_return = self.__head.get_data()
            self.__head = self.__head.get_next
            self.__count -= 1
            return to_return

    def peek(self):
        return self.__head

    def is_empty(self):
        if self.__count == 0:
            return True
        
        return False

##Ex 5
def hash_string_weighted_folding(string_to_hash, modulus):
    index = 0
    result = 0

    for number in string_to_hash:
        if index >= 4:
            ascii_code = ord(number)
            result += ascii_code
            index = 1
        else:
            ascii_code = ord(number)
            result += ascii_code * (256**index)
            index += 1

    result = result % modulus
    
    return result



##Ex 6
def max_value_length(tree):
    if tree == None:
        return 0

    else:
        data = len(str(tree.get_data()))
        left = max_value_length(tree.get_left())
        right = max_value_length(tree.get_right())

    return max(data, left, right)



##Ex 7
def reverse_sort_order(tree):
    result = []
    
    if tree == None:
        return None
    
    else: 
        result.append(tree.get_data())
        if reverse_sort_order(tree.get_left()) != None:
            result += (reverse_sort_order(tree.get_left()))
        
        if reverse_sort_order(tree.get_right()) != None:
            result += (reverse_sort_order(tree.get_right()))
            
    result.sort()
    return result[::-1]



   
##Ex 8
def get_bst_list_order(tree):
    space = Queue()
    space.enqueue(tree)
    result = []

    while space.is_empty() != True:
        data = space.dequeue()
        result.append(data.get_data())

        #left
        if data.get_left()!= None:
            space.enqueue(data.get_left())
            
        #right
        if data.get_right()!= None:
            space.enqueue(data.get_right())

            
    return result






