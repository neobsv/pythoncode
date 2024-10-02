from typing import List

def wiggleSort(nums: List[int]) -> List[int]:
    """
    Modify nums in-place instead. 
    
    at even index: 
        swap if n[i]> n[i+1) 

    at odd index: 
        swap if n[i]<=n[i+1]
    
    You want smaller elements at even indices and larger 
    elements at odd indices.
    """
    for i in range(0, len(nums)-1):
        if (i % 2) ^ (nums[i] > nums[i+1]):
            nums[i], nums[i+1] = nums[i+1], nums[i]

    return nums

if __name__ == '__main__':
    print(f'   wiggle_sort [3, 5, 2, 1, 6, 4]: { wiggleSort([3, 5, 2, 1, 6, 4]) }   ')