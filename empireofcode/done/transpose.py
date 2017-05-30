def transpose(data):
    a = len(data)
    b = len(data[0])

    transposed = [None]*b

    for i in range(0, b):
        transposed[i] = [None]*a

    for i in range(b):
        for j in range(a):
            transposed[i][j] = data[j][i]
    return transposed

"""
Transpose Matrix

Sometimes it's useful to look at world from another perspective.

In linear algebra, the transpose of a matrix A is another matrix AT (also written A′, Atr,tA or At) created by any one 
of the following equivalent actions:

reflect A over its main diagonal (which runs from top-left to bottom-right) to obtain AT
write the rows of A as the columns of AT
write the columns of A as the rows of AT
Formally, the i row, j column element of AT is the j row, i column element of A:

[AT]i j = [A]j i

If A is an m × n matrix then AT is an n × m matrix.

You have been given a matrix as a 2D list with integers. Your task is to return a transposed matrix based on input.

|1 2 3|   |1 4 7|
|4 5 6| T |2 5 8|
|7 8 9|   |3 6 9|

|1 4 3|
|8 2 6|   |1 8 7 4 7|
|7 8 3| T |4 2 8 9 8|
|4 6 9|   |3 6 3 6 1|
|7 8 1|
Input: A matrix as a list of lists with integers.

Output: The transposed matrix as a list of lists with integers.

Example:

transpose([[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]) == [[1, 4, 7],
                     [2, 5, 8],
                     [3, 6, 9]]
transpose([[1, 4, 3],
     [8, 2, 6],
     [7, 8, 3],
     [4, 9, 6],
     [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                     [4, 2, 8, 9, 8],
                     [3, 6, 3, 6, 1]]
Precondition:

0 < |matrix| < 10

∀ row ∈ matrix: 0 < |row| < 10

How it is used:

The most obvious use for this idea is in mathematical software, but the concept can be applied in the area of vector 
graphics. On a computer, one can often avoid explicitly transposing a matrix in memory by simply accessing the same 
data in a different order.


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert transpose([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]) == [[1, 4, 7],
                                      [2, 5, 8],
                                      [3, 6, 9]], "Square matrix"
    assert transpose([[1, 4, 3],
                      [8, 2, 6],
                      [7, 8, 3],
                      [4, 9, 6],
                      [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                      [4, 2, 8, 9, 8],
                                      [3, 6, 3, 6, 1]], "Rectangle matrix"

    print("Use 'Check' to earn sweet rewards!")
"""
print(transpose([[1, 4, 3], [8, 2, 6], [7, 8, 3], [4, 9, 6], [7, 8, 1]]))
