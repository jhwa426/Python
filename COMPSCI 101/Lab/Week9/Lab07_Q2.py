"""
Lab 7:

"""

def main():
    words = ('carry', 'stick', 'big', 'a', 'and', 'speak', 'softly')
    numbers = (23, 40, 19, 22, 42, 41, 63)
    print(get_two_words(numbers, words))
    print()

    words = ('whole', 'kit', 'the', 'and', 'caboodle')
    numbers = (76, 81, 62, 83, 87)
    print(get_two_words(numbers, words))
    print()

    words = ('mouth', 'in', 'look', 'do', 'gift', 'a', 'the', 'horse', 'not')
    numbers = (81, 24, 11, 63, 70, 60, 26, 73, 14)
    print(get_two_words(numbers, words))

##def get_two_words(numbers_tuple, words_tuple):
##    convert_list = list(numbers_tuple)
##    convert_list.sort()
##    
##    min_number = convert_list[0]#19
##    find_min_number = list(numbers_tuple).index(min_number) #2
##    
##    sec_min_number = convert_list[1]
##    find_sec_min_number = list(numbers_tuple).index(sec_min_number) #3
##    
##    result = []
##    result = words_tuple[find_min_number],words_tuple[find_sec_min_number]
##    return result
    
##Q2_revision
def get_two_words(numbers_tuple, words_tuple):
    convert_list = list(numbers_tuple)
    convert_list.sort()

    min_number = convert_list[0]
    pos_min_number = list(numbers_tuple).index(min_number)
    
    sec_min_number = convert_list[1]
    pos_sec_min_number = list(numbers_tuple).index(sec_min_number)

    return words_tuple[pos_min_number], words_tuple[pos_sec_min_number]

main()








