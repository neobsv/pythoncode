from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Sort each word in the list of strings provided, and
    """
    hashr = defaultdict(list)
    for w in strs:
        temp = tuple(sorted([ c for c in w ]))
        hashr[temp].append(w)
    
    res = []
    for x in hashr.values():
        res.append(x)
    
    return res

if __name__ == '__main__':
    print(f'   groupAnagrams ["eat", "tea", "tan", "ate", "nat", "bat"]: { groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) }  ')