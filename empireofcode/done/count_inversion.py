def count_inversion(sequence):
    sequence = list(sequence)
    i = 1
    n = 0
    while i < len(sequence):
        if sequence[i - 1] <= sequence[i]:
            i += 1
        else:
            tmp = sequence[i]
            sequence[i] = sequence[i - 1]
            sequence[i - 1] = tmp
            i -= 1
            if i == 0:
                i = 1
            n += 1
    return n

"""
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
"""

print(count_inversion((5, 3, 2, 1, 0)))