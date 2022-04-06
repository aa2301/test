#1st approch
def fact(num):
    f=1
    if num<2 and num>-1:
        return 1
    elif num<0:
        return None
    else:
        f=1
        while num>0:
            f=f*num
            num-=1
        return f
print(fact(5))       

#2nd approch using reccursion
def fact(num):
    if num>1:
        return num*fact(num-1)
    elif num<2 and num>-1:
        return 1
    else:
        return None
print(fact(5))

#3rd approch using fuction defined and predefined method
from math import factorial
def fact(num):
    return factorial(num) 
print(fact(5))

#4th approch direct 
from math import factorial
print("Factorial=",factorial(5))