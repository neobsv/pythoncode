from typing import List

def findMin(nums: List[int]) -> int:
    """
    find the break point in the array, i.e. min element after peak
    [ 4, 5, 6, 7,  |  1, 2, 3 ]
    """
    low = 0 
    high = len(nums) - 1 
    while low <= high:
        mid = (low + high) // 2 
        """
        if middle is > low and you are on the lowest element, right next to the peak.
        nums[mid] < nums[mid-1] only happens at the peak (mid-1).
        """
        if mid - 1 >= low and nums[mid] < nums[mid - 1]:
            return nums[mid]
        
        
        if nums[mid] < nums[low]:
            """
            <<--
            [ 6, 7, 1, | 2 |, 3, 4, 5 ]
            mid ptr is currently in lesser part, decrease search
            space from the right side of the array.
            """
            high = mid - 1
        elif nums[mid] > nums[high]:
            """
            -->>
            [ 4, 5, 6, | 7 |,  1, 2, 3 ]
            mid ptr is in the greater part, decrease search space
            from the left side of the array, to move toward the lesser part.
            """
            low = mid + 1
        elif low != high and nums[mid] == nums[low] == nums[high]:
            """
            move over the duplicates.
            """
            low += 1
        else:
            return nums[low]

if __name__ == '__main__':
    print(f'   findMin [4, 5, 6, 7, 7, 7, 7, 1, 2, 3]: { findMin([4, 5, 6, 7, 7, 7, 7, 1, 2, 3]) }   ')
    print(f'   findMin [6, 6, 6, 7, 1, 1, 1, 2, 2, 2, 2, 3, 4, 5]: { findMin([6, 6, 6, 7, 1, 1, 1, 2, 2, 2, 2, 3, 4, 5]) }   ')
