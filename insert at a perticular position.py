def insert(l,i,a):
    l1=[]
    l2=[]
    for j in range(0,i-1):
        l1.append(l[j])
    l1.append(a)
    for k in range(i-1,len(l)):
        l2.append(l[k])
    print(l1+l2)
l=[1,1,2,3,4,4,5,1]
insert(l,3,9)