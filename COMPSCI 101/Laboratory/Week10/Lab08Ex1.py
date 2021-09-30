"""
Lab 8 Ex 1
Author:
Date: May, 2020
This program prints a baby boy/girl name 
"""
def main():
    baby_boy_names_dictionary = {'A': 'Alex', 'B': 'Benjamin', 'C': 'Connor', 'D': 'Daniel', 'E': 'Ethan', 'F': 'Finn', 'G': 'George', 'H': 'Hunter', 'I': 'Isaac', 'J': 'Joshua', 'K': 'Kingston', 'L': 'Liam', 'M': 'Max', 'N': 'Noah', 'O': 'Oliver', 'P': 'Phoenix', 'Q': 'Quinn', 'R': 'Riley', 'S': 'Samuel', 'T': 'Thomas', 'U': 'Ute', 'V': 'Victor', 'W': 'William', 'X': 'Xavier', 'Y': 'Yukio', 'Z': 'Zachary'}
    baby_girl_names_dictionary = {'A': 'Abby', 'B': 'Bella', 'C': 'Charlotte', 'D': 'Daisy', 'E': 'Ella', 'F': 'Faith', 'G': 'Grace', 'H': 'Hannah', 'I': 'Isabella', 'J': 'Jade', 'K': 'Kate', 'L': 'Lily', 'M': 'Maddison', 'N': 'Natalie', 'O': 'Olivia', 'P': 'Phoebe', 'Q': 'Q', 'R': 'Rebecca', 'S': 'Samantha', 'T': 'Tayla', 'U': 'Ute', 'V': 'Violet', 'W': 'Willa', 'X': 'Xena', 'Y': 'Yuki', 'Z': 'Zoe'}
    letter = get_letter_from_user()
    print_baby_name(letter, baby_boy_names_dictionary)
    print_baby_name(letter, baby_girl_names_dictionary)

##def get_letter_from_user():
##    enter_user = input("Enter a letter: ")
##    change_upper = enter_user.upper()
##
##    return change_upper
##
##def print_baby_name(letter, baby_names_dictionary):
##    for key in baby_names_dictionary:
##        name = baby_names_dictionary[key]
##        if letter == key:
##            print("Baby name :", name)
       
        


##Q1_revision
def get_letter_from_user():
    user_input = input("Enter a letter: ")
    return user_input.upper()
    

def print_baby_name(letter, baby_names_dictionary):
    for key in baby_names_dictionary:
        if key == letter:
            print(baby_names_dictionary[key])
            
main()


