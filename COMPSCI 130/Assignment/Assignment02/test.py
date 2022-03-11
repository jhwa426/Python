class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []


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


    





##Test
item_collection = UndoRedo()
item_collection.add_item("Weka") # current=Weka
item_collection.add_item("Kaka") # current=Kaka; Weka into back
item_collection.add_item("Kiwi") # current=Kiwi; Kaka into back
print(item_collection.get_prev()) # pop Kaka from back. current=Kaka; Kiwi into forward
item_collection.add_item("Tui") # current=Tui; Kaka into back; clears forward stack
print(item_collection.get_prev()) # pop Kaka from back; current=Kaka; Tui into forward
print(item_collection.get_next()) # current=Tui; Kaka into back

