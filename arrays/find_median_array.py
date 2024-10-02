from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float

    Use the merge sort merge function, in order to first merge 
    the two arrays, in case of equal numbers, i.e. if 
    nums1[i] == nums2[j] at some point during the merge: 

    Then add the element twice, say [1, 2, 3, 3 …] because the 
    median of the arrays is affected by the fact that there 
    will be duplicate elements stemming from both the arrays.

    The median is found by checking if the length of the array is 
    even or odd, if it is even then it is the average of the 
    two middle elements, if it is odd, then the median is simply 
            the middle element itself.

    """
    m, n = len(nums1), len(nums2)
    i = j = 0
    k = 0
    nums3 = [0]*(m+n)
    
    while i<m and j<n:
        if nums1[i] < nums2[j]:
            nums3[k] = nums1[i]
            i+=1
            k+=1
        elif nums2[j] < nums1[i]:
            nums3[k] = nums2[j]
            j+=1
            k+=1
        else:
            nums3[k] = nums1[i]
            k+=1
            nums3[k] = nums1[i]
            k+=1
            i+=1
            j+=1
    
    while i<m:
        nums3[k] = nums1[i]
        i+=1
        k+=1
    
    while j<n:
        nums3[k] = nums2[j]
        j+=1
        k+=1
    """
    i=0
    while i<m:
        nums1.pop(0)
        i+=1
    """
    #print nums1
    
    mk = len(nums3)//2
    if len(nums3)%2==0:
        return float(nums3[mk]+nums3[mk-1])/2
    else:
        return float(nums3[mk])


if __name__ == '__main__':
    print(f' find_median: {findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6])} ')


