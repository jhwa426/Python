######Lab 16
######07.10.2020
######

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
            

####Ex 2
##    def put(self, key):
##        if self.__size == self.__count:
##            raise IndexError("ERROR: The hash table is full.")         
##        slot = self.get_new_hash_code_linear_probing(key)
##        if self.__slots[slot] != key:
##            self.__slots[slot] = key
##            self.__count += 1
##
##    def __len__(self):
##        return self.__count
        

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

##my_hash_table = SimpleHashTable(5)
##my_hash_table.put(13)
##my_hash_table.put(26)
##my_hash_table.put(14)
##my_hash_table.put(15)
##my_hash_table.rehashing(11)
##print(my_hash_table)


##Ex 6
class QuadraticHashTable:
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

    def get_new_hash_code_quadratic_probing(self, index, distance = 1):
        slot = self.get_hash_code(index)

        while self.__slots[slot] != None:
            slot = (index + (distance ** 2)) % self.__size
            distance += 1

        return slot

    def put(self, key):
        if self.__size == self.__count:
            raise IndexError("ERROR: The hash table is full.")

        position = self.get_hash_code(key)

        if self.__slots[position] != None:
            slot = self.get_new_hash_code_quadratic_probing(position)
            self.__slots[slot] = key
            self.__count += 1
        else:
            self.__slots[position] = key
            self.__count += 1



##my_hash_table=QuadraticHashTable()
##my_hash_table.put(1)
##print(my_hash_table)
##my_hash_table.put(8)
##print(my_hash_table)
##my_hash_table.put(15)
##print(my_hash_table)
##my_hash_table.put(22)
##print(my_hash_table)


##Ex 7
class DoubleHashTable:
    def __init__(self, size = 7, second_hash_value = 5):
        self.__size = size
        self.__slots = [None] * self.__size
        self.__second_hash_value = second_hash_value
        self.__count = 0
        
    def __str__(self):
        return str(self.__slots)

    def get_hash_code(self, key):
        return key % (self.__size)

    def get_size(self):
        return self.__size    

    def get_new_hash_code_double_hashing(self, key):
        position = self.get_hash_code(key)
        step_size = self.__second_hash_value - (key % self.__second_hash_value)      
        step = 1
        swap = position
        while self.__slots[swap] != None:
            swap = (position + step * step_size) % self.__size
            step += 1
            
        return swap

    def put(self, key):
        if self.__size == self.__count:
            raise IndexError("ERROR: The hash table is full.")

        position = self.get_hash_code(key)
        
        if self.__slots[position] != None:
            slot = self.get_new_hash_code_double_hashing(key)
            self.__slots[slot] = key
            self.__count += 1
        else:
            self.__slots[position] = key
            self.__count += 1



##my_hash_table=DoubleHashTable()
##my_hash_table.put(1)
##print(my_hash_table)
##my_hash_table.put(8)
##print(my_hash_table)
##my_hash_table.put(15)
##print(my_hash_table)
##my_hash_table.put(22)
##print(my_hash_table)
##my_hash_table.put(41)
##print(my_hash_table)

##my_hash_table=DoubleHashTable()
##my_hash_table.put(26)
##my_hash_table.put(54)
##my_hash_table.put(94)
##my_hash_table.put(15)
##my_hash_table.put(28)
##print(my_hash_table)


##Ex 8
class LinkedListHashTable:
    def __init__(self, size = 7):
        self.__size = size
        self.__slots = []
        for index in range(self.__size):
            self.__slots.append(LinkedList())
        self.__count = 0

    def get_hash_code(self, key):
        return key % (self.__size)

    def __str__(self):
        result = ""
        for element in self.__slots:
            result += "\n" + str(element) 
        result = result.replace('\n', '', 1)
        
        return result

##Ex 9
    def put(self, key):
        slot = self.get_hash_code(key)
        self.__slots[slot].add(key)
        self.__count += 1

        return self.__slots


    def __len__(self):
        return self.__count
        







    







    
