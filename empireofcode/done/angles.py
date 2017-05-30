import math


def angles(a, b, c):
    line = list()
    if a + b > c and a + c > b and b + c > a:
        al = round(math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))))
        be = round(math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))))
        ce = round(math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))))
    else:
        al = 0
        be = 0
        ce = 0

    line.append(al)
    line.append(be)
    line.append(ce)
    line.sort()

    return line


"""
You are given the lengths for each side of a triangle. You need to find all three of the angles for this triangle. 
If the given side lengths cannot form a triangle (or form a degenerated triangle), then you must return all angles
as 0 (zero). The angles should be represented as a list of integers in ascending order. Each angle is measured in 
degrees and rounded to the nearest integer number using standard mathematical rounding.

Input: The lengths of the sides of a triangle as integers.

Output: Angles of a triangle in degrees as sorted list of integers.

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

"""

angles(7, 5, 5)
