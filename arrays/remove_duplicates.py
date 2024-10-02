from typing import List

def removeDuplicates(nums: List[int]) -> List[int]:
    """
    Use a prev pointer to hold the position of the index till which no duplicates 
    are present, then increment prev only if the current index is not a duplicate. 
    This ensures that all elements till index ‘prev’ are ‘solved’ (de-duplicated).
    """
    if len(nums) == 0:
        return -1
    
    prev = 0
    for i in range (1, len(nums)):
        if (nums[prev] != nums[i]):
            prev += 1
            nums[prev] = nums[i]
            
    return nums[:prev+1]

if __name__ == '__main__':
    print(f'remove_duplicates [1, 1, 2]: { removeDuplicates( [1, 1, 2] ) } ')
    print(f'remove_duplicates [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]: { removeDuplicates( [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] ) } ')