from collections import Counter

def top_three_letters(input_string):
 print(Counter(input_string))
 return Counter(input_string).most_common(3)

if __name__ == '__main__':
    input_string = "abbccabc"
    print(top_three_letters(input_string))
