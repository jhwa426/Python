"""
Lab 7:

"""

def main():
    a_tuple = (-3, 6, 9, 4, 5) #-3, 4, 5, 6, 9
    print(get_small_middle_large(a_tuple))
    print()

    print(get_small_middle_large((2,)))
    print()

    print(get_small_middle_large((2, -5)))
    print()

    print(get_small_middle_large((6, 7, 0, 3, 2, 8))) #0,2,3,6,7,8 # 0, 3, 8 #(2,3,6,7)

##def get_small_middle_large(a_tuple):
##    result = []
##    
##    list_to_tuple = list(a_tuple)
##    list_to_tuple.sort()
##    min_tuple = min(list_to_tuple) 
##    position_min = list_to_tuple.index(min_tuple) 
##    max_tuple = max(list_to_tuple) 
##    position_max = list_to_tuple.index(max_tuple) 
##    mid_tuple = len(list_to_tuple[position_min+1:position_max]) // 2 
##
##
##    if len(a_tuple) > 2:
##        result.append(list_to_tuple[position_min])
##        result.append(list_to_tuple[mid_tuple+1])
##        result.append(list_to_tuple[position_max])
##    elif len(a_tuple) == 2:
##        result.append(list_to_tuple[position_min])
##        result.append(list_to_tuple[position_max])
##    else:
##        result.append(list_to_tuple[position_min])
##        
##    return tuple(result)

##Q1_revision
def get_small_middle_large(a_tuple):
    
    if len(a_tuple) < 2:
        return a_tuple
    elif len(a_tuple) == 2:
        return tuple(sorted(a_tuple))
    else:
        a_tuple = tuple(sorted(a_tuple))
        index = (len(a_tuple) // 2)

        the_smallest = a_tuple[0]
        middle = a_tuple[index]
        the_largest = a_tuple[-1]

        return the_smallest, middle, the_largest
    
main()








