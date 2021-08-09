######Lab 14
######01.10.2020
######

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


##        a_list = []
##        for index in range(self.__data):
##            if self.__data != None:
##                a_list.append(self.__data)
##
##                
##        return a_list



##Ex 6
def create_sample_node_chain():
    first_node = Node("three")

    second_node = Node("linked")
    first_node.set_next(second_node) ##between first and second one
    
    third_node = Node("nodes")
    second_node.set_next(third_node)##between second and third one

    return first_node


####Ex 7
def print_node_chain(node_of_chain):
    if node_of_chain == None:
        return
    print(node_of_chain.get_data())
    print_node_chain(node_of_chain.get_next())


####Ex 8
def create_node_chain(values):
    if len(values) == 1:
        return Node(values[0])
    else:
        return Node(values[0], create_node_chain(values[1:]))


##def create_node_chain(values):
##    new_node = Node(values)
##
##    for index in range(len(values)-1, -1, -1):
##        node5 = Node("elderberry")
##        node4 = Node("date", node5)
##        node3 = Node("cherry", node4)
##        node2 = Node("banana", node3)
##        node1 = Node("apple", node2)
##
##        return node1
        
    
###Ex 9
def convert_to_list(first_node):  
    node_list = []

    while first_node != None:
        node_list.append(first_node.get_data())
        first_node = first_node.get_next()

    return node_list


##Ex 10
def get_consecutive_sum(first_node):
    node_list = []

    while first_node != None:
        total = first_node.get_sum()
        node_list.append(total)
        first_node = first_node.get_next()

    return node_list












    
