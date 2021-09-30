## COMPSCI 101
## 29.06.2020

##Ex 1

##def words(list1, list2):
##    if len(list1) != len(list2):
##        return False
##    for check in list1:
##        if check not in list2:
##            return False
##    for check in list2:
##        if check not in list1:
##            return False
##    return True
    
##Ex 2

##def get_count(list1, list2):
##
##    count = 0
##    min_length = min(len(list1), len(list2))
##
##    for index1 in range(min_length):
##        element1 = list1[index1]
##        index2 = len(list2) - index1 - 1
##        element2 = list2[index2]
##
##        if element1 == element2:
##            count = count + 1
##        else:
##            return count
##
##    return count
##
##a = [10,20,30,40]
##b = [1, 2, 3, 4]
##
##print(get_count(a, b))

##Ex 3

##nums = [5, 6, 7, 8, 9]
#### [5, 6, 10, 8, 9]?


##Ex 5
##def secret(numbers):
##    for index in range(len(numbers)):
##        if numbers[index] == index:
##            return 0
##    return 1
##
##a = [8, 1, 4, 5, 7]
##print(secret(a))


##Ex 6

##def question(numbers):
##    x = 0
##    for index in range(5):
##        if index < 2: 
##            x += numbers[index]
##        elif index > 2:
##            x -= numbers[index]
##    return x
##        
##numbers = [2, 34, 40, 46, -10]
##print(question(numbers))


##Ex 7
##def main():
##    result1 = functional(2, 5)
##    print("A", result1)
##    result2 = functional(8, 0)
##    print("B", result2)
##    result3 = functional(6, -1)
##    print("C", result3)
##    print(result1 + result2 + result3)
##
##
##def functional(num1, num2):
##    if num1 < num2 and num2 > 4:
##        if num2 != 6:
##            return num1 + num2
##        else:
##            return num1 - num2
##    elif num2 < 0:
##        return num1 * 2
##    else:
##        return num1 // 2
##
##main()
        
    


##Ex 13

##def main():
##    a_list = [5, 7, 2]
##    do_something_a(a_list)
##    print("a_list:", a_list)
##
##def do_something_a(list1):
##    list2 = list1
##    to_consider = [1, 6]
##    for element in to_consider:
##        list2.insert(0, element)
##
##    list1.reverse()
##
##main()



##Ex 14

##def main():
##    a_list = [5, 4]
##    do_something_b(a_list)
##    print("a_list:", a_list)
##
##def do_something_b(list1):
##    list2 = list1
##    list1 = [4, 3]
##    for element in [1, 5,3]:
##        if element not in list1:
##            list1.append(element)
##    list1 = list2
##
##main()

##Ex 15

##def main():
##    data_dict = {"Balrog":[73,67,47,44], "Bison":[63, 54, 25], "Chun Li":[95, 89, 72, 66], "Ken":[100, 75, 65, 55], "Ryu":[100, 95, 80, 70]}
##    filename = "Output.txt"
####    write_to_file(filename, data_dict, 4)
##    write_to_file(filename, data_dict, 2)
##
##def write_to_file(filename, data_dict, max_length):
##    key_list = list(data_dict.keys())
##    key_list.sort()
##    output_stream = open(filename, "w")
##    for key in key_list:
##        output_stream.write(key + ": ")
##        values = data_dict[key]
##        values.sort()
##        if len(values) > max_length:
##            values = values[len(values) - max_length:]
##        for i in range(len(values) - 1 , -1, -1):
##            if i == 0:
##                output_stream.write(str(values[i]) + "\n")
##            else:
##                output_stream.write(str(values[i]) + ", ")
##                
##    output_stream.close()
##    
##                            
##main()



####Ex 17

def nested_loop_question(number):
    total = 0
    for i in range(1, number + 1):
        for j in range(i):
            total = total + 1
    return total

print(nested_loop_question(7))
print(nested_loop_question(0))
print(nested_loop_question(10))
print(nested_loop_question(13))



##Ex 18
##import random
##def replace_letter(word):
##    alphabet = "abcdefghijklmnopqrstuvwxyz"
##    random_word = random.randrange(len(word))
##    random_alphabet = random.randrange(len(alphabet))
##    while word[random_word] == alphabet[random_alphabet]:
##        random_alphabet = random.randrange(len(alphabet))
##
##    first_word = word[random_word]
##    middle_word = alphabet[random_alphabet]
##    result = word[:random_word] + middle_word + word[random_word + 1:]
##
##    return result
##    
##
##print(replace_letter("awesome"))

##Ex 20

##def booleans_1(number1, number2):
##    if (len(number1) == 3 and number1 % number2 == 0) or number2 % number1 == 0:
##        print("Yes")

##Ex 21

##def booleans_2(word1, word2, letter):
##    if word1[0] != word2[0] and (word1 in letter and word2 in letter):
##        print("Yes")


##Ex 22
##def booleans_3(value):
##    if value > 14 and value < 65 and value % 5 == 0 or value % 2 == 0:
##        print("A")
##    elif value % 3 == 0 or value % 2 == 0 and value > 42:
##        print("B")
##    elif value < 54:
##        print("C")
##    else:
##        print("D")
##
##def main():
##    booleans_3(20)
##    booleans_3(69)
##    booleans_3(53)
##    booleans_3(67)
##
##main()

##from tkinter import *
##
##def main():
##    window = Tk()
##    window.title("Red and green pattern")
##    window.config(background = "white")
##    window.geometry("250x250+10+20")
##    a_canvas = Canvas(window)
##    a_canvas.config(background = "white")
##    a_canvas.pack(fill = BOTH, expand = True)
##    draw_grid(a_canvas)
##    draw_pattern_in_canvas(a_canvas, 50, 0, 0, 4)
##    window.mainloop()
##
##def draw_grid(canvas):
##    for row in range(50, 350, 50):
##        canvas.create_line(-1, row, 501, row, fill = "lightblue")
##    for column in range(50, 500, 50):
##        canvas.create_line(column, -1, column, 351, fill = "lightblue")
##
##
##def draw_pattern_in_canvas(a_canvas, size, left_hand_side, y_down, n):
##    for row in range(1, n + 1):
##        x_left = left_hand_side
##        for col in range(1, n + 1):
##            rect = (x_left + 2, y_down + 2, x_left + size - 2, y_down + size - 2)
##            if col == (n - row + 1):
##                a_canvas.create_rectangle(rect, fill = "red")
##            x_left = x_left + size
##        y_down = y_down + size
##
##main()








