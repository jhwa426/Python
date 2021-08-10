class Node:

    def __init__(self,value,next=None):
        self.value = value
        self.next = next

    def getNext(self):
        return self.next

    def getValue(self):
        return self.value

class LinkedList:

    def __init__(self,node):
        self.node = node

    def __str__(self):
        node = self.node
        s = "[Node " + str(node.getValue())
        if node.getNext() is None:
            return s + "]"
        while node.next is not None:
            s += ", Node " + str(node.next.value)
            node = node.next
        return s + "]"

    def add(self,newNode):
        node = self.node
        while node.next is not None:
            node = node.next
        node.next = newNode


values = LinkedList()
values.add('cherry')
values.add('banana')
values.add('apple')
print(values)
