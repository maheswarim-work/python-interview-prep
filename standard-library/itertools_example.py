import itertools as it

##
all_ones = it.repeat(1)
print(next(all_ones))

##
print(list(map(pow, range(10), it.repeat(2))))
print(list(map(pow, range(10), it.repeat(3))))
print(list(map(pow, range(10), it.repeat(4))))

##
all_ones = it.repeat(1, times=5)
print(list(all_ones))

alternating_ones = it.cycle([1, -1])
print(next(alternating_ones))

##
friends = ["Jack", "Jill", "Joe"]
print(list(it.permutations(friends, r=2)))
print(list(it.permutations(friends, r=3)))
print(list(it.permutations(friends, r=4)))
