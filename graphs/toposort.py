from collections import defaultdict
from typing import List, Dict

def toposort(node: int, graph: List[List[int]], stack: List[int], visited: Dict[int, str]) -> bool:
    """
    - grey: in process of visiting, return false
    - black: finished visiting so return true
    """
    if visited.get(node, "") == "w":
        return False
    
    if visited.get(node, "") == "b":
        return True
    
    # start visiting the node, mark it grey
    visited[node] = "w"
    
    # print(f'before visit: {visited}')
    
    """
    - start visiting all the nodes, and if one of them hits a grey
    vertex, then return False due to a collision
    """
    for nbhr in graph.get(node, []):
        if not toposort(nbhr, graph, stack, visited):
            return False
    
    # finish visiting the node, mark it black
    visited[node] = "b"
    # print(f'after visit: {visited}')
    stack.append(node)
    return True

def hasDeadlock(connections: List[List[int]]) -> bool:
    graph = defaultdict(list)    
    for i, v in enumerate(connections):
        # print(f'index: {i} element: {v}')
        for vertex in v:
            graph[i].append(vertex)
    
    # print(f'{graph}')
    visited, stack = {}, []
    for node in graph.keys():
        if not toposort(node, graph, stack, visited):
            return True
    
    return False

if __name__ == '__main__':
    print(f" toposort [[1], [2], [3, 4], [4], [0]]: { hasDeadlock( [[1], [2], [3, 4], [4], [0]] ) } ")
    print(f" toposort [[1, 2, 3], [2, 3], [3], []]: { hasDeadlock( [[1, 2, 3], [2, 3], [3], []] ) } ")
    print(f" toposort [[2, 3, 5], [0, 2, 5, 4, 3], [3], [5], [3, 5], []]: { hasDeadlock( [[2, 3, 5], [0, 2, 5, 4, 3], [3], [5], [3, 5], []] ) } ")
