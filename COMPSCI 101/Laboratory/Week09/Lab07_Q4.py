"""
Lab 7:

"""

def main():
    number_same = get_length_same("Lab07Q04_1.txt", "Lab07Q04_2.txt")
    print(number_same)
    print()

    print(get_length_same("Lab07Q04_3.txt", "Lab07Q04_4.txt"))
    print()

    print(get_length_same("Lab07Q04_5.txt", "Lab07Q04_6.txt")) #13
    
##def get_length_same(filename1, filename2):
##    input_file1 = open(filename1, "r")
##    input_file2 = open(filename2, "r")
##    contents1 = input_file1.read()
##    contents2 = input_file2.read()
##    input_file1.close()
##    input_file2.close()
##    
##    number_list1 = contents1.split()
##    number_list2 = contents2.split()
##    
##    shortest_len = min(len(number_list1),len(number_list2)) #11
##    index = 0
##    length_count = 0
##
##    while index < shortest_len:
##        if len(number_list1[index]) == len(number_list2[index]):
##            length_count = length_count + len(number_list1[index])
##        else:
##            return length_count
##
##        index = index + 1
##                       
##    return length_count

##def get_length_same(filename1, filename2):
##    input_file1 = open(filename1, "r")
##    input_file2 = open(filename2, "r")
##    contents1 = input_file1.read()
##    contents2 = input_file2.read()
##
##    input_file1.close()
##    input_file2.close()
##
##    shortest_len = min(len(contents1),len(contents2)) #19
##
##    length_count = 0
##
##    for word in range(shortest_len):
##        if contents1[word] == contents2[word]:
##            length_count = length_count + 1
##        else:
##            return length_count
##
##    return length_count

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

main()








