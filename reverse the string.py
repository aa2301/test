def rev(string):
    a=string.upper()
    b=a[::-1]
    if a==b:
        return True
    else:
        return False
print(rev("Wow"))