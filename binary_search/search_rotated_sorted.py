from typing import List

def rotated_search(nums: List[int], target: int) -> int:
    """
    The only difference between normal search and this, is to
    check if the mid ptr is in the smaller or greater part of the
    array. Smaller part is indicated by nums[mid] <= nums[high]
    """
    low = 0
    high = len(nums)-1
    
    while (low <=high):
        mid = (low+high)//2
        
        if (nums[mid] == target):
            return mid
        
        if (nums[mid] <= nums[high]):
            """
            nums[mid] <= nums[high] detects the smaller part of the array
            [5, 6, 7, | 1 |, 2, 3, | 4 |]
            """
            if (target > nums[mid] and target <= nums[high]):
                low = mid + 1
            else:
                high = mid - 1
        else:
            if (target >= nums[low] and target < nums[mid]):
                high = mid - 1
            else:
                low = mid + 1
    
    return low if low < len(nums) else -1

if __name__ == '__main__':
    print(f' rotated_search [5, 6, 7, 1, 2, 3, 4], 3: { rotated_search([5, 6, 7, 1, 2, 3, 4], 3) } ')