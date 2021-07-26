##Test

##Ex
##selction sort

##def selection_sort(a_list):
##    for fill_slot in range(len(a_list) - 1, 0, -1):
##        pos_of_max = 0
##        for location in range(1, fill_slot + 1):
##            if a_list[location] > a_list[pos_of_max]:
##                    pos_of_max = location
##        a_list[fill_slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[fill_slot]
##        print(a_list)
##
##
##selection_sort([10, 25, 5, 3, 18, 1, 13, 6, 20])
##
##selection_sort([12, 7, 24, 44, 19, 32])



##Ex
##Bubble Sort

##def bubble_sort(a_list):
##    print(a_list)
##    for pass_num in range(len(a_list) - 1, 0, -1):
##        for i in range(len(a_list) - 2, 0, -1):
##            if a_list[i] > a_list[i + 1]:
##                    a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
##        print(a_list)
        
##bubble_sort([10, 25, 5, 3, 18, 1, 13, 6, 20])


##def short_bubble_sort(a_list):
##    print(a_list)
##    exchanges = True
##    pass_num = len(a_list) - 1
##    while pass_num > 0 and exchanges:
##        exchanges = False
##        for i in range(pass_num):
##            if a_list[i] > a_list[i + 1]:
##                exchanges = True
##                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
##        print(a_list)
##        pass_num = pass_num - 1
####
######short_bubble_sort([10, 25, 5, 3, 18, 1, 13, 6, 20])
####short_bubble_sort([12, 23, 10, 34, 5])
##short_bubble_sort([93, 54, 78, 18, 61, 13])



##Ex
##insertion sort
##def insertion_sort(data):
##    for index in range(1, len(data)):
##        current_value = data[index]
##        position = index
##        while position > 0 and data[position - 1] > current_value:
##            data[position] = data[position - 1]
##            position -= 1
##        data[position] = current_value
##        print(data)
##
##
####insertion_sort(['b', 'c', 'a', 'e', 'f'])
##insertion_sort(['h', 't', 'w', 'e', 'q', 'c', 'x'])
####insertion_sort([15, 11, 1, 3, 8])
####insertion_sort([10, 25, 5, 3, 18, 1, 13, 6, 20])
####insertion_sort([20, 10, 15, 25, 6, 35])

##Ex
##Binary Search
def bin_search(a_list, item):
    first = 0
    last = len(a_list)
    while first < last:
        midpoint = (first + last) // 2
        element = a_list[midpoint]
        if item == element:
            return True
        elif item < element: # first half
            last = midpoint
        else:
            first = midpoint + 1
    return False

print('Is 18 in the list?')
ans = bin_search([ 1, 3, 5, 6, 9, 10, 13, 18, 20 ], 10)
print(ans)

