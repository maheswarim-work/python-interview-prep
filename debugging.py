# def max_number(lst):
#     max_num = -float('inf')
#     for num in lst:
#         print(num, max_num)
#         if num > max_num:
#             print("entered if stmt")
#             max_num = num
#     return max_num
#
#
# print((max_number([-1, -2, -4])))


def max_number(lst):
    max_num = -float('inf')
    for num in lst:
        breakpoint()
        if num > max_num:
            print("entered if stmt")
            max_num = num
    return max_num

print((max_number([-1, -2, -4])))
