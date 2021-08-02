##21.09.2020
##Lecture 7

class Stack:

    def __init__(self):
        self.items= []

    def is_empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __str__(self):
        return str(self.items)

##s=Stack()
##print(s.is_empty())
##s.push(4)
##s.push("dog")
##s.push(True)
##s.push(8.4)
##print(s.is_empty())
##print(s.size())
##print(s.pop())
##print(s.pop())
##print(s.pop())
##print(s.pop())

class Queue:
    def __init__(self):
        self.items= []
        
    def is_empty(self):
        return self.items==[]
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.insert(0,item)
        
    def dequeue(self):
        self.items.pop()

    def __str__(self):
        return str(self.items)


q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
##q.enqueue(q.dequeue())
print(q)



