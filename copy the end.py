def insert_end(string):
    if len(string)>1:
        b=""
        for i in range(0,4):
            b=b+string[-2:]
    return b
print(insert_end('Python'))
print(insert_end('Exercises'))