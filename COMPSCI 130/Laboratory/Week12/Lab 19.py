######Lab 19
######27.10.2020
######

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
        



####Ex 7
def create_bst_from_list(values):
    if len(values) == 0:
        return None
    
    else:
        a_root = BinarySearchTree(values[0])
        
        for element in values:
            a_root.insert(element)
    
    return a_root


   
##Ex 8
def get_bst_preorder(tree):
    result = []
    
    if tree == None:
        return None
    
    else:
        
        result.append(tree.get_data())
        if get_bst_preorder(tree.get_left()) != None:
            result.append(get_bst_preorder(tree.get_left()))
        
        if get_bst_preorder(tree.get_right()) != None:
            result.append(get_bst_preorder(tree.get_right()))
            
    
    return result


##Ex 9
def get_bst_preorder(tree):
    result = []
    
    if tree == None:
        return None
    
    else:
        
        result.append(tree.get_data())
        if get_bst_preorder(tree.get_left()) != None:
            result += (get_bst_preorder(tree.get_left()))
        
        if get_bst_preorder(tree.get_right()) != None:
            
            result += (get_bst_preorder(tree.get_right()))
            
    
    return result


##Ex 10
def get_maximum(tree):
    if tree.get_right() == None:
        return tree.get_data()
    else:
        right = get_maximum(tree.get_right())
        
        return right




