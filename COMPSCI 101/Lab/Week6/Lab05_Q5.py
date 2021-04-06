"""
Lab 5:
"""

def main():
    print_longest_word(['fish', 'barrel', 'like', 'shooting', 'in', 'a'])
    print_longest_word(['cat', 'the', 'the', 'bag', 'let', 'out', 'of'])
    print_longest_word(['the', 'the', 'bag', 'let', 'out', 'of', 'cat'])

##def print_longest_word(word_list):
##    longest_word = []
##    
##    for word in word_list:
##        if len(word) > len(longest_word):
##            longest_word = word
##        elif len(word) == len(longest_word) and len(word) > 1:
##            longest_word = word
##
##
##    print(longest_word)
            

##Q5_revision
def print_longest_word(word_list):
    update_str = ""

    for index in range(len(word_list)):
        word = word_list[index]
        if len(word) >= len(update_str):
            update_str = word
            
    print(update_str)
            

    
main()








