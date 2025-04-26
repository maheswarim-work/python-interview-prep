
lst = [1, 2, -5, 4]
def square(x):
    return x * x

def is_odd(x):
    return x % 2 == 1

if __name__ == '__main__':

    # map
    # print(list(map(square, lst)))

    # for loop
    # result = []
    # for num in lst:
    #     result.append(square(num))
    # print(result)

    # list comprehension
    # result = [square(num) for num in lst]
    # print(result)

    # odd filter
    # print(list(filter(is_odd, lst)))

    # odd list comprehension
    # print([num for num in lst if is_odd(num)])

    # grid
    # num_rows = 2
    # num_cols = 3
    # grid = []

    # grid using for loop
    # for _ in range(num_rows):
    #     curr_row = []
    #     for _ in range(num_cols):
    #         curr_row.append(0)
    #     grid.append(curr_row)
    # print(grid)

    # grid using list comprehension
    # grid2 = [[0 for col in range(num_cols)] for row in range(num_rows)]
    # print(grid2)

    # max
    # print(max(lst))

    # max of square using lambda
    # print(max(lst, key=lambda x: x * x))

    # min
    # print(min(lst))

    # min of square using lambda
    # print(min(lst, key=lambda x: x * x))

    # odd number using lambda
    print([(lambda x: x % 2 == 1)(num) for num in lst])

    print(any([(lambda x: x % 2 == 1)(num) for num in lst]))

    print(all([(lambda x: x % 2 == 1)(num) for num in lst]))
