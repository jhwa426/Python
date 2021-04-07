"""
Lab 6:

"""

def main():
    numbers1 = [1, 4, 6, 2, 9, 8]
    numbers2 = [4, 0, 8, 1, 9, 7, 1]
    print(numbers1)
    print(numbers2)
    print(have_same_start_total(numbers1, numbers2))
    print()

    numbers1 = [1, 4, 5, 2, 9, 8]
    numbers2 = [4, 0, 8, 1, 9, 7, 1]
    print(numbers1)
    print(numbers2)
    print(have_same_start_total(numbers1, numbers2))
    print()

    numbers1 = [1, 4, 5]
    numbers2 = [4, 0, 8, 1, 9, 7, 1]
    print(numbers1)
    print(numbers2)
    print(have_same_start_total(numbers1, numbers2))

    print(have_same_start_total([1, 4, 0, 0, 6], [0, 0, 5, 0]))
    print(type(have_same_start_total([1, 4, 0, 0, 6], [0, 0, 5, 0])))
    print(have_same_start_total([1, 4, 0, 0, 6], [0, 0, 5, 0]))
    print(type(have_same_start_total([1, 4, 0, 0, 6], [0, 0, 5, 0])))
    print(have_same_start_total([1, 0, 2, 0, 5], [1, 0, 1, 1, 1, 1, 5]))
    print(have_same_start_total([1, 0, 2, 0, 5], [1, 0, 1, 1, 1, 1, 5]))


##def have_same_start_total(list1, list2):
##    new_list1 =[]
##    new_list2 =[]
##    
##    for count in range(len(list1)):
##        if count < 4 and len(list1) >= 4:
##            new_list1.append(list1[count])
##
##    for count2 in range(len(list2)):
##        if count2 < 4 and len(list2) >= 4:
##            new_list2.append(list2[count2])
##
##
##    if sum(new_list1) == sum(new_list2) and sum(new_list1)>0 and sum(new_list2)>0 :
##        return True
##    else:
##        return False

##Q1_revision          
def have_same_start_total(list1, list2):
    count = 0
    if len(list1) < 4 or len(list2) < 4:
        return False
    else:    
        index_list1 = sum(list1[:4])
        index_list2 = sum(list2[:4])

        if index_list1 == index_list2:
            return True
        else:
            return False


main()

	






