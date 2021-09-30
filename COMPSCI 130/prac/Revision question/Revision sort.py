######Revision sort

####bubble_sort
def my_bubble_sort(data):
    number = len(data)

    for i in range(number - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

        print(data)
           
        

####Test
##letters = ['e', 'd', 'c', 'b', 'a']
##my_bubble_sort(letters)
##print(letters)
##my_bubble_sort([93, 54, 78, 18, 61, 13])

####selection sort
def my_selection_sort(data):
    number = len(data)
    for i in range(number - 1, 0 ,-1): ##fill slot
        pos_of_max = 0
        for j in range(1, i + 1): ##location
            if data[j] > data[pos_of_max]:
                pos_of_max = j
        data[i], data[pos_of_max] = data[pos_of_max], data[i]
        print(data)

####Test    
####my_selection_sort([36, 42, 16, 60, 58, 92])



####insertion sort
def my_insertion_sort(data):
    for index in range(1, len(data)):
        current_value = data[index]
        position = index
        while position > 0 and data[position - 1] > current_value:
            data[position] = data[position - 1]
            position -= 1
        data[position] = current_value
        print(data)


####Test     
my_insertion_sort([15,11,1,3,8])
my_insertion_sort([10, 25, 5, 3, 18, 1, 13, 6, 20])
my_insertion_sort([20, 10, 15, 25, 6, 35])
my_insertion_sort([36, 42, 16, 60, 58, 92])



####Binary Search
def binary_search(numbers, value):
    max_index = len(numbers) - 1 #1
    min_index = 0 #2
    while (min_index <= max_index): 
        mid_point = (max_index + min_index) // 2 #3
        element = numbers[mid_point]
        if element == value: #4
            return mid_point 
        elif element > value:
            max_index = mid_point - 1
        else:
            min_index = mid_point + 1
    return -1
            

####Test
numbers = [10, 15, 20, 27, 41, 69]
print(binary_search(numbers, 69)) #5

numbers = [13, 18, 54, 61, 78, 93]
print(binary_search(numbers, 10)) #-1









