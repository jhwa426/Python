"""
Lab 6:

"""

def main():
    word_list = ['fish', 'barrel', 'like', 'shooting', 'sand', 'bank']
    print(word_list)
    shortest_length = get_shortest_length(word_list)
    print(shortest_length)
    print()

    word_list = ['cat', 'the', 'a', 'bag', 'let', 'out', 'can']
    print(word_list)
    print(get_shortest_length(word_list))
    print()

    word_list = ['it', 'the', 'the', 'the', 'out', 'big', 'I']
    print(word_list)
    print(get_shortest_length(word_list))

##def get_shortest_length(word_list):
##    shortest_length_so_far = len(word_list[0])
##
##    for word in word_list:
##        if len(word) <= shortest_length_so_far:
##            shortest_length_so_far = len(word)
##
##
##    return shortest_length_so_far

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
main()








