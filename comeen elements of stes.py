def commen(s1,s2):
    return s1 - s1.intersection(s2)
set1 = {10, 20, 30} 
set2 = {20, 40, 50}
print(commen(set1,set2))