#Adding the Digits of number
def add(num):
    a=num
    s=0
    while(a>0):
        n=a%10
        a//=10
        s+=n
    return s
print(add(12345))