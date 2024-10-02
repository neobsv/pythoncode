from typing import List

def canJump(nums: List[int]) -> bool:
    """
    :type nums: List[int]
    :rtype: bool
    """
    index_c = 0
    for i, x in enumerate(nums):
        if i>index_c:
            """
            This means you've got stuck at index_c,
            and there is a zero at index i. return False
            """
            return False
        """
        Else, set  index_c to the sum of the current index 
        and the element at the index. If index_c is already at 
        a higher element, then don't reset it/ bring it back.
        """
        index_c = max(index_c, i+x)
    return True

if __name__ == '__main__':
    print(f' jump_game [2, 3, 1, 1, 4]: { canJump([2, 3, 1, 1, 4]) }  ')
    print(f' jump_game [3, 2, 1, 0, 4]: { canJump([3, 2, 1, 0, 4]) }  ')