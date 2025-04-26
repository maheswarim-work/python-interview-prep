# mylist = ['apple', 'banana', 'cherry']
# print(mylist[-1])

# fruits = ["apple", "banana", "cherry"]
# print(fruits[1])

# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[2:6])

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
result = [x for x in fruits if "a" in x]
print(result)
