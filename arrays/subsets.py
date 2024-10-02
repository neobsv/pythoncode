from typing import List

def generate_subsets(nums: List[int]) -> List[List[int]]:
    if len(nums)==0:
        return [[]]
    first, rem = nums[0], generate_subsets(nums[1:])
    return [ [first] + subset for subset in rem  ] + rem

if __name__ == '__main__':
    print(f"   generate_subsets []: { generate_subsets([]) }   ")
    print(f"   generate_subsets [1]: { generate_subsets([1]) }   ")
    print(f"   generate_subsets [3, 1, 4, 2, 7]: { generate_subsets([3, 1, 4, 2, 7]) }   ")
    print(f"   generate_subsets [1, 1, 3, 7, 2]: { generate_subsets([1, 1, 3, 7, 2]) }   ")
