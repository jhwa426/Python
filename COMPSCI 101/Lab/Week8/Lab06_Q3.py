"""
Lab 6:

"""

def main():
    numbers_list = [31, 636, 2042, 40, 447]
    print(numbers_list)
    numbers_list2 = get_sorted_increased_decreased(numbers_list)
    print(numbers_list2)
    print()

    numbers_list = [11, 4559, 241, 12, 924]
    print(numbers_list)
    print(get_sorted_increased_decreased(numbers_list))
    print()

    numbers_list = [101, 45594, 1241, 9, 92]
    print(numbers_list)
    print(get_sorted_increased_decreased(numbers_list))


##def get_sorted_increased_decreased(numbers_list):
##    new_list = []
##    for each in range(len(numbers_list)):
##        if numbers_list[each] < 100:
##            numbers_list[each] = numbers_list[each] * 10
##            new_list.append(numbers_list[each])
##        elif numbers_list[each] >= 100:
##            numbers_list[each] = numbers_list[each] // 10
##            new_list.append(numbers_list[each])
##            
##    new_list.sort()
##    new_list.reverse()
##    
##    return new_list





##Q3_revision
def get_sorted_increased_decreased(numbers_list):
    new_list = []

    for number in numbers_list:
        if number < 100:
            number *= 10
            new_list.append(number)
        else:
            number //= 10
            new_list.append(number)
            
    return sorted(new_list, reverse=True)


main()

