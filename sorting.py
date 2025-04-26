# animals = ["cat", "dog", "cheetah", "rhino"]

# sort strings
# print(sorted(animals))
# print(sorted(animals, reverse=True))

# sort dict error
# animals = [
#     {'type': 'cat', 'name': 'Stephanie', 'age': 8},
#     {'type': 'dog', 'name': 'Devon', 'age': 3},
#     {'type': 'rhino', 'name': 'Moe', 'age': 5}
# ]
# print(sorted(animals))

# sort dict lambda
animals = [
    {'type': 'cat', 'name': 'Stephanie', 'age': 8},
    {'type': 'dog', 'name': 'Devon', 'age': 3},
    {'type': 'rhino', 'name': 'Moe', 'age': 5}
]
# print(sorted(animals, key=lambda animal:animal['age']))
# print(sorted(animals, key=lambda animal:animal['age'], reverse=True))
# print(sorted(animals, key=lambda animal:animal['age'], reverse=True)[0])

print(animals.sort(key=lambda animal:animal['age']))
print(animals)
