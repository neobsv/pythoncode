from collections import defaultdict
from typing import List

def networkDelayTime(times: List[List[int]], N: int, K: int) -> int:
    """
    This is Dijikstra.
    """
 
    graph = defaultdict(list)
    for u,v,w in times:
        graph[u].append([v,w])
    
    node_delay = { K : 0 }
    queue = [ K ]
    while queue:
        node = queue.pop(0)
        for n in graph[node]:
            neighbor, latency = n[0], n[1]
            delay = latency + node_delay[node]
            if neighbor not in node_delay or delay < node_delay[neighbor]:
                node_delay[neighbor] = delay
                queue.append(neighbor)

    return max(node_delay.values()) if len(node_delay.keys()) == N else -1

if __name__ == '__main__':
    print(f" network_delay_time [[2, 1, 1],[2, 3, 1],[3, 4, 1]], 4, 2 : { networkDelayTime([[2, 1, 1],[2, 3, 1],[3, 4, 1]], 4, 2) } ")
    print(f" network_delay_time [[1, 2, 1]], 2, 1 : { networkDelayTime([[1, 2, 1]], 2, 1) } ")
    print(f" network_delay_time [[1, 2, 1]], 2, 2 : { networkDelayTime([[1, 2, 1]], 2, 2) } ")