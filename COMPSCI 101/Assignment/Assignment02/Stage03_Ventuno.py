"""
Stage 3 functions of Assignment 2
"""
import random

def main():
    selection = 1
    while selection > 0:
        selection = get_choice()
        if selection == 1:
            test_display_current_scores()
        elif selection == 2:
            test_game_is_over()
        elif selection == 3:
            test_get_winner_name()
        elif selection == 4:
            test_display_game_result()
        elif selection == 5:
            test_display_statistics()
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
# display_line_of_symbols() FUNCTION FROM STAGE 1
# Copy this function from your Stage 1 functions
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
def display_line_of_symbols(indent, symbol, how_many):
    result = print(indent + (symbol * how_many))

    return result
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
# FIVE STAGE 3 FUNCTIONS
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
def display_current_scores(indent, score_player, score_computer,
                           player_stays, computer_stays, player_name):
    print()
    display_line_of_symbols(indent, "-", 37)
    display_line_of_symbols(indent, "-", 37)

    if score_player > score_computer:
        print(indent + player_name + "'s score: " + str(score_player) + " - "
              + player_name + " stays")
        print(indent + "Computer's score: " + str(score_computer))

    elif score_player == score_computer:
        print(indent + player_name + "'s score: " + str(score_player) + " - "
              + player_name + " stays")
        print(indent + "Computer's score: " + str(score_computer) + " - Computer stays")

    else:
        print(indent + player_name + "'s score: " + str(score_player))
        print(indent + "Computer's score: " + str(score_computer) + " - Computer stays")        

    display_line_of_symbols(indent, "-", 37)
    display_line_of_symbols(indent, "-", 37)
    print()

def game_is_over(score_player, score_computer,
                 player_stays, computer_stays):
    
    if (score_player >= score_computer and score_player <= score_computer) or score_player > 21:
        return True
    else:
        return False

def get_winner_name(score_player, score_computer, player_name):
    if score_player == score_computer:
        return "draw"
    elif score_player > 21 or (score_computer > score_player and score_computer <= 21):
        return "Computer"
    elif score_computer > 21 or (score_player > score_computer and score_player <= 21):
        return player_name

def display_game_result(indent, score_player, score_computer,
                        game_winner, player_name):
    print()
    display_line_of_symbols(indent, "+", 25)
    display_line_of_symbols(indent, "+", 25)

    print(indent + player_name + "'s score: " + str(score_player))
    print(indent + "Computer's score: " + str(score_computer))

    if score_player > score_computer or game_winner == player_name:
        print(indent + player_name + " has won.  Well done!")
    elif score_computer > score_player or game_winner == "Computer":
        print(indent + "Computer has won.")
    elif score_player == score_computer or game_winner == "draw":
        print(indent + "Result is a draw.")

    display_line_of_symbols(indent, "+", 25)
    display_line_of_symbols(indent, "+", 25)


def display_statistics(player_name, total_number_of_games, games_won_by_user, games_won_by_computer):

    print()
    print("*" * 32)
    print("*" * 32)

    print("  Number of games played: " + str(total_number_of_games))
    print("  Games won by " + player_name + ": " + str(games_won_by_user))
    print("  Games won by Computer: " + str(games_won_by_computer))
    draw = total_number_of_games - (games_won_by_user + games_won_by_computer)
    print("  Games resulting in a draw: "+ str(draw))
    print()
    
    result1 = games_won_by_user - games_won_by_computer
    result2 = games_won_by_computer - games_won_by_user
    
    if games_won_by_user > games_won_by_computer:
        print("*** " + player_name + " is winning by " + str(result1) + " *** ")
    elif games_won_by_user < games_won_by_computer:
        print("*** Computer is winning by " + str(result2) + " *** ")
    else:
        print("*** Final result is a draw ***")

    print("*" * 32)
    print("*" * 32)
    
#-----------------------------
# get_choice()
#-----------------------------
def get_choice():
    print()
    print(" ", "." * 35)
    print("  1. display_current_scores()")
    print("  2. game_is_over()")
    print("  3. get_winner_name()")
    print("  4. display_game_result()")
    print("  5. display_statistics()")
    print("  0. Exit")
    selection = int(input("     Enter selection: "))
    print(" ", "." * 35)
    print()
    return selection
#-----------------------------
# Test display_current_scores()
#-----------------------------
def test_display_current_scores():
    print("Expected output:")
    print()
    print("    -------------------------------------")
    print("    -------------------------------------")
    print("    Max's score: 20 - Max stays")
    print("    Computer's score: 18")
    print("    -------------------------------------")
    print("    -------------------------------------")
    print("\n")
    print("  -------------------------------------")
    print("  -------------------------------------")
    print("  Milly's score: 19 - Milly stays")
    print("  Computer's score: 19 - Computer stays")
    print("  -------------------------------------")
    print("  -------------------------------------")
    print()
    print("Your output:")
    display_current_scores("    ", 20, 18, True, False, "Max")
    display_current_scores("  ", 19, 19, True, True, "Milly")
#-----------------------------
# Test game_is_over()
#-----------------------------
def test_game_is_over():
    print("Expected output:")
    print("False")
    print("True")
    print("True")
    print("False")
    print()
    print("Your output:")
    print(game_is_over(17, 20, False, True))
    print(game_is_over(22, 20, False, True))
    print(game_is_over(20, 20, True, True))
    print(game_is_over(20, 19, False, False))
#-----------------------------
# Test get_winner_name()
#-----------------------------
def test_get_winner_name():
    print("Expected output:")
    print("Asad")
    print("draw")
    print("Computer")
    print("Lei")
    print()
    print("Your output:")
    print(get_winner_name(20, 22, "Asad"))
    print(get_winner_name(20, 20, "Asad"))
    print(get_winner_name(18, 21, "Jim"))
    print(get_winner_name(20, 22, "Lei"))
#-----------------------------
# Test display_game_result()
#-----------------------------
def test_display_game_result():
    print("Expected output:")
    print()
    print("  +++++++++++++++++++++++++")
    print("  +++++++++++++++++++++++++")
    print("  Guy's score: 18")
    print("  Computer's score: 24")
    print("  Guy has won.  Well done!")
    print("  +++++++++++++++++++++++++")
    print("  +++++++++++++++++++++++++")
    print()
    print(" +++++++++++++++++++++++++")
    print(" +++++++++++++++++++++++++")
    print(" Guy's score: 20")
    print(" Computer's score: 20")
    print(" Result is a draw.")
    print(" +++++++++++++++++++++++++")
    print(" +++++++++++++++++++++++++")
    print()
    print("Your output:")
    display_game_result("  ", 18, 24, "Guy", "Guy")
    display_game_result(" ", 20, 20, "draw", "Guy")
#-----------------------------
# Test display_statistics()
#-----------------------------
def test_display_statistics():
    print("Expected output:")
    print()
    print("********************************")
    print("********************************")
    print("  Number of games played: 7")
    print("  Games won by Thor: 3")
    print("  Games won by Computer: 2")
    print("  Games resulting in a draw: 2")
    print()
    print("*** Thor is winning by 1 ***")
    print("********************************")
    print("********************************")
    print()
    print("********************************")
    print("********************************")
    print("  Number of games played: 16")
    print("  Games won by Eddy: 5")
    print("  Games won by Computer: 5")
    print("  Games resulting in a draw: 6")
    print()
    print("*** Final result is a draw ***")
    print("********************************")
    print("********************************")
    print()
    print("Your output:")
    display_statistics("Thor", 7, 3, 2)
    display_statistics("Eddy", 16, 5, 5)


main()
