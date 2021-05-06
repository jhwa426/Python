""" Assignment 3 function 5"""

def main():
    print_header(5, "get_sequencial_nums_sums()")
    list1 = [3, 3, 2, 3, 4, 3]
    print(list1, end = " => ")
    print(get_sequencial_nums_sums(list1)) #[6, 5, 7]
    print()

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list1, end = " => ")
    print(get_sequencial_nums_sums(list1))
    print()

    list1 = [3]
    print(list1, end = " => ")
    print(get_sequencial_nums_sums(list1))

#--------------------------------------------------
# 5555555555555555555555555555555555555555555555555
# Returns a list with the totals of each pair of
# of elements of the parameter list.
#--------------------------------------------------
def get_sequencial_nums_sums(list1):
    result_list = []
    my_list = list1[::2]
    index = 1
    count = 0

    while count < len(list1):  
        if len(list1) % 2 == 0:
            result_list.append(list1[count] + list1[index])
        elif len(list1) == index and len(list1) % 2 != 0:
            result_list.append(list1[-1])
        else:
            result_list.append(list1[count] + list1[index])
        
            
        index = index + 2
        count = count + 2
    return result_list   



#--------------------------------------------------
# Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()
