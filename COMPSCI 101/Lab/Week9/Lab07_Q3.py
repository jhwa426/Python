"""
Lab 7:

"""

def main():
    filename = "Lab07Q03_1.txt"
    print(get_biggest_difference(filename)) #8
    print()

    filename = "Lab07Q03_2.txt"
    print(get_biggest_difference(filename)) #15


def get_biggest_difference(filename):
    input_file = open(filename, "r")
    contents = input_file.read()
    input_file.close()
    
    number_list = contents.split()
    new_list = []
    for number in range(len(number_list)):
        new_list.append(int(number_list[number]))

    min_number = min(new_list) #11, 1
    max_number = max(new_list) #19, 16

    result = abs(int(max_number) - int(min_number))
    return result
  
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


main()








