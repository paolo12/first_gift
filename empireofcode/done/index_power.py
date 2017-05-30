def index_power(array, n):
    if len(array) > n:
        return array[n] ** n
    elif len(array) < n:
        return -1
    else:
        return -1

"""
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert  == -1, "IndexError"

    print("Use 'Check' to earn sweet rewards!")
    line = [1, 2, 3, 4]
    print(type(line))
    n = 2
    if len(line) > n:
    print(line[n] ** n)
    else:
    print("0")
"""
print(index_power([1, 2, 3, 4], 2))