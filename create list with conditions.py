def getstr(n1,n2):
    a=[]
    s=""
    for i in range(n1,n2):
        if i!=3:
            a.append(i)
    for i in a:
        s=s+" "+str(i)
    return s
print(getstr(0,6))