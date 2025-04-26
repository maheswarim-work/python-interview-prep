# def count_unique(input_set):
#     seen_c = set()
#     for element in input_set:
#         if element not in seen_c:
#             seen_c.add(element)
#     return len(seen_c)

def count_unique(input_set):
    return len(set(input_set))

if __name__ == '__main__':
    print(count_unique("abcdefa"))
