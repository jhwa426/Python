"""
Lab 4:
"""

def main():
    letter = get_letter("Dreams")
    print(letter)

    print(get_letter("programming"))

def get_letter(word):
    print(word)
    
    while True:
        user = int(input("Enter index: "))
        if (user >= 0) and (user < len(word)):
            return word[user]
    
            
        

main()








