from typing import List

def missingNumber(nums: List[int]) -> int:
    """
    Using the property that the sum of the numbers upto n = n(n+1)/2,
    and using this to subtract the sum of the numbers in the array and
    and the mathematically calculated sum.
    """
    if len(nums) == 0:
        return 0
    
    sum_nums = sum(nums)
    
    s = 0
    n = nums[-1]
    
    s = (n*(n+1))//2
    
    return s - sum_nums

if __name__ == '__main__':
    print(f'    missing_number: { missingNumber([]) }    ')
    print(f'    missing_number: { missingNumber([0]) }    ')
    print(f'    missing_number: { missingNumber([1, 2, 4, 5, 6, 7]) }    ')
    print(f'    missing_number: { missingNumber([1, 2, 3, 4, 5, 6, 7, 9, 10]) }    ')