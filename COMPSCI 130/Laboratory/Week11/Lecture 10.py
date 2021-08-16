##Lecture 10

class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.left = self.left
            self.left = t

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.right = self.right
            self.right = t
    
    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    
a = BinaryTree(10)

a.insert_left(5)
a.insert_right(15)
a.insert_right(999)

x = a.get_left()
x.insert_left(2)
x.insert_right(7)
