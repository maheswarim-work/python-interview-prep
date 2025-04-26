from collections import Counter

my_list = ['apple', 'banana', 'apple', 'orange']
count = Counter(my_list)

print(count)
# Output: Counter({'apple': 2, 'banana': 1, 'orange': 1})
print(count.most_common(3))
