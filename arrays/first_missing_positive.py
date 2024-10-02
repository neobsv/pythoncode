from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    """
    Iterate from 1...max(nums), through the entire range of numbers that 
    the array should hold, and check if each one is present. If not, then 
    return the missing one.  If all are present return n+1. (This only works if 
    the array is continuous, fixed size, no duplicates)
    """
    if not nums:
        return 1
    
    if len(nums) == 1 and (0 in nums):
        return 1
    
    nums = set(nums)
    n = 1
    while n<max(nums):
        if not (n in nums):
            return n
        n = n + 1
    return n+1

if __name__ == '__main__':
    print(f'   first_missing_positive [] : { firstMissingPositive([]) } ')
    print(f'   first_missing_positive [0]: { firstMissingPositive([0]) } ')
    print(f'   first_missing_positive [1, 3, 4, 5, 6]: { firstMissingPositive([1, 3, 4, 5, 6]) } ')
    print(f'   first_missing_positive [3, 4, 5] : { firstMissingPositive([3, 4, 5]) } ')
