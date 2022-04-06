def check_dup(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i) 
    return b
a=[1,2,3,3,3,3,4,5]
print(check_dup(a))