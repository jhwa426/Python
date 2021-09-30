"""
Lab 6:

"""


def main():
    numbers_list = [31, 636, 2042, 40, 447]
    print(numbers_list)
    increase_decrease(numbers_list)
    print(numbers_list)
    print()

    numbers_list = [11, 4559, 241, 99, 100]
    print(numbers_list)
    increase_decrease(numbers_list)
    print(numbers_list)
    print()

    numbers_list = [101, 45594, 1241, 9, 92]
    print(numbers_list)
    increase_decrease(numbers_list)
    print(numbers_list)


##def increase_decrease(numbers_list):
##    new_list = []
##    for each in range(len(numbers_list)):
##        if numbers_list[each] < 100:
##            numbers_list[each] = numbers_list[each] * 10
##            new_list.append(numbers_list[each])
##        elif numbers_list[each] >= 100:
##            numbers_list[each] = numbers_list[each] // 10
##            new_list.append(numbers_list[each])
##
##    return new_list

##Q4_revision
def increase_decrease(numbers_list):
    result_list = []

    for index in range(len(numbers_list)):
        if numbers_list[index] < 100:
            numbers_list[index] *= 10
            result_list.append(numbers_list[index])
        else:
            numbers_list[index] //= 10
            result_list.append(numbers_list[index])
            
    return result_list


main()


