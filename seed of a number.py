def seed(a,b):
    n=a
    s=a
    while(n>0):
        f=n%10
        n//=10
        s*=f
    if s==b:
        return True
    else:
        return False
a,b = [int(x) for x in input().split(',')]
print(seed(a,b))