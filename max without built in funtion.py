def large(l1):
    c=0
    for i in range(len(l1)+1):
        if l1[i]<l1[i+1]:
            c=l1[i+1]
        else:
            pass
    return c
print(large([1,5,-8,0,-2]))