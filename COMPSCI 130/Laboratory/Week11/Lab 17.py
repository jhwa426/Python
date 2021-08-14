######Lab 17
######13.10.2020
######


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


##Ex 3
def create_a_bigger_tree():
    ##root
    a_root = BinaryTree("a")
    
    ##right
    a_root.insert_right("c")

    ##left
    a_root.insert_left("b")
    
    ##left_side of "b"
    left = a_root.get_left()
    left.insert_left("d")
    left.insert_right("e")

    ##righ_side of "b"
    left_b = left.get_left()
    left_b.insert_right("f")
    right = left.get_right()
    right.insert_right("g")


    return a_root
    

    
    
####Ex 4      
def add_all(a_list, index):
    if len(a_list) > index:
        a_root = BinaryTree(a_list[index])
        left_index = (2 * index + 1)
        right_index = (2 * index + 2)
        a_root.set_left(add_all(a_list, left_index))
        a_root.set_right(add_all(a_list, right_index))

    else:
        return None

    return a_root
        


####Test case
##def print_tree(t, level):
##    # Print the root node
##    print(' ' * (level*4) + str(t.get_data())) 
##    # Print the left subtree
##    if t.get_left() != None:
##        print('(l)', end = '')
##        print_tree(t.get_left(), level + 1) 
##    # Print the right subtree
##    if t.get_right() != None: 
##        print('(r)', end = '')
##        print_tree(t.get_right(), level + 1)
##
##
##tree = add_all([10, 5, 11, 22], 0)
##print_tree(tree, 0)
##print()
##tree = add_all([10, 5, 15, 11, 22], 0)
##print_tree(tree, 0)



##Ex 5
def get_height(b_tree):
    if b_tree == None:
        return -1
    return 1 + max(get_height(b_tree.get_left()), get_height(b_tree.get_right()))



##Ex 6
def search(tree, item):
    if tree.get_data() == None:
        return False
    elif tree.get_left() == item or tree.get_right() == item:
        return True
    else:
        return False



##Ex 7
def get_sum_string_len(my_tree):
    total = 0

    if my_tree == None:
        return total
    
    else:
        total = len(my_tree.get_data())
        total += get_sum_string_len(my_tree.get_left())
        total += get_sum_string_len(my_tree.get_right())

    return total


##Ex 8
def convert_tree_to_list(b_tree):
    a_list = []
    
    if b_tree == None:
        return None
        
    else:
        a_list.append(b_tree.get_data())
        a_list.append(convert_tree_to_list(b_tree.get_left()))
        a_list.append(convert_tree_to_list(b_tree.get_right()))
        
    return a_list
    
##tree = BinaryTree(12345)
##result = convert_tree_to_list(tree)
##print(result)



##Ex 9
def get_min_even(b_tree):
    a_list = []
    if b_tree == None:
        return 9999

    else:
        data = b_tree.get_data()
        left = get_min_even(b_tree.get_left())
        right = get_min_even(b_tree.get_right())

        if data % 2 == 0:
            a_list.append(data)

        a_list.append(left)
        a_list.append(right)

        return min(a_list)


##Ex 10
def combine_trees(btree1, btree2):
    if btree1 == None:
        return btree2
    if btree2 == None:
        return btree1

    ##data
    data = btree1.set_data(btree1.get_data() + btree2.get_data())
    
    ##left
    btree1.set_left(combine_trees(btree1.get_left(), btree2.get_left()))
    
    #right
    btree1.set_right(combine_trees(btree1.get_right(), btree2.get_right()))

    return btree1


##Assignmet 2
def create_tree_from_nested_list(node_list):
    if node_list:
        result = BinaryTree(node_list[0])
        left = create_tree_from_nested_list(node_list[1])
        right = create_tree_from_nested_list(node_list[2])
        if left != None:
            result.set_left(left)
        if right != None:
            result.set_right(right)
        return result 

def max_value_length(tree):
    if tree == None:
        return 0

    else:
        data = tree.get_data()
        left = max_value_length(tree.get_left())
        right = max_value_length(tree.get_right())

    if left > right:
        return left + 1
    
    else:
        return right + 1




binary_tree = create_tree_from_nested_list([7, [2, [14, None, None], [5, None, None]], [9, None, [144, None, None]]])
print(max_value_length(binary_tree))

binary_tree = create_tree_from_nested_list(["Hoiho", ["Kaki", ["Takahe", None, None], None], ["Ruru", None, ["Moa", None, ["Piwaiwaka", None, None]]]])
print(max_value_length(binary_tree))




