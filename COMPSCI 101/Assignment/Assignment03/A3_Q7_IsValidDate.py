""" Assignment 3 function 7"""

def main():
    print_header(7, "is_a_valid_date()")
    print("1.", is_a_valid_date("January 21")) #True
    print("2.", is_a_valid_date("Auust 3"))
    print("3.", is_a_valid_date(" June   15B "))
    print("4.", is_a_valid_date("February 0"))
    print("5.", is_a_valid_date(" December 3K1"))
    print("6.", is_a_valid_date("January 28 6"))
    print("7.", is_a_valid_date(" January 6  ")) #True
    print("8.", is_a_valid_date(" January   "))
    print("9.", is_a_valid_date("    May     9   ")) #True
#--------------------------------------------------
# 7777777777777777777777777777777777777777777777777
# Returns True if the parameter string is a
# valid date, otherwise returns False
#--------------------------------------------------
##def is_a_valid_date(date_str):
##    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
##    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
##
##    word = date_str.strip()
##    word_split = word.split()
##
##    for each_str in range(len(word_split)):
##        valid = word_split[each_str]
##        valid_num = word_split[-1]
##        if valid in month_names and valid_num.isdigit() and len(word_split) <=2:
##            position = word_split.index(valid)
##            if int(valid_num) <= days_in_month[position] and int(valid_num) > 0:
##                return True
##
##        else:
##            return False

        
def is_a_valid_date(date_str):
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    word = date_str.strip()
    word_split = word.split()

    valid_num = word_split[-1]
    valid_date = word_split[0]

    for each_str in range(len(word_split)):
        valid = word_split[each_str]
        if valid in month_names and len(word_split) == 2 :
            position = month_names.index(valid_date)
            if valid_num.isdigit() and int(valid_num) <= int(days_in_month[position]) and int(valid_num) > 0 :
                return True

        else:
            return False

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
