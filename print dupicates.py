def check_dup(a):
    b=[]
    for i in a:
        if a.count(i)>1:
            b.append(i)
    return b
a=[1,2,2,3,3,4,4,4]
print(check_dup(a))
