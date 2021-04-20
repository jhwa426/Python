##Q1_revision
def get_small_middle_large(a_tuple):
    
    if len(a_tuple) < 2:
        return a_tuple
    elif len(a_tuple) == 2:
        return tuple(sorted(a_tuple))
    else:
        a_tuple = tuple(sorted(a_tuple))
        index = (len(a_tuple) // 2)

        the_smallest = a_tuple[0]
        middle = a_tuple[index]
        the_largest = a_tuple[-1]

        return the_smallest, middle, the_largest
        

####Test
##a_tuple = (-3, 6, 9, 4, 5)
##
##print(get_small_middle_large(a_tuple)) #(-3, 5, 9)
##print()
##print(get_small_middle_large((2,))) #(2,)
##print()
##print(get_small_middle_large((2, -5))) #(-5, 2)




##Q2_revision
def get_two_words(numbers_tuple, words_tuple):
    convert_list = list(numbers_tuple)
    convert_list.sort()

    min_number = convert_list[0]
    pos_min_number = list(numbers_tuple).index(min_number)
    
    sec_min_number = convert_list[1]
    pos_sec_min_number = list(numbers_tuple).index(sec_min_number)

    return words_tuple[pos_min_number], words_tuple[pos_sec_min_number]
    


####Test
##words = ('carry', 'stick', 'big', 'a', 'and', 'speak', 'softly')
##numbers = (23, 40, 19, 22, 42, 41, 63)
##print(get_two_words(numbers, words))
##print()
##
##print()
##word_list = ('whole', 'kit', 'the', 'and', 'caboodle')
##numbers = (76, 81, 62, 83, 87)
##print(get_two_words(numbers, words))

##Q3_revision
def get_biggest_difference(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split()
    input_file.close()
    
    num_list = []

    for index in range(len(contents)):
        num_list.append(int(contents[index]))
        
    max_num = max(num_list)
    min_num = min(num_list)

    return abs(max_num - min_num)





##Test
##filename = "Lab07Q03_1.txt"
##print(get_biggest_difference(filename)) #8
##print()
##filename = "Lab07Q03_2.txt"
##print(get_biggest_difference(filename)) #15


##Q4_revision
def get_length_same(filename1, filename2):
    input_file1 = open(filename1, "r")
    input_file2 = open(filename2, "r")
    contents1 = input_file1.read()
    contents2 = input_file2.read()
    
    input_file1.close()
    input_file2.close()
    
    length = min(len(contents1),len(contents2))

    count = 0
    
    for index in range(length):
        if contents1[index] == contents2[index]:
            count += 1

    return count



##Test
##number_same = get_length_same("Lab07Q04_1.txt", "Lab07Q04_2.txt")
##print(number_same)
##print()
##print(get_length_same("Lab07Q04_3.txt", "Lab07Q04_4.txt"))




##Q5_revision
def get_number_of_unique_repeats(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split()
    input_file.close()

    name_list = []
    count = 0
    for index in range(len(contents)):
        name = contents[index]
        if name not in name_list:
            name_list.append(name)

    for check_i in range(len(name_list)):
        if name_list[check_i] in name_list and contents.count(name_list[check_i]) > 1:
            count += 1

    return count
            
        





##Test
##number_repeated = get_number_of_unique_repeats("Lab07Q05_1.txt") #4
##print(number_repeated)
##print()
##print(get_number_of_unique_repeats("Lab07Q05_2.txt")) #4
##print()
##print(get_number_of_unique_repeats("Lab07Q05_3.txt")) #0

 
##Q6_revision
def write_without_blank_lines(filename_in, filename_out):
    input_file = open(filename_in, "r")
    output_file = open(filename_out, "w")
    contents = input_file.readlines()
    input_file.close()

    index = 0
    number = 1

    while index < len(contents):
        name = contents[index]
        new_line = name.strip()

        if new_line != "":
            result = "{}. {}\n".format(number, new_line)
            output_file.write(result)
            number += 1
        index +=1
            
        
    output_file.close()    

##Test
write_without_blank_lines("Lab07Q06_in.txt", "Lab07Q06_out.txt")
















