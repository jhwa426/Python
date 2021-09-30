"""
Stage 4 function of Assignment 2
"""

import random

#-----------------------------
# Test get_computer_selection()
#-----------------------------
def main():
    selection = get_computer_selection(19, 18, True)
    display_selection(1, selection, 19, 18, True)

    selection = get_computer_selection(20, 20, True)
    display_selection(2, selection, 20, 20, True)

    selection = get_computer_selection(18, 18, True)
    display_selection(3, selection, 18, 18, True)

    selection = get_computer_selection(18, 18, False)
    display_selection(4, selection, 17, 17, False)
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
# ONE STAGE 4 FUNCTION
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
def get_computer_selection(score_player, score_computer, player_stays):
    roll = 1
    stay = 2
    ventuno = 21

    if score_player < score_computer and score_computer <= ventuno:
        return roll
    
    elif score_player > score_computer:
        if score_computer == True:
            return stay
        else:
            return roll
        
    elif score_player == score_computer:
        if score_player == ventuno or score_computer == ventuno:
            return stay
        else:
            return roll
    





#-----------------------------
# display_selection()
# display information about
# the computer selection
#-----------------------------
def display_selection(output_num, selection, score1, score2, player_stayed):
    action = "stay"
    if selection == 1:
        action = "roll"
    number = str(output_num) + ": "
    if player_stayed == True:
        print(number + " Player has stayed at " + str(score1) + ", and the computer has " + str(score2))
    else:
        print(number + " Player has " + str(score1) + " and the computer has " + str(score2))
    print("    Computer has decided to " + action + "\n")


main()
