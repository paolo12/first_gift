import math


def simple_areas(*args):
    a = list(args)
    print("a =", a)
    if len(a) == 1:
        return (math.pi * a[0] ** 2) / 4
    elif len(a) == 2:
        return a[0] * a[1]
    elif len(a) == 3:
        p = (a[0] + a[1] + a[2]) / 2
        return math.sqrt(p * (p - a[0]) * (p - a[1]) * (p - a[2]))

"""
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"

    print("Earn cool rewards by using the 'Check' button!")
"""
print(simple_areas(2, 3))