import sys

g = (i for i in range(1,1001))
print(sys.getsizeof(g))

l = [i for i in range(1,1001)]
print(sys.getsizeof(l))
