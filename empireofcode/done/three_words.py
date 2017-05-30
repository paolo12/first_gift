def three_words(words):
    words = words.split(" ")
    n = 0
    for i in words:
        if not i.isdigit():
            n += 1
        elif n == 3:
            return True
        elif i.isdigit():
            n = 0

    if n >= 3:
        return True
    else:
        return False
"""
    if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert three_words("Hello World hello"), "Hello"
    assert not three_words("He is 123 man"), "123 man"
    assert not three_words("1 2 3 4"), "Digits"
    assert three_words("bla bla bla bla"), "Bla Bla"
    assert not three_words("Hi"), "Hi"

    print("Earn cool rewards by using the 'Check' button!")

three_words("Hello World hello") == True
three_words("He is 123 man") == False
three_words("1 2 3 4") == False
three_words("bla bla bla bla") == True
three_words("Hi") == False
"""
three_words("bla bla bla bla")