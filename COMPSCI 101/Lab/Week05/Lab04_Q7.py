"""
Lab 4:
"""

def main():
    result = test_string("Antonid")
    print(result)
    print(test_string("Anatonis"))
    print(test_string("PD"))

def test_string(phrase):
    if ((len(phrase) % 2 == 0) and (phrase[0] in ("aeiouAEIOU") or phrase[-1] in ("aeiouAEIOU"))):
        
        return True
    
    else:
        return False


##Q7
##def test_string(phrase):
##    vowel = "aeiouAEIOU"
##
##    if len(phrase) % 2 == 0 and (phrase[0] in vowel or phrase[-1] in vowel):
##        return True
##    else:
##        return False


main()

