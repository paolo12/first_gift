def hamming(n, m):
    n = list(bin(n))
    m = list(bin(m))
    i = k = 0
    while i < 2:
        del n[0]
        del m[0]
        i += 1
    if len(n) < len(m):
        while len(n) < len(m):
            n.insert(0, "0")
    elif len(n) > len(m):
        while len(n) > len(m):
            m.insert(0, "0")

    for i in range(0, len(n)):
        if n[i] != m[i]:
            k += 1
            i += 1
        else:
            i += 1
    return k


"""

Hamming Distance

The Hamming distance between two binary integers is the number of bit positions that differs ( read more about the
Hamming distance on Wikipedia). For example:

117 = 0 1 1 1 0 1 0 1
 17 = 0 0 0 1 0 0 0 1
  H = 0+1+1+0+0+1+0+0 = 3
You are given two positive numbers (N, M) in decimal form. You should calculate the Hamming distance between these
two numbers in binary form.

Input: Two arguments as integers.

Output: The Hamming distance as an integer.

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert hamming(117, 17) == 3, "First example"
    assert hamming(1, 2) == 2, "Second example"
    assert hamming(16, 15) == 5, "Third example"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
"""
hamming(16, 15)
