"""
Lab 7:

"""

def main():
    number_repeated = get_number_of_unique_repeats("Lab07Q05_1.txt") #4
    print(number_repeated)
    print()

    print(get_number_of_unique_repeats("Lab07Q05_2.txt")) #4
    print()

    print(get_number_of_unique_repeats("Lab07Q05_3.txt"))


##def get_number_of_unique_repeats(filename):
##    input_file = open(filename, "r")
##    contents = input_file.read()
##    input_file.close()
##    word_list = contents.split()
##    check_list = [] #['Penny', 'Charla', 'Palmer', 'Joya', 'Rochelle', 'Tarra', 'Myrtle', 'Conroy', 'Gabriel', 'Husein']
##    count = 0
##
##    for word in range(len(word_list)):
##        if word_list[word] not in check_list:
##            check_list.append(word_list[word])
##
##    for check in range(len(check_list)):
##        if check_list[check] in word_list and word_list.count(check_list[check]) >= 2:
##            count = count + 1
##                                                            
##            
##    return count

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
    
main()








