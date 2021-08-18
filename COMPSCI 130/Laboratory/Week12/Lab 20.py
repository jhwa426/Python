######Lab 20
######29.10.2020
######

##Ex 4
class PriorityQueue:
    def __init__(self):
        self.__binary_heap = [0]
        self.__size = 0

    def __str__(self):
        return str(self.__binary_heap)

    def __len__(self):
        return len(self.__binary_heap) - 1

    ##Ex 5
    def add_all(self, a_list):
        for number in a_list:
            self.__binary_heap.append(number)
    ##Ex 6       
    def percolate_up(self, index):
        while index // 2 > 0:
            if self.__binary_heap[index] < self.__binary_heap[index // 2]:
                self.__binary_heap[index // 2], self.__binary_heap[index] = self.__binary_heap[index], self.__binary_heap[index // 2]
                
            index = index // 2
    
##    def percolate_up(self, index):
##        while index // 2 > 0:
##            if self.__binary_heap[index] < self.__binary_heap[index // 2]:
##                temp = self.__binary_heap[index // 2]
##                self.__binary_heap[index // 2] = self.__binary_heap[index]
##                self.__binary_heap[index] = temp
##            index = index // 2
            
    ##Ex 7
    def insert(self, element):
        self.__binary_heap.append(element)
        self.__size += 1
        self.percolate_up(self.__size)
        

    ##Ex 8
    def get_smaller_child_index(self, index):
        if index * 2 + 1 > len(self):
            return index * 2
        
        else:
            #left
            if self.__binary_heap[index * 2] < self.__binary_heap[index * 2 + 1]:
                return index * 2
            
            #right
            else:
                return index * 2 + 1
            


    ##Ex 9
    def percolate_down(self, index):
        while index * 2 <= len(self):
            min_child = self.get_smaller_child_index(index)
            
            if self.__binary_heap[index] > self.__binary_heap[min_child]:
                self.__binary_heap[index], self.__binary_heap[min_child] = self.__binary_heap[min_child], self.__binary_heap[index]
                
            index = min_child



    ##Ex 10
    def create_heap_fast(self, values):
        index = len(values) // 2
        self.__binary_heap = [0] + values

        while index > 0:
            self.percolate_down(index)
            index -= 1
        




##Test
pq = PriorityQueue()
keys = [9, 5, 8, 6, 3, 2]
pq.create_heap_fast(keys)
print(pq)











        


