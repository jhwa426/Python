######Lab 12
######24.09.2020
######

##Ex 1
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


    ##Ex 3
    def push_list(self, a_list):
        for word in a_list:
            self.push(word)

    ##Ex 4
    def multi_pop(self, number):
        index = number
        if len(self.__items) >= index:
            for word in range(index):
                self.__items.pop()
            return True
        else:
            return False

    ##Ex 5
    def copy(self):
        new_stack = Stack()
        for element in self.__items:
            new_stack.push_list([element])

        return new_stack

    ##Ex 6
    def __eq__(self, other):
        if not isinstance(other, Stack):
            return False

        return self.__items == other.__items
      

##Ex 7
def reverse_sentence(sentence):
    word_stack = Stack()
    
    for word in sentence.split():
        word_stack.push(word)

    word_list = []
    
    while not word_stack.is_empty():
        word_list.append(word_stack.pop())
    
    return " ".join(word_list)


##Test
##print(reverse_sentence('hello world'))

##Ex 8
def is_balanced_brackets(text):
    bracket_stack = Stack()
    
    open_bracket = ["(", "[", "{"] 
    close_bracket = [")", "]","}"]

    for bracket in text:
        if bracket in open_bracket:
            bracket_stack.push(bracket)
        elif bracket in close_bracket:
            position = close_bracket.index(bracket)
            if bracket_stack.size() != 0 and open_bracket[position] == bracket_stack.peek():
                bracket_stack.pop()
            else:
                return False
            
    if bracket_stack.size() == 0:
        return True
    else:
        return False



##Ex 9
##postfix_stack = Stack()
##postfix_stack.push(3)
##postfix_stack.push(4)
##postfix_stack.pop()
##postfix_stack.pop()
####postfix_stack.push(3*4)
####postfix_stack.push(6)
####postfix_stack.pop()
####postfix_stack.pop()
####postfix_stack.push(12/6)
####postfix_stack.pop()
##postfix_stack.push(12/6 + 3)
####print(postfix_stack.peek())
##
##
##
####equation = '34*6/3+'
####
######12 6/3+
####
####expression = ["+", "-", "*", "/"]
####for element in equation:
####    if element == '+':
####        op2 = postfix_stack.pop()
####        op1 = postfix_stack.pop()
####        postfix_stack.push(op1 + op2)
####    elif element == '-':
####        op2 = postfix_stack.pop()
####        op1 = postfix_stack.pop()
####        postfix_stack.push(op1 - op2)
####    elif element == '*':
####        op2 = postfix_stack.pop()
####        op1 = postfix_stack.pop()
####        postfix_stack.push(op1 * op2)
####    elif element == '/':
####        op2 = postfix_stack.pop()
####        op1 = postfix_stack.pop()
####        postfix_stack.push(op1 / op2)
####    else:
####        postfix_stack.push(int(element))
####
####print(postfix_stack)

##Ex 10

def evaluate_postfix(postfix_list):
    postfix_stack = Stack()
    for element in postfix_list:
        if element == '+':
            num2 = postfix_stack.pop()
            num1 = postfix_stack.pop()
            postfix_stack.push(num1 + num2)
        elif element == '-':
            num2 = postfix_stack.pop()
            num1 = postfix_stack.pop()
            postfix_stack.push(num1 - num2)
        elif element == '*':
            num2 = postfix_stack.pop()
            num1 = postfix_stack.pop()
            postfix_stack.push(num1 * num2)
        elif element == '/':
            num2 = postfix_stack.pop()
            num1 = postfix_stack.pop()
            postfix_stack.push(int(num1 / num2))
        elif element == "^":
            num2 = postfix_stack.pop()
            num1 = postfix_stack.pop()
            postfix_stack.push(num1 ** num2)
        elif element == "%":
            num2 = postfix_stack.pop()
            num1 = postfix_stack.pop()
            postfix_stack.push(num1%num2)
        else:
            postfix_stack.push(int(element))
            
    return postfix_stack.peek()

##print(evaluate_postfix(["3", "4", "*", "6", "/", "3", "+"]))
##print(evaluate_postfix(['2', '10', '^']))
##print(evaluate_postfix(['2', '4', '3', '*', '^']))
##print(evaluate_postfix(['10', '4', '2', '-', '5', '*', '+', '3', '%']))
##print(evaluate_postfix(['7', '2', '9', '8', '-', '*', '3', '/', '+']))
##print(evaluate_postfix(['6', '2', '/', '5', '*']))
##print(evaluate_postfix(['5', '2', '/']))

def compute(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 // number2














