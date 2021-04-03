"""
Name : Jeff Hwang
User name : jhwa426
ID number : 107793487

Question 4

"""

value = input("Value: ")
value = int(value)
print()

price100s = value // 100
quota = price100s
remainder = value % 100

price50s = remainder // 50
quota = price50s
remainder = remainder % 50 

price25s = remainder // 25
quota = price25s
reminder = remainder % 25 

price10s = reminder //10
quota = price10s 
reminter = reminder % 10 

price5s = reminder // 5 
quota = price5s 
remainder = reminder % 5 

prices1s = remainder // 1
quota = prices1s
remainder = remainder % 1

print("You will need : ")
print("=" * 19)
print("100s: ", price100s)
print(" 50s: ", price50s)
print(" 25s: ", price25s)
print(" 10s: ", price10s)
print("  5s: ", price5s)
print("  1s: ", prices1s)
print("=" * 19)
