VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def striped_words(text):
    n = 0
    text = text.split()
    text = ' '.join(str(e) for e in text)
    text = text.split(',')
    text = ' '.join(str(e) for e in text)
    text = text.split('.')
    text = ' '.join(str(e) for e in text)
    print("text = ", text)
    for _ in text.split():
        print("_ =", _)
        m = 0
        for i in range(0, len(_) - 1):
            print("_[", i, "] =", _[i])
            if _[i].upper() not in VOWELS and _[i].upper() not in CONSONANTS:
                print("i(1) =", i)
                m = 0
                print("m(1) =", m)
                break
            elif _[i].upper() in VOWELS and _[i + 1].upper() not in VOWELS or _[i + 1].isalpha() is not True:
                print("i(2) =", i)
                m = 1
                print("m(2) =", m)
            elif _[i].upper() in CONSONANTS and _[i + 1].upper() not in CONSONANTS or _[i + 1].isalpha() is not True:
                print("i(3) =", i)
                m = 1
                print("m(3) =", m)
            else:
                m = 0
                break
            n += m
        print("___")
    return n

print("n =", striped_words("Hello world"))
"""

Striped Words

The alphabet contains both vowel and consonant letters (yes, we divide the letters).

Vowels -- A E I O U Y

Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with different words. These words are separated by white-spaces and punctuation marks. 
Numbers are not considered words in this mission (a mix of letters and digits is not a word either). You should count 
the number of words (striped words) where the vowels with consonants are alternating, that is; words that you count 
cannot have two consecutive vowels or consonants. The words consisting of a single letter are not striped -- do not 
count those. Casing is not significant for this mission.

Input: A text as a string.

Output: A quantity of striped words as a number.

Example:

striped_words("My name is ...") == 3
striped_words("Hello world") == 0
striped_words("A quantity of striped words.") == 1
striped_words("Dog,cat,mouse,bird.Human.") == 3
Precondition:

A text contains only ASCII symbols.

0 < |text| < 10000

How it is used:

This idea in this task is a useful exercise for linguistic research and analysis. Text processing is one of the main 
tools used in the analysis of various books and languages and can help translate print text to a digital format.

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert striped_words("My name is ...") == 3, "All words are striped"
    assert striped_words("Hello world") == 0, "No one"
    assert striped_words("A quantity of striped words.") == 1, "Only of"
    assert striped_words("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
"""