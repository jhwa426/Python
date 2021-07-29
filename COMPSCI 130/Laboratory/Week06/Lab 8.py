####Lab 8
####25.08.2020
####
####Ex 1 - 3
####Rectangle

class Rectangle:
    def __init__(self, width=10, height=10):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width
        
    def get_height(self):
        return self.__height
##Ex 2
    def __str__(self):
        return str(self.__width) + " x " + str(self.__height)
    
    def __repr__(self):
        return 'Rectangle(' + str(self.__width) + ', ' + str(self.__height) + ')'
##Ex 3
    def get_area(self):
        return self.__width * self.__height
    
    def get_perimeter(self):
        return (self.__width + self.__height) * 2


##Test Ex 1
r1 = Rectangle(3, 4)
print(r1.get_width(), r1.get_height()) #3 #4
r2 = Rectangle()
print(r2.get_width(), r2.get_height()) #10 #10

##Test Ex 2
r1 = Rectangle(3, 4)
print(r1) #3 x 4
print(repr(r1)) #Rectangle(3, 4)
r2 = Rectangle()
print(r2) #10 x 10
print(repr(r2)) #Rectangle(10, 10)


##Test Ex 3

r1 = Rectangle(3, 4)
print(r1.get_area()) #12
print(r1.get_perimeter()) #14
r3 = Rectangle()
print(r3.get_area()) #100
print(r3.get_perimeter()) #40


####Ex4 - 8
####QuadraticEquation

class QuadraticEquation:

    def __init__(self, coeff_a = 1, coeff_b = 1, coeff_c = 1):
        self.__coeff_a = coeff_a
        self.__coeff_b = coeff_b
        self.__coeff_c = coeff_c

    def get_coeff_a(self):
        return self.__coeff_a
    
    def get_coeff_b(self):
        return self.__coeff_b
    
    def get_coeff_c(self):
        return self.__coeff_c

##Ex 5       
    def get_discriminant(self):
        return (self.__coeff_b)**2 -4*(self.__coeff_a * self.__coeff_c)

##Ex 6
    def has_solution(self):
        equation = (self.__coeff_b)**2 -4*(self.__coeff_a * self.__coeff_c)
        if equation < 0:
            return False
        else:
            return True

##Ex 7
    def get_root1(self):
        numerator = -self.__coeff_b + ((self.__coeff_b)**2 -4*(self.__coeff_a * self.__coeff_c))**(1/2)
        denominator = 2 * self.__coeff_a

        return numerator / denominator
    
    def get_root2(self):
        numerator = -self.__coeff_b - ((self.__coeff_b)**2 -4*(self.__coeff_a * self.__coeff_c))**(1/2)
        denominator = 2 * self.__coeff_a
        
        return numerator / denominator

##Ex 8
    def __str__(self):
        equation = (self.__coeff_b)**2 -4*(self.__coeff_a * self.__coeff_c)
        
        numerator1 = -self.__coeff_b + (equation)**(1/2)
        denominator1 = 2 * self.__coeff_a
        numerator2 = -self.__coeff_b - (equation)**(1/2)
        denominator2 = 2 * self.__coeff_a

        if  equation < 0:
            return "The equation has no roots."
        elif (numerator1 / denominator1) == (numerator2 / denominator2):
            return "The root is {:.2f}.".format(numerator1 / denominator1)
        else:
            return "The roots are {:.2f} and {:.2f}.".format((numerator1 / denominator1),(numerator2 / denominator2))
        

##Test Ex 4
equation1 = QuadraticEquation(1, 2, 1)
print(equation1.get_coeff_a(), equation1.get_coeff_b(), equation1.get_coeff_c()) #1 2 1
equation2 = QuadraticEquation()
print(equation2.get_coeff_a(), equation2.get_coeff_b(), equation2.get_coeff_c()) #1 1 1

##Test Ex 5
equation1 = QuadraticEquation(1, 2, 1)
print(equation1.get_discriminant()) #0
equation2 = QuadraticEquation()
print(equation2.get_discriminant()) #-3

##Test Ex 6
equation1 = QuadraticEquation(1, 2, 1)
print(equation1.has_solution()) #True
equation2 = QuadraticEquation()
print(equation2.has_solution()) #False 

##Test Ex 7
equation1 = QuadraticEquation(4, 4, 1)
print(equation1.get_root1(), equation1.get_root2()) #-0.5 -0.5
equation3 = QuadraticEquation(1, 2, -63)
print(equation3.get_root1(), equation3.get_root2()) #7.0 -9.0


