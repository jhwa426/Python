##COMPSCI.101.C.S1.2020 Mock test

##Ex 1
##result = 21 // 4 ** 2 - 1 + 16 / 5 * 3 // 2 - 1
##print("Result:", result)


##Ex 2
##value = 3 ** (1 + 1 * 2) // 5 % (20 / 2)
##print(value)


##Ex 3
##phrase = "How marvellous."
##bits_of_string = (phrase[-2] + "-" + phrase[2: 5] + "-" + phrase[4: : 2])
##print("Output:", bits_of_string) 

##Ex 4
##word = "ENERGY"
##result = (word[ : : 3] * 2).lower() + word[ : : -2]
##print("**" + result + "**")


##Ex 6
##def get_letter(score):
##    if score >= 60:
##        letter = "D"
##    elif score >= 70:
##        letter = "C"
##    elif score >= 80:
##        letter = "B"
##    elif score >= 90:
##        letter = "A"
##    else:
##        letter = "F"
##
##    return letter
##
##def main():
##  print(get_letter(95), end = " ")
##  print(get_letter(66), end = " ")
##  print(get_letter(74), end = " ")
##  print(get_letter(87), end = " ")
##  print(get_letter(54), end = " ")
##
##main()

##Ex 7

number = 16

while number > 4:
    number = number - 5
    if number % 2 == 0:
        number = number - 1
    print(number, end = " ")
    
print("Stop.")













