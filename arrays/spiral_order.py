from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[List[int]]:
    if len(matrix) == 0:
        return []
    
    T = 0
    B = len(matrix) -1 #number of rows
    L = 0
    R = len(matrix[0]) - 1 #number of columns
    
    result_matrix = []
    direction = 0

    while (T<=B and L<=R):
        if (direction == 0):
            for i in range (L, R+1, 1):
                result_matrix.append(matrix[T][i])
            T+=1
        elif (direction == 1):
            for i in range (T, B+1, 1):
                result_matrix.append(matrix[i][R])
            R-=1
        elif (direction == 2):
            for i in range (R, L-1, -1):
                result_matrix.append(matrix[B][i])
            B-=1
        elif (direction == 3):
            for i in range (B, T-1, -1):
                result_matrix.append(matrix[i][L])
            L+=1
        direction = (direction+1)%4
    
    return result_matrix

if __name__ == '__main__':
    print(f'    spiral_order [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]: { spiralOrder([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]) }  ')