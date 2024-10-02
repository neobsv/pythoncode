from typing import List

def removeElement(nums: List[int], val: int) -> List[int]:
    """
    Use a prev pointer to hold the position of the index till which 'elements without val' 
    are present, then increment prev only if the current index is not 'val'. This ensures 
    that all elements till index 'prev' are 'solved' (have no val elements).
          prev     i
    1 2 3 4 |  4 5 | 6
    1 2 3 4 5 | 5 6 7 7 8

    """
    if len(nums) == 0:
        return 0
    
    # edge case, single element array
    if len(nums)==1: 
        if nums[0] != val:
            return 1
        else:
            return 0

    prev = 0
    for i in range(len(nums)):
        if (val != nums[i]):
            nums[prev] = nums[i]
            prev += 1
    return nums[:prev]

if __name__ == '__main__':
    print(f' remove_element [1, 3, 4, 2, 5, 5, 7]: { removeElement([], 4) }  ')
    print(f' remove_element [1, 3, 4, 2, 5, 5, 7]: { removeElement([1], 1) }  ')
    print(f' remove_element [1, 3, 4, 2, 5, 5, 7]: { removeElement([1], 4) }  ')
    print(f' remove_element [1, 3, 4, 2, 5, 5, 7]: { removeElement([1, 3, 4, 2, 5, 5, 7], 5) }  ')
    print(f' remove_element [1, 3, 4, 2, 5, 5, 7]: { removeElement([1, 3, 4, 2, 5, 5, 7], 4) }  ')