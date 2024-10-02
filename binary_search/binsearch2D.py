from typing import List

def binsearch2D(matrix: List[List[int]], target: int) -> int:
    """
    In a matrix, the indices can be flattened from
    2D to 1D by setting:

    low = 0
    high = numRows*numCols - 1
    
    then mid = (low+high)//2 like normal.

    The corresponding element in the matrix can then
    be located by converting the 1D index to 2D again:

    row = (1D index) / numRows
    col = (1D index) % numCols

    """
    n = len(matrix[0])
    m = len(matrix)
    low = 0
    high = (n*m) - 1

    while low <= high:
        mid = (low + high)//2
        r = mid // m
        c = mid % n
        elem = matrix[r][c]
        if elem < target:
            low = mid + 1
        elif elem > target:
            high = mid - 1
        else:
            return mid
    return low

if __name__ == '__main__':
    print(f' binsearch2D  [[1, 3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]], 7: { binsearch2D([[1, 3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]], 7) }  ')
    print(f' binsearch2D  [[1, 3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]], 11: { binsearch2D([[1, 3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]], 11) }  ')