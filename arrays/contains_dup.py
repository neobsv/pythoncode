from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    """
    Sort the numbers, hold a variable prev, check if it collides with nums[i].
    """
    if len(nums) <= 1:
        return False
    
    nums.sort()

    prev = nums[0]
    for i in range(1, len(nums)):
        if (prev == nums[i]):
            return True
        else:
            prev = nums[i]
    return False

if __name__ == '__main__':
    print(f'  contains_duplicate []: { containsDuplicate([]) }  ')
    print(f'  contains_duplicate [1]: { containsDuplicate([1]) }  ')
    print(f'  contains_duplicate [1, 2, 3, 1]: { containsDuplicate([1, 2, 3, 1]) }  ')
    print(f'  contains_duplicate [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]: { containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) }   ')