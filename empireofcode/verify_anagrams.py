def verify_anagrams(first_word, second_word):
    first_word = str(first_word).replace(' ', '').lower()
    second_word = str(second_word).replace(' ', '').lower()

    first_word = list(first_word)
    second_word = list(second_word)

    first_word.sort()
    second_word.sort()

    print("first_word =", first_word)
    print("len(first_word) =", len(first_word))

    print("second_word =", second_word)
    print("len(second_word) =", len(second_word))

    if len(first_word) == len(second_word) and len(first_word) > 1:
        for i in range(0, len(first_word) - 1):
            if ord(first_word[i]) == ord(second_word[i]):
                n = True
                i += 1
            else:
                n = False
                i += 1
    elif len(first_word) == len(second_word) and len(first_word) == 1:
        return ord(first_word[0]) == ord(second_word[0])
    else:
        n = False
    return n


"""
Verify Anagrams
To institute a super secret password-answer security system, we've implemented an anagram policy where all passwords 
must be anagrams for answers. There's only one problem, we need to verify that people are using proper anagrams in 
their passwords.

An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or 
phrase, using all the original letters exactly once. Two words are anagrams to each other if we can get one from 
another by rearranging the letters. Anagrams are case-insensitive and don't take whitespaces into account.

For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.

You are given two words or phrases. Try to verify if they are anagrams.

Input: Two arguments. Words as strings.

Output: Determination if the passwords are anagrams or not as boolean (True or False).

Example:

verify_anagrams("Programming", "Gram Ring Mop") == True
verify_anagrams("Hello", "Ole Oh") == False
verify_anagrams("Kyoto", "Tokyo") == True
Precondition:

0 < |first_word| < 100

0 < |second_word| < 100

Words contain only ASCII latin letters and whitespaces.

How it is used:

Anagramming can be a fun way to train your brain, but they have other applications. Psychologists use anagram-oriented 
tests, often called "anagram solution tasks", to assess the implicit memory. Anagrams are often used to create 
pseudonyms, allowing one to conceal, reveal or operate somewhere in between - like a mask that can establish identity. 
In addition to this, multiple anagramming is a technique sometimes used to solve some kinds of cryptograms.

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
"""
print(verify_anagrams("bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU",
                      "TSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"))