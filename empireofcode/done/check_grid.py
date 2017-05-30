def check_grid(grid):
    for m in range(0, len(grid) - 1):
        if grid[m] == grid[m + 1]:
            return False
        else:
            m += 1
    for _ in grid:
        for i in range(0, len(_) - 1):
            if _[i] == _[i + 1]:
                return False
            else:
                i += 1
    return True
"""

Crystal Grid

An equal number of atoms, combined in the same way produce the same crystal forms, and the same crystal form does not 
depend on the nature of the atoms, but only on their number and mode of combination.

--Ellhard Mitscherlich

The initial crystal quality check phase (link) is not enough to satisfactorily pass a crystal for use. As such, we need 
to work to improve the process. Since we've checked random atomic lines/rows, perhaps it would be best to perform 
checks on random slices of the crystal. This crystal type contains two atoms composed of the elements "X" (Xenatom) 
and "Z" (Zorium). In a well grown crystal, these atoms should alternate down each row and column.

You are given a slice of crystal lattice as a grid (2D array) of the atoms "X" and "Z". A well grown grid should have 
proper periodic arrangements both horizontally and vertically. If one atom is found next to another atom of its 
element, the crystal is unusable. For example:

[["X", "Z"],
 ["Z", "X"]] is good

[["X", "Z", "X"],
 ["Z", "X", "Z"],
 ["X", "Z", "X"]] is good

[["X", "Z", "X"],
 ["Z", "Z", "Z"],
 ["X", "Z", "X"]] is bad
Input: Atomic grid as a list of lists with strings.

Output: The crystal quality as a boolean.

Example:

check_grid([["X", "Z"], ["Z", "X"]]) == True
check_grid([["X", "X"], ["X", "X"]]) == False
Precondition:

1 < |grid| ≤ 12

∀ row ∈ grid: 1 < |row| ≤ 12

All rows have the same length and contains only "X"/"Z"

How it is used:

In this mission we will use more complex structure as list of list. This structure often use as tables or grids or land maps.

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_grid([["X", "Z"], ["Z", "X"]]), "2x2 Good"
    assert check_grid([["X", "Z", "X"],
                       ["Z", "X", "Z"],
                       ["X", "Z", "X"]]), "3x3 Good"
    assert check_grid([["X", "Z", "X", "Z"],
                       ["Z", "X", "Z", "X"]]), "2x4 Good"
    assert not check_grid([["X", "X"],
                           ["X", "X"]]), "2x2 Bad"
    assert not check_grid([["X", "Z", "X"],
                           ["Z", "Z", "Z"],
                           ["X", "Z", "X"]]), "3x3 Bad"
    assert not check_grid([["X", "Z", "X", "Z"],
                           ["X", "Z", "X", "Z"]]), "2x4 Bad"

    print("Use 'Check' to earn sweet rewards!")
"""
print(check_grid([["X", "Z", "X", "Z"],
                           ["X", "Z", "X", "Z"]]))
