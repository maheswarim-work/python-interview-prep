def fizz_buzz(numbers):
    '''
    Given a list of integers:
    1. Replace all integers that are divisible by 3 with "fizz"
    2. Replace all integers that are divisible by 5 with "buzz"
    3. Replace all integers that are both divisible by 3 and 5 with "fizzbuzz"
    '''
    print(numbers)
    for i in range(len(numbers)):
        # print(numbers[i])
        num = numbers[i]
        if num % 3 == 0:
            numbers[i] = "fizz"
            # print(numbers)
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num % 3 == 0 and  num % 5 == 0:
            numbers[i] = "fizzbuzz"
    return numbers


if __name__ == '__main__':
    nums = [45, 22, 14, 65, 97, 72]
    print(fizz_buzz(nums))
