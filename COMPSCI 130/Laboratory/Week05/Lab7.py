##Lab 7
##20.08.2020

##Ex 1
##def insertion_sort(data):	
##    for index in range(1, len(data)):
##        item_to_insert = data[index]
##        i = index - 1
##        while i >= 0 and data[i][1] < item_to_insert[1]:
##            data[i + 1] = data[i]
##            i -= 1
##        data[i + 1] = item_to_insert
##          
####Test
##s1 = (7, "Smith")
##s2 = (5, "Brown")
##s3 = (4, "Chan")
##s4 = (2, "Kim")
##s5 = (0, "Lin")
##s6 = (1, "Singh")
##s7 = (3, "Gupta")
##students = [s1, s2, s3, s4, s5, s6, s7]
##insertion_sort(students)
##for x in students:
##    print(x)

####(7, 'Smith')
####(1, 'Singh')
####(0, 'Lin')
####(2, 'Kim')
####(3, 'Gupta')
####(4, 'Chan')
####(5, 'Brown')


##Ex 2
####def double(my_list):
####    result = [index * 2 for index in my_list]
    
##def double(my_list):
##    for index in range(len(my_list)):
##        my_list[index] *= 2
##
##        
####Test
##my_list = [1, 2, 3]
##double(my_list)
##print(my_list) #[2, 4, 6]
##
##numbers = [3, 2, 1]
##id_before = id(numbers)
##double(numbers)
##print(numbers)
##id_after = id(numbers)
##print(id_before == id_after) #same reference before and after
####[6, 4, 2]
###True

##Ex 3
def get_middle_number(numbers):
    numbers.sort()
    middle_num1 = int(len(numbers) / 2) ##float
    middle_num2 = len(numbers)//2 ##int

    if len(numbers) % 2 != 0:
        return numbers[middle_num1]
    else:
        return numbers[middle_num2]



##Test
numbers1 = [20, 24, 3, 8, 9]  #if sorted [3, 8, 9, 20, 24]
numbers2 = [15, 28, 22, 21]   #if sorted [15, 21, 22, 28]
numbers3 = [18, 9, 8, 5, 12, 25, 4, 3, 7] #if sorted [3, 4, 5, 7, 8, 9, 12, 18, 25]
print("1.", get_middle_number(numbers1)) ##1. 9
print("2.", get_middle_number(numbers2)) ##2. 22
print("3.", get_middle_number(numbers3)) ##3. 8

numbers3 = [18, 9, 8, 5, 12, 25, 4, 3, 7]  #if sorted [3, 4, 5, 7, 8, 9, 12, 18, 25]
numbers4 = [8, 24, 4, 10, 10, 25, 23, 21, 24, 5, 4, 6, 23, 23, 19]
print("3.", get_middle_number(numbers3)) #3. 8
print("4.", get_middle_number(numbers4)) #4. 19


##Ex 4
##def get_middle_number_from_file(filename):
##    input_file = open(filename, "r")
##    contents = input_file.read().split()
##    input_file.close()
##    numbers = []
##    
##    for number in contents:
##        numbers.append(int(number))
##    numbers.sort()
##
##    middle_num1 = int(len(numbers) / 2) ##float
##    middle_num2 = len(numbers)//2 ##int
##    if len(numbers) % 2 != 0:
##        return numbers[middle_num1]
##    else:
##        return numbers[middle_num2]
##    
##
##
####Test
##print("1.", get_middle_number_from_file('numbers1.txt'))
##print("2.", get_middle_number_from_file('numbers2.txt'))
##print("3.", get_middle_number_from_file('numbers3.txt'))

