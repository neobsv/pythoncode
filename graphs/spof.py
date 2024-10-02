from collections import defaultdict
def singlePointOfFailure(connections) -> int:
    """
    - remove each edge from the graph, and see which disconnected
    edge leads to the graph having more than one cc.
    """
    graph = defaultdict(list)
    
    vertices = [ i for i in range(len(connections[0])) ]
    
    for i, row in enumerate(connections):
        for j, v in enumerate(row):
            if v == 1:
                graph[i].append(j)
    
    number_islands = 0
    ccs = set([])
    for v1 in graph.keys():
        for j, v2 in enumerate(graph.get(v1, [])):
            # print(f'v1: {v1} v2: {v2} graph: {graph}')
            r_v1 = graph[v1].pop(j)
            i = graph[r_v1].index(v1)
            r_v2 = graph[r_v1].pop(i)
            # print(f'mutate graph: {graph}')
            for start in graph.keys():
                stack, visited = [start], set([])
                res = []
                while len(stack) > 0:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        res.append(current)
                        for nbhr in graph.get(current, []):
                            if nbhr not in visited:
                                stack.append(nbhr)
                ccs.add(tuple( visited ))
                # print(f'ccs: {ccs}')
            number_islands = max(number_islands, len(ccs)//2)
            graph[v1].insert(j, r_v1)
            graph[r_v1].insert(i, r_v2)
            # print(f'restore graph: {graph}')
    
    return number_islands

if __name__ == '__main__':
    print(f" spof [[0, 1], [1, 0]] : { singlePointOfFailure( [[0, 1], [1, 0]] ) } ")
    print(f" spof [[0, 1, 1], [1, 0, 1], [1, 1, 0]] : { singlePointOfFailure( [[0, 1, 1], [1, 0, 1], [1, 1, 0]] ) } ")
    print(f" spof [[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]] : { singlePointOfFailure( [[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]] ) } ")
    print(f" spof [[0, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]] : { singlePointOfFailure( [[0, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]] ) } ")
