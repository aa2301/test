def combine(list,string):
    l=[]
    for i in list:
        l.append(string+str(i))
    return l
print(combine([1,2,3,4],"emp"))