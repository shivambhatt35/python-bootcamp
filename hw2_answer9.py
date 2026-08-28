import numpy as np

def transpose_2d(arr):
    """This function takes a 2d array, arr, and returns the matrix transposed. (rows become columns and columns become rows)"""
    rows = len(arr)
    cols = len(arr[0])

    result = []
    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(arr[row][col])
        result.append(new_row)

    return result


original = [
    [1, 2, 3],
    [4, 5, 6]
]

for row in original:
    print(row)

transposed_array = transpose_2d(original)

for row in transposed_array:
    print(row)

for row in original:
    print(row)