##Ex 5
##def get_middle_number_from_file(filename):
##    try:
##        input_file = open(filename, "r")
##        contents = input_file.read().split()
##        input_file.close()
##        numbers = []
##        alpabet = "abcdefghijklmnopqrstuvwxyz"
##
##        for number in contents:
##            if "." in number:
##                number = round(float(number))
##                numbers.append(number)
##                print('ERROR: "'"{}"'" contains an invalid value.'.format(filename))
##            elif number in alpabet:
##                print('ERROR: "{}" contains an invalid value.'.format(filename))
##            else:
##                numbers.append(int(number))
##                
##        numbers.sort()
##        middle_num = len(numbers) // 2
##        
##        return numbers[middle_num]
##
##
##    except FileNotFoundError:
##        return 'ERROR: "'"{}"'" does not exist.'.format(filename)
##    except IndexError:
##        return 'ERROR: "{}" is empty.'.format(filename)
##    
##
##    
##print(get_middle_number_from_file('test0.txt')) #ERROR: "test0.txt" does not exist.
##print(get_middle_number_from_file('test1.txt')) #ERROR: "test1.txt" is empty.
##print(get_middle_number_from_file('test2.txt')) #12
##print(get_middle_number_from_file('test8.txt')) #ERROR: "test8.txt" contains an invalid value.
###################################################ERROR: "test8.txt" contains an invalid value.
###################################################6
##print(get_middle_number_from_file('test9.txt')) #ERROR: "test9.txt" contains an invalid value.
#################################################12

##Ex 6
##def linear_search(student_id, students):
##    for index in range(len(students)):
##        if students[index][0] == student_id:
##            return students[index][1]

##Test
##s1 = (7, "Smith")
##s2 = (5, "Brown")
##s3 = (4, "Chan")
##s4 = (2, "Kim")
##s5 = (0, "Lin")
##students = [s1, s2, s3, s4, s5]
##print(linear_search(0, students)) #Lin

##s1 = (1, "Anderson")
##s2 = (2, "Huang")
##s3 = (3, "Ng")
##s4 = (4, "Roberts")
##s5 = (5, "Smith")
##s7 = (7, "Zhou")
##students = [s1, s2, s3, s4, s5, s7]
##print(linear_search(-456, students)) #None

##Ex 7
##def get_unique_letters(word_a, word_b):
##    result = ''
##    for letter in word_a:
##        if letter not in word_b and letter not in result:
##            result += letter
##
##    for letter in word_b:
##        if letter not in word_a and letter not in result:
##            result += letter
##            
##    return ''.join(sorted(result))

##def get_unique_letters(word_a, word_b):
##    result = []
##    for letter in word_a:
##        if letter not in word_b and letter not in result:
##            result.append(letter)
##    
##    for letter in word_b:
##        if letter not in word_a and letter not in result:
##            result.append(letter)
##        
##    return ''.join(sorted(result))

         
##Test
##print(get_unique_letters('hello', 'world')) #dehrw
##print(get_unique_letters('world', 'hello')) #dehrw
##print(get_unique_letters('x', 'aaxxxaa')) #a
##print(get_unique_letters('xa', 'aaxxxaa')) #ax
##print(get_unique_letters('constructionism', 'circles')) #elmnotu


##Ex 8
##def rotate_3(numbers):
##    a_list = []
##    b_list = []
##
##    for index in range(len(numbers)):
##        if index <= 2:
##            a_list.append(numbers[index])
##        else:
##            b_list.append(numbers[index])
##    return b_list + a_list
##        
##    
##
####Test
##numbers = [7,72,91,39,30,78,62,52,43,28]
##print(rotate_3(numbers)) #[39, 30, 78, 62, 52, 43, 28, 7, 72, 91]
##
##numbers = [1]
##result = rotate_3(numbers)
##print(result) #[1]
##
##numbers = [58,11,35,83,97,65,96,39,74,18,4]
##print(rotate_3(numbers)) #[83, 97, 65, 96, 39, 74, 18, 4, 58, 11, 35]


