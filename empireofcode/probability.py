def probability(marbles, step):
    return 0.50

"""

Pearl Box

Story

Let's play with pearls. To start the game, robots put several black and white pearls in one of the boxes. For each move,
the robots take a pearl out of the box and put one of the opposite color back. The winner is the one who pulls the white
pearl on the Nth step.

Our robots don't like indeterminacy and want to know the probability of a white pearl on the Nth step. The probability 
is a value between 0 (0% chance or will not happen) and 1 (100% chance or will happen). The result is a float from 0 to 
1 with two digits precision (±0.01).

You are given a start set of pearls as a string that contains "b" (black) and "w" (white) and the number of the step 
(N). The order of the pearls does not matter.

Input: The start sequence of the pearls as a string and the step number as an integer.

Output: The probability for a white pearl as a number.

Example:

probability('bbw', 3) == 0.48
probability('wwb', 3) == 0.52
probability('www', 3) == 0.56
probability('bbbb', 1) == 0
probability('wwbb', 4) == 0.5
probability('bwbwbwb', 5) == 0.48
Precondition:

0 < N ≤ 20

0 < |pearls| ≤ 20

How it is used:

This task introduces you to the basics of probability theory and statistics. Fun fact: regardless of the initial state, 
as the number of steps increases, the probability approaches 0.5!

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(probability('bbw', 3), 0.48), "1st example"
    assert almost_equal(probability('wwb', 3), 0.52), "2nd example"
    assert almost_equal(probability('www', 3), 0.56), "3rd example"
    assert almost_equal(probability('bbbb', 1), 0), "4th example"
    assert almost_equal(probability('wwbb', 4), 0.5), "5th example"
    assert almost_equal(probability('bwbwbwb', 5), 0.48), "6th example"

    print("All done? Earn rewards by using the 'Check' button!")
"""

