VOWELS = "aeiouy"

def translate(phrase):
    phrase = list(phrase)
    a = len(phrase)
    try:
        for i in range(0, a):
            if phrase[i] not in VOWELS and phrase[i] != " ":
                del phrase[i + 1]
            elif phrase[i] == " ":
                i += 1
            else:
                del phrase[i + 1]
                del phrase[i + 1]
    except IndexError:
        return ''.join(phrase)
    return ''.join(phrase)

print(translate("aaa bo cy da eee fe"))

"""

Bird Language

Robots keep little mechbirds as pets. Recently, they were trying to teach it how to speak basic language. Today the 
bird spoke its first word: "hieeelalaooo". This sounds a lot like "hello", but with too many vowels. With the 
information they discovered, we should help them to make a translation module.

The bird converts words by two rules:

after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
Vowels letters == "aeiouy".

You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one 
whitespace). The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given 
in lowercase. You should translate this phrase from the bird language to something more understandable.

Input: A bird phrase as a string.

Output: The translation as a string.

Example:

translate("hieeelalaooo") == "hello"
translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
translate("aaa bo cy da eee fe") == "a b c d e f"
translate("sooooso aaaaaaaaa") == "sos aaa"
Precondition:

A phrase satisfies regexp "\A([a-z]+\ ?)+(<!\ )\Z".

A phrase always has the translation.

How it is used:

This a similar cipher to those used by children when they invent their own "bird" language. Now you will be ready to crack the code.

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
"""


"""
    phrase = list(phrase)
    phrase2 = list()

    def consonant(stroka, n):
        stroka2 = list()
        for i in range(0, len(stroka) - 1, n):
            print("i(do) =", i)
            if CONSONANTS.find(stroka[i]) != -1:
                stroka2.append(stroka[i])
                print("stroka2 =", stroka2)
            else:
                i += 1
            print("i(posle) =", i)
        stroka = ''.join(stroka2)
        return stroka


    print("CONSONANTS")
    for i in range(0, len(phrase) - 1):
        print("i(do) =", i)
        if CONSONANTS.find(phrase[i]) != -1:
            phrase2.append(phrase[i])
            print("phrase2 =", phrase2)
        else:
            i += 2
        print("i(posle) =", i)

    print("VOWELS")
    for i in range(0, len(phrase) - 1, 2):
        print("i(do) =", i)
        if VOWELS.find(phrase[i]) != -1:
            phrase2.append(phrase[i])
            print("phrase2 =", phrase2)
        else:
            i += 2
        print("i(posle) =", i)
    phrase = ''.join(phrase2)
"""