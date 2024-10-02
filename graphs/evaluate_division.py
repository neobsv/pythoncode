from collections import defaultdict
from typing import List

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    """
    For each node ; value pair given, prepare a graph with the forward
    edge representing the value v of moving from currency A -> B and the
    converse moving from B -> A would have a weight of 1/v
    """
    def dfs_path(graph: List[List[int]], start: str, end: str):
        
        if (start not in graph) or (end not in graph):
            return -1.0
        
        
        stack = [(start, [1.0])]
        visited = {}
        
        for n in graph.keys():
            visited[n] = 0
        
        while stack:
            vertex, path = stack.pop()
            
            if vertex == end:
                return path[-1]
            
            if not visited[vertex]:
                visited[vertex] = 1
                for n, v in graph[vertex]:
                    stack.append((n, path + [path[-1]*v]))
        
        return -1.0
          
    graph = defaultdict(list)
    
    for e, v in zip (equations, values):
        graph[e[0]].append([e[1], v])
        graph[e[1]].append([e[0], 1.0/v])
    
    result = []
    for query in queries:
        result.append(dfs_path(graph, query[0], query[1]))
    
    return result

if __name__ == '__main__':
    print(f" evaluate_division equations = [ ['a', 'b'], ['b', 'c'] ], values = [2.0, 3.0], queries = [ ['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x'] ] : { calcEquation([ ['a', 'b'], ['b', 'c'] ], [2.0, 3.0], [ ['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x'] ]) } ")

