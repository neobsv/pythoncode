from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    """
    Check if the abs. value of the difference between the two indices is 
    less than or equal to k, using a hashmap, and immediately and return true 
    if such a combination is found.
    """
    elements = {}
    for i in range (len(nums)):
        if nums[i] in elements and abs(i - elements[nums[i]]) <= k:
            return True
        elements[nums[i]] = i
    return False

if __name__ == '__main__':
    print(f' contains_nearby_duplicate [1,2,3,1], 3: { containsNearbyDuplicate([1,2,3,1], 3) }  ')
    print(f' contains_nearby_duplicate [1,2,3,1,2,3], 2: { containsNearbyDuplicate([1,2,3,1,2,3], 2) }  ')