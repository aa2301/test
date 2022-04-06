from re import X


def sorteo(unsortedlist):
    print("Even numbers from the said list:")
    c=list(filter(lambda x: x%2==0,unsortedlist))
    print(c)
    print("Odd numbers from the said list:")
    d=list(filter(lambda y: y%2!=0, unsortedlist))
    return d
a=[1,2,3,4,5,6,7,8,9,10]
print("Original list of integers:")
print(a)
print(sorteo(a))