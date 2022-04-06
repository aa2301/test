from itertools import permutations
def permutation(l):
    return permutations(l)
i=input
l=[]
for j in range(int(i)):
    b=int(input)
    l.append(b)
print(permutation(l))