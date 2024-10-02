from typing import List

def set_zeroes(matrix: List[List[int]]) -> List[List[int]]:
    """
    Use two separate lists to record the rows and cols where you encounter
    zeros. Next, iterate over the lists and use them to set the corresponding
    rows and cols to zero.
    """
    rlen = len(matrix[0])
    clen = len(matrix)
    rows_zero = []
    cols_zero = []

    for i in range(clen):
        for j in range(rlen):
            if matrix[i][j] == 0:
                rows_zero.append(i)
                cols_zero.append(j)

    for r in rows_zero:
        matrix[r] = [0]*rlen


    for c in cols_zero:
        for i in range(clen):
            matrix[i][c] = 0

    return matrix

if __name__ == '__main__':
    print(f"  set_zeroes [[1, 0, 1], [1, 1, 1], [1, 1, 1]]: { set_zeroes([[1, 0, 1], [1, 1, 1], [1, 1, 1]]) }   ")
    print(f"  set_zeroes [[1, 1, 1], [0, 1, 1], [1, 1, 1]]: { set_zeroes([[1, 1, 1], [0, 1, 1], [1, 1, 1]]) }   ")