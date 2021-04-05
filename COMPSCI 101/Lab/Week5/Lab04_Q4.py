"""
Lab 4:
"""

def main():
    result = remove_spaces("1 5 67 88")
    print(result)

    print(remove_spaces("programming  is such fun,  fun,   fun"))
    print()

    print(remove_spaces("1 5 67 88    "))
    print()

    print(remove_spaces("    1 5    67 88"))


def remove_spaces(phrase):
    new_str = ""
    index = 0
    space = " "

    while index < len(phrase):
        if phrase[index] != space:
            new_str += phrase[index]

        index += 1

    return new_str

##def remove_spaces(phrase):
##    new_string = ""
##    index = 0
##    space = ""
##    
##    while index < len(phrase):
##        if phrase[index] != " ":
##            new_string = new_string + phrase[index]
##            
##        else:
##            space = space + phrase[index]
##
##        index = index + 1
##
##    return new_string

##def remove_spaces(phrase):
##    result = phrase.replace(" ", "")
##    return result

main()



#### practice
##def remove_comma(phrase):
##    empty = ""
##    index = 0
##    rubbish = ""
##
##    while index < len(phrase):
##        if (phrase[index] != ","):
##            empty = empty + phrase[index]
##
##        else:
##            rubbish = rubbish + phrase[index]
##
##        index = index + 1
##
##    return empty
##
##
##def main():
##    result = remove_comma("1 5 67 88")
##    print(result)
##
##    print(remove_comma("programming  is such fun,  fun,   fun"))
##    print()
##
##    print(remove_comma("1 5 67 88    "))
##    print()
##
##    print(remove_comma("    1 5    67 88"))
##
##
##main()
