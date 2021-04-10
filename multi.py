def multi(n,x,y):
    lst = []
    if n >= max(x,y):
        for i in range(x,n,x):
            if i%y != 0:
                lst.append(i)

    return lst

x = lambda n,x,y: [i for i in range(x,n,x) if i%y != 0]

print(multi(45,21,15))
print(x(45,21,15))