##from Geometry import Point
##
##p = Point(5, 7)
##print(p.x, p.y)
##
##p.translate(1, 0)
##print(p.x, p.y)


##from ImageProcessing import Image
##image = Image(8, 8)
### set pixel at 3, 7 to value 255
##image.pixels[3][7] = 255


from Fraction import Fraction

## Default methods
f1 = Fraction(3, 4)
print(f1.get_numerator()) #3

f1.set_numerator(12)
print(f1.get_numerator()) #12


f1 = Fraction(1, 2)
f2 = Fraction(1, 2)
print(f1) # Calls a special method __str__
print(f1 == f2) # Calls a special method __eq__

##str
f1 = Fraction(1, 2)
print(f1)

##Eq
##f1 = Fraction(1, 2)
##f2 = Fraction(3, 4)
##f3 = Fraction(3, 6)
##
##print(f1 == f2)
##print(f1 == f3)
##
##
##Overriding __repr__
##f1 = Fraction(1, 2)
##print(repr(f1))
##
##
##add
##
##f1 = Fraction(1, 2)
##f2 = Fraction(1, 3)
##result = f1 + f2
##
##print(result)
##
##
##Greatest Common Divisor
##x = Fraction(2, 3)
##y = Fraction(3, 4)
##
##z = x + y
##
##print(z)
##
##w = z + Fraction(5, 12)
##
##print(w)
##print(w + Fraction(1, 6) == Fraction(2, 1))
##
##
##
##
##
##
##
##
