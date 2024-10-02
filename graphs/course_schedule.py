from collections import defaultdict
from typing import List, Dict


def canFinish(prerequisites: List[List[int]]) -> bool:
    """
    Graph 3 coloring:
    Initially all vertices are colored white, and the dfs begins, color the node grey and visit all its neighbors. If the node
    is grey and a loop or cycle exists in the graph, then we are bound to reach the same node again at the end of the loop (think of
    a node with a self-loop or as a part of a small triangle). Therefore, during the time we visit the neighbors of the graph, if we reach a
    grey colored node, then we return False. Once we are done visiting all neighbors, we mark the node black, and push it onto the stack.
    """
    def toposort(node: int, graph: Dict[int, int], stack: List[str], visited: Dict[int, str]):
        # In the process of visiting this vertex, we reach this
        # vertex again, so return False.
        if visited.get(node) == "g":
            return False
        
        # Finished visiting this vertex, so return.
        if visited.get(node) == "b":
            return True
        
        visited[node] = "g"
        # Visit all the neighbors in the graph, if we reach the 
        # same vertex again, return False.
        for neighbor in graph.get(node,[]):
            if not toposort(neighbor, graph, stack, visited):
                return False
        
        visited[node] = "b"
        stack.append(node)
        return True
    
    graph = defaultdict(list)
    stack = []
    visited = {}
    
    for (course, req) in prerequisites:
        graph[req].append(course)
    
    for node in graph:
        if not toposort(node, graph, stack, visited):
            return False
    
    return True


if __name__ == '__main__':
    print(f" canFinish [[1, 0]]: { canFinish([[1, 0]]) } ")
    print(f" canFinish [[1, 0],[0, 1]]: { canFinish([[1, 0],[0, 1]])  }  ")
