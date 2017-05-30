def rotate_list(elements, rotates):
    while rotates > 0:
        e = elements[0]
        elements.pop(0)
        elements.insert(len(elements), e)
        rotates -= 1
    return elements


"""
if __name__ == '__main__':
    assert rotate_list([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2], "First"
    assert rotate_list([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6, 1, 2, 3], "Second"
    assert rotate_list([1, 2, 3, 4, 5, 6], 0) == [1, 2, 3, 4, 5, 6], "Third"

    print("All set? Click \"Check\" to review your code and earn rewards!")
"""

print(rotate_list([1, 2, 3, 4, 5, 6], 2))
