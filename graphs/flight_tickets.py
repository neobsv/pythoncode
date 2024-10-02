from typing import List

def findItinerary(tickets: List[List[str]]) -> List[str]:
    """
    Sorting it in such a way that the larger from airport is at the begining. Sort in such a way that if the 
    from airports are the same, then, the to airports are sorted from larger to smaller.
    This ensures that as the graph is populated, the smallest to airport gets appended to the end of the target list.

    Do a dfs starting from JFK, which will take you to the smallest to airport in the JFK list. Next,  
    starting from the "smallest-JFK-to-airport" go to its smallest to airport. Then follow this pattern till no airports remain.
    Popping the smallest-to-airport from targets each time we append it to the stack ensures that we get an eulerian path, why?
    Because we ensure that once we visit this edge, we can no longer visit it again.
    This means that we will not have back edges in our dfs graph.

    """
    targets = collections.defaultdict(list)

    for a, b in sorted(tickets)[::-1]:
        targets[a].append(b)

    route, stack = [], ['JFK']
    while stack:
        while targets[stack[-1]]:
            stack.append(targets[stack[-1]].pop())
        route.append(stack.pop())

    return route[::-1]

if __name__ == '__main__':
    print(f" find_itinerary [['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]: { findItinerary( [['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']] ) } ")
    print(f" find_itinerary [['JFK','SFO'],['JFK','ATL'],['SFO','ATL'],['ATL','JFK'],['ATL','SFO']]: { findItinerary( [['JFK','SFO'],['JFK','ATL'],['SFO','ATL'],['ATL','JFK'],['ATL','SFO']] ) } ")