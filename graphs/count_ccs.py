from typing import List, Set

def dfs(startx: int, starty: int, grid: List[List[int]], visited: Set[object], allowed: Set[object]):
    stack = [(startx, starty)]
    while len(stack) > 0:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            for move in [ ( current[0] + 1, current[1] ), ( current[0], current[1] + 1 ), ( current[0] - 1, current[1] ), ( current[0], current[1] - 1 )  ]:
                if ( move not in visited ) and ( move in allowed ) and ( grid[move[0]][move[1]] != '0' ):
                    stack.append(move)
    

def countClouds(skyMap) -> int:
    
    start_cells = set([])
    allowed = set([])
    for i in range(len(skyMap)):
        for j in range(len(skyMap[0])):
            if skyMap[i][j] == '1':
                start_cells.add((i, j))
            allowed.add((i, j))
    
    ccs = 0
    visited = set([])
    for cell in start_cells:
        if cell not in visited:
            dfs(cell[0], cell[1], skyMap, visited, allowed)
            ccs += 1
    
    return ccs

if __name__ == '__main__':
    print(f" countClouds [['0', '1', '1', '0', '1'], ['0', '1', '1', '1', '1'], ['0', '0', '0', '0', '1'], ['1', '0', '0', '1', '1']]: { countClouds([['0', '1', '1', '0', '1'], ['0', '1', '1', '1', '1'], ['0', '0', '0', '0', '1'], ['1', '0', '0', '1', '1']])  } ")