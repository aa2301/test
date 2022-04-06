#3 que
def colist(l1):
    c=0
    for i in l1:
        a=list(i)
        if a[0]==a[-1]:
            c+=1
    return c
print(colist(['abc', 'xyz', 'aba', '1221']))