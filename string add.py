def strdd(string):
    if len(string)>1:
        return string[:2]+string[-2:]
    else:
        return " "
print(strdd("w"))