##Test Ex 8
equation1 = QuadraticEquation(4, 4, 1)
print(equation1) #The root is -0.50.
equation2 = QuadraticEquation()
print(equation2) #The equation has no roots.
equation3 = QuadraticEquation(1, 2, -63)
print(equation3) #The roots are 7.00 and -9.00.


####Ex 9 - 10
####Product


class Product:
    def __init__(self, product_id, product_name, product_price = 1):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_price = product_price

    def __str__(self):
        product = self.__product_name + "(id = " + str(self.__product_id) + "), $" + str(self.__product_price)
        return product
        
##Ex 10
    def set_product_price(self, product_price):
        if self.__product_price >= 0 and self.__product_price <= 999:
            return self.__product_price
        else:
            self.__product_price = product_price
            return self.__product_price
        
    def get_product_price(self):
        return self.__product_price

    def set_product_name(self, product_name):
        self.__product_name = product_name
        return self.__product_name
            
    def get_product_name(self):
        return self.__product_name

    def set_product_id(self, product_id):
        if self.__product_id > 1:
            return self.__product_id
        else:
            self.__product_id = 10
            return self.__product_id

    def get_product_id(self):
        return self.__product_id
        


####Test Ex 9
##p1 = Product(1, 'Apple iPhone SE 64GB', 799)
##p2 = Product(2, 'Apple iPhone 11 64GB', 1349)
##p3 = Product(3, 'Dynamix A-SC-HD15F Solder Connector')
##print(p1) #Apple iPhone SE 64GB(id = 1), $799
##print(p2) #Apple iPhone 11 64GB(id = 2), $1349
##print(p3) #Dynamix A-SC-HD15F Solder Connector(id = 3), $1


####Test Ex 10
p1 = Product(1, 'Apple iPhone SE 64GB', 799)
print(p1.get_product_price()) #799
print(p1.get_product_name()) #Apple iPhone SE 64GB
print(p1.get_product_id()) #1
p1.set_product_price(-10)
p1.set_product_name("Unknown")
p1.set_product_id(10)
print(p1) #Unknown(id = 10), $799

print()

p1 = Product(1, 'Apple iPhone SE 64GB', 799)
p2 = Product(2, 'Apple iPhone 11 64GB', 1349)
p2.set_product_price(1320)
p1.set_product_name("Unkown")
print(p2.get_product_price()) #1320
print(p1.get_product_name()) #Unkown
print(p1) #Unkown(id = 1), $799
print(p2) #Apple iPhone 11 64GB(id = 2), $1320

##Ex 11

class Goat:
    def __init__(self, age):
        self.__age = age

    def __str__(self):
        result = "I am a Goat. My age is {}".format(self.__age)
        return result

    def get_age(self):
        if self.__age > 0:
            return self.__age
        else:
            self.__age = 50
            return self.__age

    def set_age(self, age):
        self.__age = age
        return self.__age

    def speak(self, repeat = 1):
        return print(repeat * "Baaa ")


##Test
animal = Goat(2)
print(animal) #I am a Goat. My age is 2
animal.set_age(50)
print("Now my age is", animal.get_age()) #Now my age is 50
animal.set_age(-2)
print("My age is", animal.get_age()) #My age is 50
animal.speak() #Baaa
animal.speak(5) #Baaa Baaa Baaa Baaa Baaa


##Ex 12
class Robot:
    def __init__(self, name, position = (0,0)):
        self.__name = name
        self.__position = position

    def move_to(self, x_position, y_position):
        self.__position = x_position, y_position

    def up(self, displacement):
        self.__position = self.__position[0], self.__position[1] + displacement

    def right(self, displacement):
        self.__position = self.__position[0] + displacement, self.__position[1]

    def __str__(self):
        result = "{} is at {}".format(self.__name, self.__position)
        return result
        


##Test
##robot1 = Robot("Marvin")
print(robot1) #Marvin is at (0, 0)
robot1.move_to(5, 11)
print(robot1) #Marvin is at (5, 11)
robot1.move_to(1, 2)
print(robot1) #Marvin is at (1, 2)
robot1.up(3)
robot1.right(-4)
print(robot1) #Marvin is at (-3, 5)


robot1 = Robot("Marvin", (19, 3))
print(robot1) #Marvin is at (19, 3)
robot1.up(3)
robot1.right(4)
print(robot1) #Marvin is at (23, 6)

