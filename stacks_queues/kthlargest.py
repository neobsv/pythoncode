from typing import List

def quickselect(nums: List[int], k: int) -> int:
    """
    the quickselect algorithm enables you to determine
    the kth largest / smallest element in a list without
    having to sort the entire list.

    :param nums: list of numbers to be sorted
    :param k: integer which denotes k
    :returns: The kth largest element

    """
    """

        First we pick the pivot element (ideally at random but we use mid here), 
        the left half of the list will be less than this element and the right
        half will be greater.

        [ 5, 7, 1, 3, 2, 6, 4 ]

        move the pivot element to the last position, and use its value to run the
        partition.
        [ 5, 7, 1, 2, 6, 4 ] 3

        1st swap: 1, 7, 5, 2 ...
        2nd swap: 1, 2, 5, 7 ...
        ...

        pivot is 3, and place two pointers at the begining of the list, now move
        the second pointer (j) till the n-1th element, and move the first pointer (i)
        only when the current ith element is less than the pivot element.

        [  1, 2, | 5,  7 |  6, ...  ] 3
                 |       |
                 i=2     |
                         j --> loop terminates when j reaches the end,
                         no more swaps now because all elements on the right
                         side of 'i' are now greater than the pivot element. 


    after this, we now need to check if 'i' == k, if so we are at the right place
    to select the element, and in this case the pivot element is the kth largest element.
    
    if k < i: we need to move toward the left half of the list because 'i' is too large.
    if k > i: we traverse the right half of the list, since 'i' is now too small.

    """
    while True:
        pivot_index = len(nums)//2
        pivot_element = nums[pivot_index]

        last_index = len(nums) - 1
        nums[pivot_index], nums[last_index] = nums[last_index], nums[pivot_index]

        # maintain 'i' as the leftmost barrier element, and start j from 0 and move
        # until we reach the second last element, right before the pivot element (last).
        i = 0
        for j in range(last_index):
            if nums[j] < pivot_element:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        
        # Pivot index is now at 'i', so swap the pivot element back to the correct spot.
        nums[i], nums[last_index] = nums[last_index], nums[i]
        
        if k==i:
            return pivot_element
        elif k < i:
            nums = nums[:i]
        else:
            nums = nums[i+1:]
            k -= i + 1


if __name__ == '__main__':
    nums = [ 5, 7, 1, 3, 2, 6, 4 ]
    for k in range(len(nums)):
        print(f"kth largest: {quickselect(nums, k)}")
