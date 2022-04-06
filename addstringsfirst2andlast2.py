def addstr(str1,str2):
    return str2[:2]+str1[2:len(str1)]+" "+str1[:2]+str2[2:len(str2)]
print(addstr("abc","xyz"))