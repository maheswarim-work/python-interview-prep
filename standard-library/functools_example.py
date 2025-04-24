from functools import reduce, lru_cache
from functools import cached_property

##
print(reduce(lambda x, y: x + y, [1, 2, 3, 4])) #10
print(((1+2)+3)+4) #10

##
print(reduce(lambda x, y: x * y, [1, 2, 3, 4], 10))
print((((10 * 1) * 2) * 3) * 4)

##
class Data:
    def __init__(self, n):
        self.n = n

    @property
    def f(self):
        total = 0
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    total += i + j + k
        return total

###
d = Data(200)
print(d.f)

##

##
class Data2:
    def __init__(self, n):
        self.n = n

    @cached_property
    def f(self):
        total = 0
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    total += i + j + k
        return total

###
d2 = Data2(200)
print(d2.f)

##

# 0, 1, 1, 2, 3, 5, 8, 13 etc
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))

###

@lru_cache #Least-recently-used cache decorator.
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))
