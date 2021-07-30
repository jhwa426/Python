class Fraction:
    def __init__(self, top, bottom):
        self.__numerator = top
        self.__denominator = bottom

    def get_numerator(self):
        return self.__numerator

    def set_numerator(self, top):
        self.__numerator = top
        
## return string
    def __str__(self):
        return '(' + str(self.__numerator) + '/' + str(self.__denominator) + ')'

    def __repr__(self):
        return 'Fraction(' + str(self.__numerator) + ', ' + str(self.__denominator) + ')'
## return string

    def __eq__(self, other):
        return self.__numerator * other.__denominator == other.__numerator * self.__denominator

    def __add__(self, other):
        new_num = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        new_den = self.__denominator * other.__denominator
        
        return Fraction(new_num, new_den)


##Greatest Common Divisor
    def __gcd(m, n):
        while m % n != 0:
            old_m = m
            old_n = n
            m = old_n
            n = old_m % old_n
        return n

##Improving the constructor
    def __init__(self, top, bottom):
        common = Fraction.__gcd(top, bottom)

        self.__numerator = top // common
        self.__denominator = bottom // common
