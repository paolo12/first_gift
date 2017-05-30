def common_words(first, second):
    first = set(first.split(","))
    second = set(second.split(","))
    third = set.intersection(first, second)
    listing = list(third)
    listing.sort()
    stringer = ','.join(str(e) for e in listing)
    return stringer

"""
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert common_words("hello,world", "hello,earth") == "hello", "Hello"
    assert common_words("one,two,three", "four,five,six") == "", "Too different"
    assert common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

S = "hello,world"
print("type(S) =", type(S))
S1 = S.split(",")
print("type(S1) =", type(S1))
"""
common_words("one,two,three", "four,five,one,two,six,three")