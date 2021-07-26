##Lab 6
##18.08.2020

##Ex 1

def short_bubble_sort(a_list):
    print(a_list)
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        print(a_list)
        pass_num = pass_num - 1
##
##Test
##short_bubble_sort([93, 54, 78, 18, 61, 13])
short_bubble_sort([93, 54, 78, 18, 61, 13])

##def short_bubble_sort(data, index):
##    count = 0
##    number = len(data)
##
##    for i in range(number - 1, 0, -1):
##        for j in range(i):
##            if data[j] > data[j+1]:
##                data[j] ,data[j+1] = data[j+1], data[j]
##        count +=1
##        if count == index:
##            return data




##Ex 2      
##def bubble_row(data, index):
##    for i in range(index):
##        if data[i] > data[i+1]:
##            data[i], data[i+1] = data[i+1], data[i]
## 
##
####Test
##letters = ['e', 'd', 'c', 'b', 'a'] #['d', 'c', 'b', 'a', 'e']
##bubble_row(letters , 4)
##print(letters)
##
##letters = ['e', 'd', 'c', 'b', 'a'] #['d', 'c', 'e', 'b', 'a']
##bubble_row(letters, 2)
##print(letters)
##
##letters = ['m', 'v', 'o', 'd', 'h', 'l', 'y', 's', 'x', 'z']
###['m', 'o', 'd', 'h', 'v', 'l', 'y', 's', 'x', 'z']
##bubble_row(letters, 4)
##print(letters)


##Ex 3

##def my_bubble_sort(data):
##    count = 0
##    number = len(data)
##
##    for i in range(number - 1, 0, -1):
##        for j in range(i):
##            if data[j] > data[j+1]:
##                data[j] ,data[j+1] = data[j+1], data[j]
##        count +=1
##        
##    return data
##
##
####Test
##letters = ['e', 'd', 'c', 'b', 'a']
##my_bubble_sort(letters)
##print(letters)

##selction sort
##Ex 4
def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                    pos_of_max = location
        a_list[fill_slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[fill_slot]
        print(a_list)
####        
####Test
##selection_sort([0, 4, 2, 7, 5])
##selection_sort([36, 42, 16, 60, 58, 92])
##selection_sort([12, 7, 24, 44, 19, 32])
##selection_sort([100, 98, 24, 44, 1, 32])
##selection_sort([12, 7, 24, 44, 19, 32])

##Ex 5
##def get_position_of_highest(data, index):
##    pos_of_max = 0
##    for i in range(1, index + 1):
##        if data[i] > data[pos_of_max]:
##            pos_of_max = i
##            
##    return pos_of_max
##
##
####Test
##letters = ['e', 'd', 'c', 'b', 'a']
##print(get_position_of_highest(letters, 4)) # 0
##
##letters = ['g', 'y', 'd', 'h', 'w', 't', 'e', 'q', 'c', 'x', 'b', 'f', 'u', 'r', 'k', 'm']
##print(get_position_of_highest(letters, 2)) # 1
##
##letters = ['y', 'd', 'h', 'w', 't', 'e', 'q', 'a']
##print(get_position_of_highest(letters, 3)) #0
##
##letters = ['t', 'e', 'q', 'c', 'x', 'b']
##print(get_position_of_highest(letters, 2)) #0
##
##letters = ['t', 'e', 'q', 'c', 'x', 'b', 'f', 'u', 'r', 'k']
##print(get_position_of_highest(letters, 4)) #4


##Ex 6
##def selection_row(data, index):
##    pos_of_max = 0
##    for i in range(1, index + 1):
##        if data[i] > data[pos_of_max]:
##            pos_of_max = i
##    data[i], data[pos_of_max] = data[pos_of_max], data[i]


####Test
##letters = ['e', 'd', 'c', 'b', 'a']
##selection_row(letters, 4)
##print(letters) #['a', 'd', 'c', 'b', 'e']
##
##letters = ['b', 'f', 'u', 'r', 'k']
##selection_row(letters, 3)
##print(letters) #['b', 'f', 'r', 'u', 'k']



##Ex 7
def my_selection_sort(data):
    for fill_slot in range(len(data) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if data[location] > data[pos_of_max]:
                pos_of_max = location
        data[fill_slot], data[pos_of_max] = data[pos_of_max], data[fill_slot]
        


##Test
##letters = ['e', 'd', 'c', 'b', 'a']
##my_selection_sort(letters)
##print(letters) #['a', 'b', 'c', 'd', 'e']

    

##Ex 8
##insertion sort

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
                a_list[position] = a_list[position - 1]
                position -= 1
        a_list[position] = current_value
        print(a_list)

##insertion_sort([10, 25, 5, 3, 18, 1, 13, 6, 20])
##insertion_sort([20, 10, 15, 25, 6, 35])
##insertion_sort([36, 42, 16, 60, 58, 92])


##Ex 9
##def shifting(data, index):
##    item_to_check = data[index]
##    while index > 0 and data[index - 1] > item_to_check:
##        data[index] = data[index - 1]
##        index -= 1
##
##
##letters = ['a', 'c', 'f', 'b', 'g']
##shifting(letters, 3)
##print(letters) #['a', 'c', 'c', 'f', 'g']
##
##letters = ['b', 'c', 'k', 'a', 'z', 'n', 'j', 's']
##shifting(letters, 3)
##print(letters) #['b', 'b', 'c', 'k', 'z', 'n', 'j', 's']
##
##  
####Ex 10
##def insertion_row(data, index):
##    item_to_insert = data[index]
##    while index > 0 and data[index - 1] > item_to_insert:
##        data[index] = data[index - 1]
##        index -= 1
##
##    data[index] = item_to_insert
##
####Test
##letters = ['b', 'c', 'a', 'e', 'f']
##insertion_row(letters, 2)
##print(letters) #['a', 'b', 'c', 'e', 'f']
##
##letters = ['h', 't', 'w', 'e', 'q', 'c', 'x']
##insertion_row(letters, 3)
##print(letters) #['e', 'h', 't', 'w', 'q', 'c', 'x']
##
##
####Ex 11
def my_insertion_sort(data):
    for index in range(1, len(data)):
        current_value = data[index]
        position = index
        while position > 0 and data[position - 1] > current_value:
            data[position] = data[position - 1]
            position -= 1
        data[position] = current_value
        print(data)


##Test
letters = ['x', 'b', 'f', 'u', 'r', 'k']
my_insertion_sort(letters)
print(letters) #['b', 'f', 'k', 'r', 'u', 'x']



##Ex 12
def binary_search(numbers, value):
    max_index = len(numbers) - 1
    min_index = 0
    while (min_index <= max_index):
        mid_point = (min_index + max_index) // 2
        element = numbers[mid_point]
        if value == element:
            return mid_point
        elif value < element:
            max_index = mid_point - 1
        else:
            min_index = mid_point + 1
        
    return -1



######Test
##numbers = [10, 15, 20, 27, 41, 69]
##print(binary_search(numbers, 69)) #5
##
##numbers = [13, 18, 54, 61, 78, 93]
##print(binary_search(numbers, 10)) #-1








