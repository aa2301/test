#1 que
def rmtp(tuple):
    b=[]
    for i in tuple:
        if i!=():
            b.append(i)
    return b
a=[(),(),('',),('a','b'),('a','b','c'),('d')]
print(rmtp(a))