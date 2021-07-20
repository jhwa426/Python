##Ex 1
##name = "Jeff"
##price = 10.1
##number = 2
##boolean_value = True

##Ex 2
##gst = 1.15
##
##price = float(input("Enter a price: "))
##result = gst * price
##
##print("GST applied:", round(result, 2))

##Ex 3

#Michael
##user_input = input("Enter a sentence: ")
##
##for each in range(len(user_input)):
##    if user_input[each].islower():
##        print(user_input[each].upper(), end="")
##    else:
##        print(user_input[each].lower(), end="")


##Ex 4
##a_list = []
##b_list = []
##
##user_input1 = input("Enter a word: ") #struts
##user_input2 = input("Enter another word: ") #trusts
##
##for word1 in user_input1:
##    a_list.append(word1)
##a_list.sort()
##
##for word2 in user_input2:
##    b_list.append(word2)
##b_list.sort()
##
##if a_list == b_list:
##    result1 = user_input1 + " and " + user_input2 + " are anagrams of each other."
##    print(result1)
##else:
##    result2 = user_input1 + " and " + user_input2 + " are not anagrams of each other."
##    print(result2)


##Ex 5
##for number in range(200, 296):
##    if number == 295:
##        print(number)
##    elif (not number % 3 == 0) and number % 5 == 0:
##        print(str(number) + ",", end = "")


##Ex 6

##user_input = int(input("Enter a number: "))
##a_list = []
##
##while user_input != -999:
##    a_list.append(user_input)
##    user_input = int(input("Enter a number: "))
##    
##print(a_list)
    
    
##Ex 7

##user_input = int(input("Enter number of rows: "))
##
##for number in range(1, user_input + 1):
##    for column in range(1, number + 1):
##        print(column, end =" ")
##    print("")


##Ex 8
##user_input = int(input("Enter number of rows: ")) #5 #9
##
##
##for row in range(1, user_input + 1):
##    if row == 1:
##        print("*" * user_input)
##    elif row == user_input:
##        print("*" * user_input)
##    else:
##        for column in range(1, user_input + 1):
##            if column == 1:
##                print("*",end = "")
##            elif column == user_input:
##                print("*",end = "")
##            elif column == row:
##                print("*",end = "")
##            elif column == (user_input - row) + 1:
##                print("*",end = "")
##            else:
##                print(" ",end = "")
##            
##        print("")

user_input = int(input("Enter number of rows: ")) #5 #9

for row in range(1, user_input + 1):
    if row == 1:
        print("*" * user_input)
    elif row == user_input:
        print("*" * user_input)
    else:
        for column in range(1, user_input + 1):
            if column == 1:
                print(column,end = "")
            elif column == user_input:
                print(column,end = "")
            elif column == row:
                print(column,end = "")
            elif column == (user_input - row) + 1:
                print(column,end = "")
            else:
                print(" ",end = "")
            
        print("")  

##Ex 9
##user_input = int(input("Enter an integer: "))
##a_tuple = ()
##
##for number in range(1, user_input+1):
##    a_tuple = a_tuple + (number,)
##
##print(a_tuple)
    

##Ex 10
##user_input = input("Enter a word: ")
##
##a_dic = {}
##
##for letter in range(len(user_input)):
##    word = user_input[letter]
##    ascii_code = ord(word)
##    a_dic[word] = ascii_code
##    
###print
##for key in sorted(a_dic.keys()):
##    print(key, ":", a_dic[key],sep="")









