def flat_list(array):
    list_all = list()

    def i_is_list(inside_array):
        array_inside = inside_array
        for j in range(0, len(array_inside)):
            if type(array_inside[j]) is list:
                i_is_list(array_inside[j])
            else:
                list_all.append(array_inside[j])
            j += 1

    for i in range(0, len(array)):
        if type(array[i]) is not list:
            list_all.append(array[i])
        elif type(array[i]) is list:
            i_is_list(array[i])
        i += 1
    return list_all


"""
Flatten List

There is a list which contains integers or other nested lists which may contain yet more lists and integers which 
then… you get the idea. You should put all of the integer values into one flat list. The order should be as it was in 
the original list with string representation from left to right.

Input: A nested list with lists or integers.

Output: The one-dimensional list with integers. 
if __name__ == "__main__":
    assert flat_list([1, 2, 3]) == [1, 2, 3], "Flat"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "One"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Nested"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "In In"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
"""
print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
