from collections import defaultdict
from typing import List, Dict

def validTree(edges: List[List[int]] ) -> bool:
    """
    check 2 things:
    1. is it cyclic? No, continue to step 2, else cannot be a tree
    2. Is every node reachable?
    """
    def isCyclicUtil(v: int, visited: Dict[int, bool], parent: int) -> bool:
        # Mark current node as visited
        visited.add(v)

        for nbhr in graph[v]:
            # if adj is not visited, recur, pass the current vertex
            # and the predecessor (parent) to that vertex
            if nbhr not in visited:
                if isCyclicUtil(nbhr, visited, v) == True:
                    return True
            # If an adjacent is visited and not parent of current 
            # vertex, then there  is a cycle.
            elif nbhr != parent:
                return True
        return False

    graph = defaultdict(list)
    visited = set([])

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # check for cycles
    if isCyclicUtil(0, visited, -1) == True:
        return False

    return len(visited) == len(graph.keys())

if __name__ == '__main__':
    print(f" valid_tree [[0, 1], [0, 2], [0, 3], [1, 4]]: {  validTree([[0, 1], [0, 2], [0, 3], [1, 4]]) }  ")
    print(f" valid_tree [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]: {  validTree([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) }  ")