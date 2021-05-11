"""Assignment 3 function 8"""

def main():
    print_header(8, "get_dice_score()")
    print("1:", get_dice_score([5, 3, 2, 5, 4, 5, 6, 4, 3]))
    print("2:", get_dice_score([3, 4, 1, 5, 3, 1, 4, 6]))
    print("3:", get_dice_score([5, 3, 2, 2, 6, 4, 5, 1, 4]))
    print("4:", get_dice_score([2, 1, 1, 1, 2, 3, 3, 1, 3, 2]))
    print("5:", get_dice_score([3, 4, 1, 5, 2, 1, 5, 1, 2, 3, 4, 6]))
    print("6:", get_dice_score([]))
#--------------------------------------------------
# 8888888888888888888888888888888888888888888888888
# Score a hand of random dice throws
#--------------------------------------------------
##def get_dice_score(list_of_dice):
##    index = 0
##    count = 0
##    while index < len(list_of_dice):
##        if
        
def get_dice_score(list_of_dice):
    dice = [1,2,3,4,5,6]
    empty_list = []
    score = 0
    
    if 1 not in list_of_dice:
        return score
    
    for number in dice:
        empty_list.append(list_of_dice.count(number))
        print(empty_list)
        
    for check in range(len(empty_list)):
        for each in range(check+1, len(empty_list)):
            if empty_list[each] > empty_list[check]:
                empty_list[each] = empty_list[check]
                
    for result in range(len(empty_list)):
        score = score + empty_list[result] * (result + 1)
        
    return score

#--------------------------------------------------
# Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()
