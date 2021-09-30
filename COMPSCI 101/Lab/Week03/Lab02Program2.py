"""
Jeff Hwang ,

prompt the user to enter a floating-point value and an integer value and calculates
and display the value obtained when the floating-point value is rased to the power of
the integer value.


Exercise 2
"""

output_floating = float(input("Enter a floating point number: "))
output_integer = int(input("Enter an integer: "))

convert = abs(output_floating) ** output_integer

print(output_floating, "to the power of", output_integer, "is", round(convert,3))
