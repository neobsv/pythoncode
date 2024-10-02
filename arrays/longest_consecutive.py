from typing import List

def longestConsecutive(nums: List[int]) -> int:
    """
    Look at each number, check if n-1 is in the set, if not then iterate 
    from it till the largest sequence that it can produce. Return the largest 
    sequence that can be generated using all elements like this. 
    (no duplicates, no negatives).
    """
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best

if __name__ == '__main__':
    print(f' longest_consecutive []: { longestConsecutive([]) } ')
    print(f' longest_consecutive [0]: { longestConsecutive([0]) } ')
    print(f' longest_consecutive [1, 2, 3, 4]: { longestConsecutive([1, 2, 3, 4]) } ')
    print(f' longest_consecutive [1, 2, 3, 4, 7, 8, 9, 10, 11]: { longestConsecutive([1, 2, 3, 4, 7, 8, 9, 10, 11]) } ')