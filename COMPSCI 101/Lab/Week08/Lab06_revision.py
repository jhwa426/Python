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



##Test
##numbers1 = [1, 4, 6, 2, 9, 8]
##numbers2 = [4, 0, 8, 1, 9, 7, 1]
##print(have_same_start_total(numbers1, numbers2))
##
##numbers1 = [1, 4, 5, 2, 9, 8]
##numbers2 = [4, 0, 8, 1, 9, 7, 1]
##print(have_same_start_total(numbers1, numbers2))


##Q2_revision
def swap_elements(numbers_list, number1, number2):
    if number1 in numbers_list and number2 in numbers_list:
        num_pos1 = numbers_list.index(number1)
        num_pos2 = numbers_list.index(number2)
        numbers_list[num_pos1], numbers_list[num_pos2] = numbers_list[num_pos2], numbers_list[num_pos1]
    else:
        return numbers_list




####Test
##numbers = [9, 0, 2, 5, 6, 4, 5]
##print(numbers) #[9, 0, 2, 5, 6, 4, 5]
##swap_elements(numbers, 2, 4)
##print(numbers) #[9, 0, 4, 5, 6, 2, 5]
##print()
##
##numbers = [9, 0, 9, 5, 6, 6, 5]
##print(numbers) #[9, 0, 9, 5, 6, 6, 5]
##swap_elements(numbers, 9, 6)
##print(numbers) #[6, 0, 9, 5, 9, 6, 5]
##print()
##
##numbers = [9, 8, 11, 5, 6, 7, 5]
##print(numbers)
##swap_elements(numbers, 6, 4)
##print(numbers)

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



##numbers_list = [31, 636, 2042, 40, 447]
##print(numbers_list)
##numbers_list2 = get_sorted_increased_decreased(numbers_list)
##print(numbers_list2)
##print()
##print(get_sorted_increased_decreased([11, 4559, 241, 12, 924]))




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


####Test
##numbers_list = [31, 636, 2042, 40, 447]
##print(numbers_list)
##increase_decrease(numbers_list)
##print(numbers_list)
##print()
##
##numbers_list = [11, 4559, 241, 99, 100]
##increase_decrease(numbers_list)
##print(numbers_list)


##Q5_revision
def get_shortest_length(word_list):
    shortest_length = len(word_list[0])

    for word in word_list:
        if len(word) <= shortest_length:
            shortest_length = len(word)


    if len(word_list) == 0:
        return 0
    else:
        return shortest_length





####Test
##word_list = ['fish', 'barrel', 'like', 'shooting', 'sand', 'bank']
##shortest_length = get_shortest_length(word_list)
##print(shortest_length)#4
##print()
##
##word_list = ['cat', 'the', 'a', 'bag', 'let', 'out', 'can']
##print(get_shortest_length(word_list))#1
##print()
##
##word_list = ['it', 'the', 'the', 'the', 'out', 'big', 'I']
##print(get_shortest_length(word_list))#1






##Q6_revision
def remove_short_words(word_list):
    shortest_lengt = get_shortest_length(word_list)

    for index in range(len(word_list)-1,-1,-1):
        if len(word_list[index]) == (shortest_lengt):
            word_list.pop(index)

    return word_list

    


####Test
##word_list = ['water', 'out', 'of', 'fish']
##remove_short_words(word_list)
##print(word_list) # ['water', 'out', 'fish']


##Q7_revision
def insert_word(word_list, word_to_insert, before_this_word):
    if before_this_word in word_list and word_to_insert not in word_list:
        find_pos = word_list.index(before_this_word)
        word_list.insert(find_pos, word_to_insert)

    return word_list








##Test
word_list = ['fish', 'barrel', 'like', 'shooting', 'sand', 'bank']
insert_word(word_list, "water", "bank")
print(word_list)
print()

word_list = ['cat', 'the', 'bag', 'let', 'out', 'can']
insert_word(word_list, "dog", "let")
print(word_list)




