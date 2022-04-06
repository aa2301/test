def count(string):
    a=0
    b=0
    for i in string:
        if ord(i) in range(65,91) or ord(i) in range(97,123):
            a+=1
        elif ord(i) in range(48,58):
            b+=1
        else:
            pass
    print("Letters:",a)
    print("Digits:",b)
count("Python 3.2")
