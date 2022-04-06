def insert_sting_middle(s1,s2):
    return s1[:len(s1)//2]+s2+s1[len(s1)//2:]
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('[[]]', 'Python'))