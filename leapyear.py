def leapyear(a):
    if a%4==0:
        if a%100==0 and a%400==0:
            k=True
        elif a%100!=0:
            k=True
        else:
            k=False
    else:
        k=False
    return k
a=int(input())
print(leapyear(a))