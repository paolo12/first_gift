def check_line(line):
    if len(line) == 2:
        if line[0] != line[1]:
            n = True
        else:
            return False
    else:
        for i in range(1, len(line) - 1):
            while i < len(line) - 1:
                if line[i] != line[i - 1] and line[i] != line[i + 1]:
                    n = True
                else:
                    return False
                i += 1
    return n
"""
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_line(["X", "Z", "X"]) == True
    assert check_line(["X", "Z", "X", "X"]) == False
    assert check_line(["X", "Z"]) == True
    assert check_line(["Z", "X"]) == True
    assert check_line(["Z", "X", "Z", "X", "Z", "Z", "X"]) == False

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
"""
print(check_line(["X", "Z", "X"]))