def swap_sort(array):
    return ""

"""

Robot Sort

All of the refined ingots should be sorted by size in each lot while passing by on a conveyor. Because the conveyor is 
already running, our robots needs to quickly swap neighboring ingots.

You are given the size and initial order of the ingots as an array of numbers. Indexes are their position, values are 
their sizes. You should order this array from the smallest to the largest in size.

For each action a Robot can swap two neighboring elements. Each action should be represented as a string with two 
digits - indexes of the swapped elements (ex, "01" - swap 0th and 1st ingots). The result should be represented as a 
string that contains the sequence of actions separated by commas. If the array does not require sorting, then return 
an empty string.

And you can swap only N*(N-1)/2 times, where N - is a quantity of ingots.

Initial   6 ============
position  4   ======== 
          2     ====

Swap      4   ========
0 - 1     6 ============ 
          2     ====
          
Swap      4   ========
1 - 2     2     ==== 
          6 ============
          
Swap      2     ====
0 - 1     4   ======== 
          6 ============
Input: An array as a tuple of integers.

Output: The sequence of actions as a string.

Example:

swap_sort((6, 4, 2)) == "01,12,01"
swap_sort((1, 2, 3, 4, 5)) == ""
swap_sort((1, 2, 3, 5, 3)) == "43"
Precondition:

1 ≤ |array| ≤ 10

How it is used:

This mission will show you how to work the simplest sorting algorithms. It also models one of the game mechanics in the 
classic puzzle game "Tetris Attack".

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_solution(f, indata):
        result = f(indata)
        array = list(indata[:])
        la = len(array)
        if not isinstance(result, str):
            print("The result should be a string")
            return False
        actions = result.split(",") if result else []
        for act in actions:
            if len(act) != 2 or not act.isdigit():
                print("The wrong action: {}".format(act))
                return False
            i, j = int(act[0]), int(act[1])
            if i >= la or j >= la:
                print("Index error: {}".format(act))
                return False
            if abs(i - j) != 1:
                print("The wrong action: {}".format(act))
                return False
            array[i], array[j] = array[j], array[i]
        if len(actions) > (la * (la - 1)) // 2:
            print("Too many actions. BOOM!")
            return False
        if array != sorted(indata):
            print("The array is not sorted. BOOM!")
            return False
        return True

    assert check_solution(swap_sort, (6, 4, 2)), "Reverse simple"
    assert check_solution(swap_sort, (1, 2, 3, 4, 5)), "All right!"
    assert check_solution(swap_sort, (1, 2, 3, 5, 3)), "One move"

    print("Earn cool rewards by using the 'Check' button!")
"""
print(swap_sort(6, 4, 2))