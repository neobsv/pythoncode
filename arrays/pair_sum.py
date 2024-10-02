from typing import List

def arrayPairSum(nums: List[int]) -> int:
    """

    Sort the array. Sum the even indexed elements (::n is 
    extended slicing notation in python, which skips over ‘n’ 
    elements each) since the max element of each pair of indices in
    A sorted array are the even indexed elements.
    """
    return sum(sorted(nums)[::2])

if __name__ == '__main__':
    print(f' array pair sum: {arrayPairSum([1, 2, 3, 4, 5, 6, 7])} ')
