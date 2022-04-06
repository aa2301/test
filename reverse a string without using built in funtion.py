from re import A


def rev(string):
    b=""
    for i in string:
        b=i+b
    return b
print(rev("1234abcd"))