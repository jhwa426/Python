##Lab 4
##13.08.2020

##Ex 1
##def rate(n):
##    i = n
##    total = 0
##    while i > 0:
##        total += i
##        i -= 1
##    return total
##
##print(rate(10))


##Ex 2
##def rate(n):
##    i = n
##    total = 0
##    while i > 1:
##        total += i
##        i //= 2
##    return total
##
##print(rate(10))

##Ex 3
##def rate(n):
##    i = 0
##    total = 0
##    while i < 10:
##        j = 0
##        while j < 10:
##            total += j 
##            j += 1
##        i += 1
##    return total
##
##print(rate(1))


##Ex 4
def rate(n):
    i = 0 #1
    total = 0 #1
    count = 4
    while i < 10: #10
        count += 4
        j = 0 #n
        while j < n: #n(n+1)
            count += 3
            total += j #n * n
            j += 1 #n * n
        i += 1 #n
    return print(count) #1

##def rate(n):
##    return print(3*(n**2) + 3*n + 13)
##3n^2+ 3n + 13

rate(1)
rate(10)
rate(100)


##Ex 6
##def rate(n):
##    total = 0
##    i = 0
##    count = 4
##    while i < n:
##        count += 4
##        j = 0
##        while j < n:
##            count += 3
##            total += j 
##            j += 1
##        i += 1
##        
##    return print("Number of operations:", count)
##
##
##rate(2) #24
##rate(10) #32
##rate(20) #42

##Ex 7
##def rate(n):
##    total = 0
##    i = 1
##    count = 4
##    while i < n:
##        count += 4
##        j = 0
##        while j < n:
##            count += 3
##            total += j 
##            j += 1
##        i *= 2
##        
##    print("Number of operations:",count)
##
##rate(2)


##Ex 9
##def rate(n):
##    total = 0
##    i = 0
##    count = 4
##    while i < n:
##        count += 4
##        j = 0
##        while j < 2 * n:
##            count += 3
##            total += j 
##            j += 1
##        i += 1
##        
##    return print("Number of operations:",count)
##
##
####Test
##rate(2) #Number of operations: 36



##Ex 11
##def rate(n):
##    total = 0
##    i = 0
##    count = 20
##    while i < 4:
##        j = 0
##        while j < i:
##            count += 3
##            total += j
##            j += 1
##        i += 1
##    return print("Number of operations:",count)
##
####Test
##rate(2) #Number of operations: 38



