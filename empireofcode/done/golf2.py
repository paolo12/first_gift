def golf(number):
    number = list(str(number))
    n = 1
    for i in number:
        if int(i) != 0:
            n = n * int(i)
        else:
            continue
    return n

print(golf(999))

"""
Digits Multiplication

After programming the computers to handle division we should add functionality for multiplication. For this we will 
use a simple numbers exercise.

You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120.

In this mission the main goal to make your code as short as possible. The shorter your code, the more points you earn. 
Your score for this mission is dynamic and directly related to the length of your code.

Input: A positive integer.

Output: The product of the digits as an integer.

Example:

golf(123405) == 120
golf(999) == 729
golf(1000) == 1
golf(1111) == 1
Precondition:

0 < number < 106

Scoring:

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

Rank1:

Any code length.

Rank2:

Your code should be shorter than 100 characters.

Rank3:

Your code should be shorter than 70 characters.

How it is used:

This mission teaches you to work with simple data type conversions to solve a problem.
"""

# if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf(123405) == 120
#    assert golf(999) == 729
#    assert golf(1000) == 1
#    assert golf(1111) == 1
#    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")