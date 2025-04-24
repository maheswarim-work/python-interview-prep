from collections import Counter

def top_three_letters(input_string):
 return Counter(input_string).most_common(3)

if __name__ == '__main__':
    input_string = "abbccabc"
    print(top_three_letters(input_string))
    # Result
    # [('b', 3), ('c', 3), ('a', 2)]
