""" Assignment 3 function 6"""

def main():
    print_header(6, "remove_triplets()")
    a_list = [6, 6, 6, 7, 6, 6, 6, 3, 3, 3, 8, 8, 8, 3] #[7, 3]
    print(a_list, end = " => ")
    remove_triplets(a_list)
    print(a_list)
    print()

    a_list = [6, 6, 6, 5, 7, 5, 5, 5] #[5, 7]
    print(a_list, end = " => ")
    remove_triplets(a_list)
    print(a_list)
    print()

    a_list = [6, 6, 6, 7, 6, 6, 6, 6, 6] #[7, 6, 6]
    print(a_list, end = " => ")
    remove_triplets(a_list)
    print(a_list)
    print()

    a_list = [6, 6, 6]
    print(a_list, end = " => ")
    remove_triplets(a_list)
    print(a_list)
    print()

    a_list = [1, 1, 1, 1]
    print(a_list, end = " => ")
    remove_triplets(a_list)
    print(a_list)
    print()

    a_list = [1, 1, 2, 1, 2, 1] #[1, 1, 2, 1, 2, 1]
    print(a_list, end = " => ")
    remove_triplets(a_list) 
    print(a_list)
    print()
#--------------------------------------------------
# 6666666666666666666666666666666666666666666666666
# Remove triplets made up of three sequential
# identical elements
#--------------------------------------------------

def remove_triplets(a_list):
    index = len(a_list) - 1
    if len(a_list) < 3:
        return
    
    while index > 1:
        if a_list[index] == a_list[index-1] and a_list[index] == a_list[index-2]:
            a_list.pop(index)
            a_list.pop(index-1)
            a_list.pop(index-2)
            index = index - 3
        else:
            index = index - 1

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
