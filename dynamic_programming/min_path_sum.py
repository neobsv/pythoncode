from typing import List

def min_path_sum(grid: List[List[int]]) -> int:
    """
    Regular 2D dp, look at the top cell and the left cell, and fill in
    the result T with the min of the two values. 
    """
    T = [ [ 0 for i in range(len(grid[0])) ] for j in range(len(grid)) ]

    for i in range(len(grid[0])):
        T[0][i] = T[0][i-1] + grid[i][0]

    for j in range(len(grid)):
        T[j][0] = T[j-1][0] + grid[0][j]

    T[0][0] = grid[0][0]

    for i in range(1, len(T)):
        for j in range(1, len(T[0])):
            T[i][j] += min(grid[i][j] + T[i-1][j], grid[i][j] + T[i][j-1])

    return T[-1][-1]

if __name__ == '__main__':
    print(f" min_path_sum [[1, 3, 1], [1, 5, 1], [4, 2, 1]]: { min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) } ")