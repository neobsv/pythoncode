from typing import List

def word_search(word: str, start: List[int], board: List[List[str]]) -> bool:
	"""
	check for the boundary conditions where the first char should equal word[0],
	and the cell should be within the boundary of the grid. Remove the letter from
	the board and move in four directions, and if any one of the four directions returns
	True its a True, otherwise it is False. Restore the letter that was removed.
	"""

	if  not ( ( start[0] >= 0 and start[0] < len(board) ) and ( start[1] >=0 and start[1] < len(board[0]) ) ):
		return False

	if word[0] != board[start[0]][start[1]]:
		return False

	if len(word) <= 1:
		return True

	moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
	applied_moves = [ [ start[0] + move[0], start[1] + move[1] ] for move in moves ]
	board[start[0]][start[1]] = ''
	for move in applied_moves:
		if word_search(word[1:], move, board):
			return True

	return False

def dfs(board: List[List[str]], word: str) -> bool:

	start_cells = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if word[0] == board[i][j]:
				start_cells.append([i, j])

	res = False
	for start in start_cells:
		res |= word_search(word, start, board)

	return res

if __name__ == '__main__':
	print(f"    dfs [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED': { dfs( [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED') }   ")
	print(f"    dfs [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE'   : { dfs( [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE') }   ")
	print(f"    dfs [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB'  : { dfs( [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB') }   ")
