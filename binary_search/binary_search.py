from typing import List

def binary_search(nums: List[int], target: int) -> int:
    """
    Normal binary search.
    """
    if len(nums) == 0:
        return -1

    low = 0
    high = len(nums)-1
    
    while low<=high:
        mid = (low+high)//2

        if nums[mid] == target:
            return mid

        if nums[mid]<target:
            low = mid+1
        else:
            high = mid-1
    
    return low if low < len(nums) else -1

if __name__ == '__main__':
    print(f'binary_search []: { binary_search([], 0) }  ')
    print(f'binary_search [0]: { binary_search([0], 0) }  ')
    print(f'binary_search [0]: { binary_search([0], 7) }  ')
    print(f'binary_search [1, 5, 7, 11, 24, 37, 71, 72, 73, 74, 75, 76, 77, 77, 90, 92, 95, 101, 102 ], 7: { binary_search([1, 5, 7, 11, 24, 37, 81, 82, 83, 84, 85, 86, 87, 88, 90, 92, 95, 101, 102 ], 7) }  ')
    print(f'binary_search [1, 5, 7, 11, 24, 37, 71, 72, 73, 74, 75, 76, 77, 77, 90, 92, 95, 101, 102 ], 77: { binary_search([1, 5, 7, 11, 24, 37, 81, 82, 83, 84, 85, 86, 87, 88, 90, 92, 95, 101, 102 ], 77) }  ')