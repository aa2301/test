import collections
def upper(string):
    b=a.split(" ")
    c=a.title().split(" ")
    print(b)
    print(c)
    e=[]
    if (collections.Counter(b)==collections.Counter(c)):
        d=True
        e.append(d)
    else:
        d=False
        e.append(d)
    f=all(e)
    return f
a=input("Enter The String: ")
print(upper(a))
