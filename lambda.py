# x = lambda a,b: (a*b)+10
# print(x(5,2))

def myfunc(n):
    print(n)
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

