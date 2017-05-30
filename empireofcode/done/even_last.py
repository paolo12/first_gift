def even_last(array):
    summ_array = []
    i = 0
    if len(array) == 0:
        return 0
    else:
        while (i <= len(array)-1) and (len(summ_array) < len(array)):
            summ_array.append(array[i])
            print("summ_array = ", summ_array)
            if i + 1 <= len(array):
                i += 2
            else:
                continue
        result = sum(summ_array) * array[-1]
        return result


"""
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert even_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_last([6]) == 36, "(6)*6=36"
    assert even_last([]) == 0, "An empty array = 0"

    print("Use 'Check' to earn sweet rewards!")
"""

print(even_last([]))
