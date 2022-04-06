def k(l):
    o=[]
    f=[]
    for i in l:
        for j in i:
            if 0<=j<=9:
                o.append(int(j))
            elif 65<=ord(j)<=91:
                

    return
l=["A:1","B:1","A:5","B:-1","A:1"]
print(k(l))