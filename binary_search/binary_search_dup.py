from typing import List

def binary_search_low(nums: List[int], target: int) -> int:
    """
    Normal binary search, modified to find the lowest index of the target
    element in a list containing duplicates.
    """
    if len(nums) == 0:
        return -1

    low = 0
    high = len(nums)-1
    
    while low<=high:
        mid = (low+high)//2

        if nums[mid] == target:
            while mid - 1 >= 0 and nums[mid] == nums[mid-1]:
                mid -= 1
            return mid

        if nums[mid]<target:
            low = mid+1
        else:
            high = mid-1
    
    return low if low < len(nums) else -1


def binary_search_high(nums: List[int], target: int) -> int:
    """
    Normal binary search, modified to find the highest index of the target
    element in a list containing duplicates.
    """
    if len(nums) == 0:
        return -1

    low = 0
    high = len(nums)-1
    
    while low<=high:
        mid = (low+high)//2

        if nums[mid] == target:
            while mid + 1 < len(nums) and nums[mid] == nums[mid+1]:
                mid += 1
            return mid

        if nums[mid]<target:
            low = mid+1
        else:
            high = mid-1
    
    return low if low < len(nums) else -1
            
def searchRange(nums: List[int], target: int) -> List[int]:
    """
    Binary search for a target element in a List containing duplicates.
    """
    lower = binary_search_low(nums, target)
    higher = binary_search_high(nums, target)
    return [lower, higher]

if __name__ == '__main__':
    print(f' searchRange [], 4: { searchRange([], 4)  } ')
    print(f' searchRange [0], 4: { searchRange([0], 4)  } ')
    print(f' searchRange [0], 0: { searchRange([0], 0) }  ')
    print(f' searchRange [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11], 4: { searchRange([1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11], 4)  } ')
    print(f' searchRange [1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11], 3: { searchRange([1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11], 3)  } ')





