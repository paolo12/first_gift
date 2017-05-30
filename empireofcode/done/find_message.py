def find_message(text):
    s = ""
    for i in range(0, len(text)):
        if text[i].isupper():
            s = s + text[i]
            i += 1
        else:
            i += 1
    return s

"""
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

    print("Earn cool rewards by using the 'Check' button!")

s = "How are you? Eh, ok. Low or Lower? Ohhh."
s1 = ""
for i in range(0, len(s)):
    print("s[", i, "] -", s[i])
    if s[i].isupper():
        s1 += s[i]
        i += 1
    else:
        i += 1
print(s1)
"""

find_message("How are you? Eh, ok. Low or Lower? Ohhh.")