"""
Lab 6:

"""

def main():
    word_list = ['fish', 'barrel', 'like', 'shooting', 'sand', 'bank']
    print(word_list)
    remove_short_words(word_list)
    print(word_list)
    print()

    word_list = ['cat', 'the', 'the', 'bag', 'let', 'out', 'can']
    print(word_list)
    remove_short_words(word_list)
    print(word_list)
    print()

    word_list = ['it', 'the', 'the', 'the', 'out', 'big', 'if']
    print(word_list)
    remove_short_words(word_list)
    print(word_list)

##def get_shortest_length(word_list):
##    #Copy the get_shortest_length(word_list) from Program 5
##    shortest_length_so_far = len(word_list[0])
##
##    for word in word_list:
##        if len(word) <= shortest_length_so_far:
##            shortest_length_so_far = len(word)
##
##
##    return shortest_length_so_far

##def remove_short_words(word_list):
##    shortest_length = get_shortest_length(word_list)
##    index = len(word_list)-1 #3
##    
##    while index > -1:
##        if len(word_list[index]) == shortest_length:
##            word_list.pop(index)
##
##        index = index - 1
##        
##    return word_list
        
##Method 2
##def remove_short_words(word_list):
##    
##    for word in range(len(word_list)-1,-1,-1):
##        if len(word_list[word]) == get_shortest_length(word_list):
##            word_list.pop(word)
##
##    return word_list



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

##Q6_revision
def remove_short_words(word_list):
    shortest_lengt = get_shortest_length(word_list)

    for index in range(len(word_list)-1,-1,-1):
        if len(word_list[index]) == (shortest_lengt):
            word_list.pop(index)

    return word_list



main()
