from typing import List

def isBipartite(graph: List[List[int]]) -> bool:
    """
    For each node, maintain a dictionary to record 1 / 0 based on if
    the node is not colored, and recurse to the next node with the opposite 
    color. The other case is, if the node is colored, then return True, if the
    color that it is supposed to be (input parameter) matches the color it actually
    is (visited set), otherwise return false because it is not possible to two color
    the graph completely.

    """
    def bipartComponent(v, color):
        # Base case:
        if v in colored:
            return True if colored[v] == color else False
        # Recursive case:  
        else:
            colored[v] = color
            for u in graph[v]:
                if not bipartComponent(u, not color):
                    return False
            return True

    colored = {} # Similar to visited set, but also has color information
    for v in range(len(graph)):
      if v not in colored and bipartComponent(v, True) == False:
            return False

    return True

if __name__ == '__main__':
    print(f" is_bipartite [[1, 3], [0, 2], [1, 3], [0, 2]] : { isBipartite( [[1, 3], [0, 2], [1, 3], [0, 2]] ) } ")
    print(f" is_bipartite [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]] : { isBipartite( [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]] ) } ")