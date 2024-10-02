from typing import List

def majorityElement(nums: List[int]) -> int:
    """
    :type nums: List[int]
    :rtype: int

   The character count keeps track of how many times the majority 
   Element repeats itself.

   The count is decreased when an element different from maj_element 
   is found, therefore even if we are counting the wrong character, 
   its count will hit zero.

   When the count hits zero, we replace the character with the 
   Char at the current index. This way we are guaranteed that the
   majority element will be the one with the highest count and 
   will be locked onto, since the probability of hitting the 
   majority element over any other element when the count drops to 
   Zero is over 50% compared to the 1/n probability for all others.
   
   """
    maj_element = 0
    count = 0
    i=0
    while i<len(nums):
        if maj_element==nums[i]:
            count += 1
        elif count==0:
            maj_element = nums[i]
        else: 
            count -= 1
        i+=1
    return maj_element

if __name__ == '__main__':
    print(f'  maj_element ["a", "b", "a", "a", "x", "x", "y", "a", "1", "a", "a", "a", "a", "a"]: { majorityElement(["a", "b", "a", "a", "x", "x", "y", "a", "1", "a", "a", "a", "a", "a"]) }  ')
    print(f'  maj_element ["x", "x", "x", "y", "x", "1"]: { majorityElement(["x", "x", "x", "y", "x", "1"]) }  ')