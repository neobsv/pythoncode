from typing import List

def rotate_image(matrix: List[List[int]]) -> List[List[int]]:
	"""
	1. Horizontal reflect the entire matrix i.e. rotate 180 degrees
	2. Transpose the matrix to rotate it -90 degrees
	"""
	matrix.reverse()
	for i in range(len(matrix)-1):
		for j in range(i+1, len(matrix)):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	return matrix

if __name__ == '__main__':
	print(f' rotate90 [[1,2,3],[4,5,6],[7,8,9]]: { rotate_image([[1,2,3],[4,5,6],[7,8,9]]) }  ')
	print(f' rotate90 [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]: { rotate_image([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) }  ')