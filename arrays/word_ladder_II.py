from collections import defaultdict
from collections import deque
from typing import List

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

    
    d = defaultdict(list)
    
    for w in wordList:
        for i in range(len(w)):
            nw = w[:i] + "*" + w[i + 1:]
            d[nw].append(w) 
    
  
    def neighbors(w):
        for i in range(len(w)):
            if (nw := w[:i] + "*" + w[i + 1:]) in d:
                yield from d[nw]    
    

    seen = set([])           
    q = deque([beginWord]) 
    res = [[beginWord]]
            
    while len(q) > 0:
        """
        maintain pattern while still recording all possible paths?
        there we go, now prune all the ones that don't start with begin word
        and end with end word.
        """
        # print(f' queue: {q} ')
        current = q.popleft()
        if current not in seen:
            seen.add(current)
            
            """
            if in the same loop, check for possible alternate paths by
            using length of the previous results, the fact that the current
            node MUST be the last node in the prev. results and the neighbor
            hasn't already been visited yet.
            """
            for nbhr in neighbors(current):
                if nbhr not in seen:
                    for rs in res:
                        if len(rs) > 0 and rs[-1] == current and nbhr not in rs:
                            res.append( rs + [nbhr] )
                            # print(f' res: {res} ')
                    q.append(nbhr)
            
            if current == endWord:
                break

    temp  = []
    min_len = 9999
    for i, r in enumerate(res):
        # print(f' result: {r} ')
        if len(r) > 0 and r[-1] == endWord:
            temp.append(r)
            min_len = min(min_len, len(r))

    new_res = []
    for r in temp:
        if len(r) == min_len:
            new_res.append(r)

    return new_res

if __name__ == '__main__':
    print(f"   findLadders hit, cog, [hot,dot,dog,lot,log,cog] : { findLadders('hit', 'cog', ['hot','dot','dog','lot','log','cog'])  }   ")
    print(f"   findLadders hit, cog, [hot,dot,dog,lot,log,cog] : { findLadders('hit', 'cog', ['hot','dot','log','cog'])  }   ")