##Ex 9
##def get_list_of_odd_maximums(a_list_of_lists):
##    odd_list = []
##    for i in a_list_of_lists:
##        a_list = []
##        for j in i:
##            if j % 2 != 0:
##                odd_num = j
##                a_list.append(odd_num)
##
##        if len(a_list) > 0:
##            odd_list.append(max(a_list))
##        else:
##            odd_list.append(None)
##
##    return odd_list        
##
####Test
##a_list_of_lists = [ [3, 42, 678, -5, -5],
##                [-4, -2, -33, -29, 0],
##                [51],
##                [4, 6, -4],
##                [-309, -3, -34] ]
##
##result = get_list_of_odd_maximums(a_list_of_lists)
##print("Odd maximums:", result) #Odd maximums: [3, -29, 51, None, -3]
##
##a_list_of_lists = [ [4, -4],
##                [-5, -4, -7, 0],
##                [-82],
##                [-5, 5, 3, -2] ]
##result = get_list_of_odd_maximums(a_list_of_lists)
##print("Odd maximums:", result) #Odd maximums: [None, -5, None, 5]



##Ex 10
##def draw_triangle(size):
##    count = size // 2
##    for row in range(1, count+1):
##        if size - 10 == 0:
##            print(row * "X")
##        for column in range(row):
##            
##                
##            
##
##        
##    print(size * "X")
##
####Test
##draw_triangle(10)



##Ex 11
##def swaps(numbers):
##    count = 0
##    for fill_slot in range(len(numbers) - 1, 0, -1):
##        pos_of_max = 0
##        for location in range(1, fill_slot + 1):
##            if numbers[location] > numbers[pos_of_max]:
##                pos_of_max = location
##                
##        numbers[fill_slot], numbers[pos_of_max] = numbers[pos_of_max], numbers[fill_slot]
##        if numbers[fill_slot] != numbers[pos_of_max] and numbers[pos_of_max] != numbers[fill_slot]:
##            count += 1
##  
##    return count
##
####Test
##numbers = [0, 4, 2, 7, 5]
##print(swaps(numbers)) #2
##
##numbers = [5, 2, 1, 8, 0, 3, 7]
##print(swaps(numbers)) #4
## 
##numbers = [0, 1, 2, 3, 4, 5]
##print(swaps(numbers)) #0
##
##numbers = [5]
##print(swaps(numbers)) #0

##Ex 12

##def check_count(student_id, students):
####    for index in range(1, len(students)):
####        current_value = students[index]
####        position = index - 1
####        while position >= 0 and students[position] > current_value:
####            students[position + 1] = students[position]
####            position -= 1
####        students[position + 1] = current_value
##    students.sort()
##    max_index = len(students) - 1
##    min_index = 0
##    count = 0
##    while (min_index <= max_index):
##        count += 1
##        mid_point = (min_index + max_index) // 2
##        element = students[mid_point]
##        if student_id == element[0]:
##            return count
##        elif student_id < element[0]:
##            max_index = mid_point - 1
##        else:
##            min_index = mid_point + 1
##
##
##    return -1

    

##Test
##s1 = (7, "Smith")
##s2 = (5, "Brown")
##s3 = (4, "Chan")
##s4 = (2, "Kim")
##s5 = (0, "Lin")
##students = [s1, s2, s3, s4, s5]
##print(check_count(0, students)) #2
##
##s1 = (7, "Smith")
##s2 = (5, "Brown")
##s3 = (4, "Chan")
##s4 = (2, "Kim")
##s5 = (0, "Lin")
##students = [s1, s2, s3, s4, s5]
##print(check_count(7, students)) #3
##
##s1 = (7, "Smith")
##s2 = (5, "Brown")
##s3 = (4, "Chan")
##s4 = (2, "Kim")
##s5 = (0, "Lin")
##students = [s1, s2, s3, s4, s5]
##print(check_count(8, students)) #-1
##
##s1 = (70, "Anderson")
##s2 = (60, "Huang")
##s3 = (50, "Ng")
##s4 = (40, "Roberts")
##s5 = (30, "Smith")
##s6 = (20, "Smith")
##s7 = (10, "Zhou")
##students = [s1, s2, s3, s4, s5, s6, s7]
##print(check_count(50, students)) #3
##
##students = []
##print(check_count(1, students)) # -1

