 from typing import List

 def sortColors(nums: List[int]) -> List[int]:
    """
    Start with the color with the lowest hex, perform one pass
    where the numbers in the array are swapped if equal to the
    current hex; similar to insertion sort.

    Next, continue from that index till the end of the array,
    and do the same.
    """
    prev = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[prev], nums[i] = nums[i], nums[prev]
            prev += 1
    
    for i in range(prev, len(nums)):
        if nums[i] == 1:
            nums[prev], nums[i] = nums[i], nums[prev]
            prev += 1
    return nums

if __name__ == '__main__':
    print(f'   sort_colors : { sortColors([2,0,2,1,1,0]) }   ')