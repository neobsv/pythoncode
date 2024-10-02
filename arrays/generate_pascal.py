from typing import List

def generate(N: int) -> List[List[int]]:
	if N==0:
		return []
	if N==1:
		return [[1]]
	A = [[1], [1, 1]]
	for i in range(2, N):
		row = [1] + [ A[i-1][j] + A[i-1][j-1] for j in range(1, len(A[-1])) ] + [1]
		A.append(row)
	return A

if __name__ == '__main__':
	print(f'  pascal_triangle 3: {  generate(3) }  ')
	print(f'  pascal_triangle 3: {  generate(5) }  ')