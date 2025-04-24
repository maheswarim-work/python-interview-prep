import string
import timeit
from string import ascii_lowercase

print(ord('A'))
print('A' > 'a')
print('abc' > 'abd')
print(ord('c'))
print(ord('d'))
print('HELLO WORLD'.isupper())
print(string.ascii_uppercase)

###

def is_upper(s):
    for letter in s:
        if letter not in string.ascii_uppercase:
            return False
        return True

print(is_upper('HELLO WORLD'))
print(is_upper('HELLOWORLD'))

###

uppercase_set = set(string.ascii_uppercase)

def is_upper_using_set(s):
    for letter in s:
        if letter not in uppercase_set:
            return False
        return True


time_taken = timeit.timeit("is_upper('HELLO WORLD')", globals=globals())
print(time_taken)

time_taken_set = timeit.timeit("is_upper_using_set('HELLO WORLD')", globals=globals())
print(time_taken_set)

###

def is_upper_cleaner(s):
    return all(letter in uppercase_set for letter in s)

print(is_upper_cleaner('HELLO WORLD'))
print(is_upper_cleaner('HELLOWORLD'))

result = all(print(5) for _ in range(5))
print(result)

###
print(string.ascii_letters)
print(string.ascii_uppercase)
print(ascii_lowercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
print(string.whitespace)

###
whitespace_set = set(string.whitespace)

print(''.join(letter for letter in 'HELLO WORLD' if letter not in whitespace_set))
















