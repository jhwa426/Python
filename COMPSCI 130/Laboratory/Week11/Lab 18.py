######Lab 18
######15.10.2020
######

##Ex 2
##def running_sum_over_7(numbers):
##    if sum(numbers) < 7:
##        return -1
##    
##    result = 0
##    for number in numbers:
##        if result <= 7:
##            result += number
##    return result

def running_sum_over_7(numbers):
    result = 0
    if sum(numbers) < 7:
        return -1
    else:
        first_num = numbers[0]
        if first_num < 7:
            result = first_num + running_sum_over_7(numbers[1:])
        return result
        
##print(running_sum_over_7([1, 3, 5, 7, 9, 11]))
##
##print(running_sum_over_7([2, 4, 6, 8, 10, 12]))
##
##print(running_sum_over_7([2, 1]))

##Ex 3
class Parallelogram:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height
        return self.__height

    def set_width(self, width):
        self.__width = width
        return self.__width

    def get_area(self):
        return self.__width * self.__height

    def __str__(self):
        return "Parallelogram: {}cm (width) x {}cm (height)".format(self.__width,self.__height)

##Ex 4
class Cipher:
    def __init__(self, offset, reverse):
        self.__offset = offset
        self._reverse = reverse
        

    def encode(self, words):
        a_string = ""

        for word in words:
            element = ord(word)
            element += self.__offset

            if element > ord("z"): ##122
                shift = element - ord("z") 
                element = ord("a") + shift - 1
                
            elif element < ord("a"): ##97
                shift = ord("a") - element -1 
                element = ord("z") - shift
    
            a_string += chr(element)

        if self._reverse == True:
            return a_string[::-1]
            
        return a_string
 
##Ex 5        
    def decode(self, words):
        a_string = ""
        for word in words:
            element = ord(word)
            element -= self.__offset

            if element > ord("z"): ##122
                shift = element - ord("z") 
                element = ord("a") + shift - 1
                
            elif element < ord("a"): ##97
                shift = ord("a") - element -1 
                element = ord("z") - shift
    
            a_string += chr(element)
            
        if self._reverse == True:
            return a_string[::-1]
        
        return a_string


##Ex 6
class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)

    def __str__(self):
        return 'Stack: {} <- top of the stack'.format(str(self.__items))

    def slice(self, start, stop, step = 1):
        new_list = self.__items[start:stop:step]
        new_stack = Stack()
        
        for element in new_list:
            new_stack.push(element)
            
        return new_stack


##Ex 7
class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []
 
    def enqueue(self, item):
        self.__items.insert(0,item)

    def dequeue(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def peek(self):
        return self.__items[self.size() - 1]

    def __str__(self):
        return 'Queue: front->{}<- end'.format(str(self.__items[::-1]))


    def splice(self, second_queue):
        ##self.__items ##['3', '2', '1']
        
        self.__items = second_queue.__items + self.__items
        


##Ex 8
def create_chain(elements):
    if len(elements) == 0:
        return None
    elif len(elements) == 1:
        return Node(elements[0])
    else:
        return Node(elements[0], create_chain(elements[1:]))

##Ex 9
class LinkedList:
    def __init__(self):
        self.__head = Node(None)
        
    def add(self, item): #add to the beginning of the list
        new_node = Node(item, self.__head)
        self.__head = new_node
        
    def size(self):
        current = self.__head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count
    
    def is_empty(self):
        return self.__head == None
    
    def __str__(self):
        result = "["
        separator = ""
        current = self.__head
        
        while current != None:
            result += separator + str(current.get_data())
            separator = ", "
            current = current.get_next()
        result += "]"
        
        return result

    def has_same_elements(self, list2):
        current_node = self.__head
        current_list = []

        compare_node = list2.__head
        compare_list = []


        for i in range(list2.size()):
            if current_node != None: 
                current_list.append(current_node.get_data())
                current_node = current_node.get_next()        

        for j in range(list2.size()):
            if compare_node != None:  
                compare_list.append(compare_node.get_data())
                compare_node = compare_node.get_next()
                
        count = 0
        for index in current_list:
            if index in compare_list:
                count += 1


        if count == list2.size():
            return True
        return False

    
        
##Ex 10
def get_rightmost_data(b_tree):
    a_list = []

    if b_tree == None:
        return 0
    
    else:
        a_list.append(b_tree.get_data())
##        a_list.append(get_rightmost_data(b_tree.get_left()))
        a_list.append(get_rightmost_data(b_tree.get_right()))

    return max(a_list)
    
    

##Ex 11
def print_leaf_nodes(b_tree):
    if b_tree == None:
        return

    if b_tree.get_right() == None and b_tree.get_left() == None:
        print(b_tree.get_data(), end = " ")

    if b_tree.get_left() != None:
        print_leaf_nodes(b_tree.get_left())
        
    if b_tree.get_right() != None:
        print_leaf_nodes(b_tree.get_right())




##Ex 13
def evaluate_f(num):
    if num == 0:
        return 2
##even
    if num % 2 == 0:
        result = evaluate_f(num-2) + 3
        return result
##odd
    if num % 2 != 0:
        result = evaluate_g(num) + evaluate_f(num - 1)
        return result

        
def evaluate_g(num):
    if num == 1:
        return 3
##even  
    if num % 2 == 0:
        result = (evaluate_f(num) * evaluate_g(num - 1))
        return result
##odd
    if num % 2 != 0:
        result = evaluate_g(num - 2) - 2
        return result



##Ex 14
class Folder:
    def __init__(self, folder_name, list_of_subfolders, list_of_filenames):
        self.__name = folder_name
        self.__subfolders = list_of_subfolders
        self.__files = list_of_filenames
        
    def __str__(self):
        return self.__name
    
    def get_files(self):
        return self.__files
    
    def get_subfolders(self):
        return self.__subfolders



def folder_search(folder, file):
    file_name = folder.get_files() #list_of_filenames
    sub = folder.get_subfolders() #list_of_subfolders

    ##base case
    if file in file_name:
        return folder

    else:
        for name in sub:
            search = folder_search(name, file)
            if search != None:
                return search







####Test case
##b = Folder('Folder_b', [], ['File_0', 'File_1', 'File_2'])
##c = Folder('Folder_c', [], ['File_3', 'File_4'])
##a = Folder('Folder_a', [b, c], [])
##print(folder_search(a, 'File_3')) #Folder_c
##
##
##
##b = Folder('Folder_b', [], ['File_0', 'File_1', 'File_2'])
##c = Folder('Folder_c', [], ['File_3', 'File_4'])
##a = Folder('Folder_a', [b, c], ['File_5', 'File_6'])
##print(folder_search(a, 'File_0')) #Folder_b






