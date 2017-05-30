def count_units(number):
    number = list(bin(number))
    n = 0
    for i in number:
        if i == '1':
            n += 1
    return n
"""
Binary Count

For the Robots the decimal format is inconvenient. If they need to count to "1", their computer brains want to count it
out in binary representation of that number. You can read more about binary here.

So for now, we are using integers to inform our watchtowers about the quantity of enemies they have incoming.

You are given a positive integer as a number, and you need to convert it to the binary format then count how many 
units (1) there are. For example: 5 = 0b101 contains two units, so the answer is 2.

Input: A number as a positive integer.

Output: The quantity of units in binary form as an integer.

Example:

count_units(4) == 1
count_units(15) == 4
count_units(1) == 1
count_units(1022) == 9
Precondition:

0 ≤ number ≤ 232

How it is used:

Binary as a computer language is very difficult for humans to understand, but makes the lives of our computers and 
robots easier. Every time you press a key on your keyboard it sends a binary signal informing the computer you hit 
that key. Every time you code a program, the computer takes your code and interprets it in binary then executes your 
program.

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_units(4) == 1
    assert count_units(15) == 4
    assert count_units(1) == 1
    assert count_units(1022) == 9

    print("Use 'Check' to earn sweet rewards!")
"""
print(count_units(1022))