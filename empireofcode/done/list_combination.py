def list_combination(list1, list2):
    list3 = list()
    for i in range(0, len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
        i += 1
    return list3
"""
if __name__ == '__main__':
    assert list_combination([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6], "First"
    assert list_combination([1, 1, 1, 1], [2, 2, 2, 2]) == [1, 2, 1, 2, 1, 2, 1, 2], "Second"

    print("All set? Click \"Check\" to review your code and earn rewards!")
"""
print(list_combination([1, 1, 1, 1], [2, 2, 2, 2]))
