""" Use this file to develop and test your Assignment 4 function 2"""

#--------------------------------------------------
# 2222222222222222222222222222222222222222222222222
# print_rows()
#--------------------------------------------------
def print_rows(row_dict):
    collection_keys = row_dict.keys()
    keys_list = list(collection_keys)
    keys_list.sort()

    for key in keys_list:
        value = row_dict[key]
        smallest = min(value)
        biggest = max(value)
        if value[0] > 0 and value[1] > 0:
            print("*" * smallest + str(key.upper() * biggest) + "*" * smallest,end = "")
            

def main():
    print_header(2, "print_rows()")
    print_rows({'a': (4, 3), 'c': (5, 0), 'b': (-2, 5)})
    print()

    print_rows({'d': (12, -3), 'c': (1, 2), 'b': (3, -4), 'f': (11, 6)})
    print()

    print_rows({'d': (6, -3), 'z': (1, 3), 'b': (3, 0), 's': (4, 6)})

#--------------------------------------------------
#Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()

