#multiplication in tuple 
def mul(tup):
    a=1
    for i in tup:
        a*=i
    return a
print(mul((4, 3, 2, 2, -1, 18)))
print(mul((2, 4, 8, 8, 3, 2, 9)))