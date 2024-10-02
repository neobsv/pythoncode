from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    A[i] + A[j] = target
    A[i] = target - A[j]
    Store target - A[j] in a hashmap as keys with the associated 
    Index (j) as a value, and if we hit the same number again for 
    some A[i], then we will be able to produce the index j, such 
    that A[i] + A[j] = target.

    """
    hash_r  = {}
    for i in range(len(nums)):
        if not nums[i] in hash_r:
            hash_r[target-nums[i]] =  i
        else:
            other = hash_r[nums[i]]
            return [ other, i ]

if __name__ == '__main__':
    print(f' Two Sum: {twoSum([1, 4, 7, 2, 3, 5, 11], 13)} ')