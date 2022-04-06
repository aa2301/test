a=input()
b=input()
l=[]
for i in a:
    if i in b:
        l.append(i)
print(''.join(l))