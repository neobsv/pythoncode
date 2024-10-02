from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    indexA = indexB = 0
    k = m
    nums1 = nums1 + [0]*( m+n )

    while indexA < m and indexB < n:
        if nums1[indexA] < nums2[indexB]:
            nums1[k] = nums1[indexA]
            indexA += 1
        elif nums1[indexA] > nums2[indexB]:
            nums1[k] = nums2[indexB]
            indexB += 1
        else:
            nums1[k] = nums1[indexA]
            k += 1
            nums1[k] = nums2[indexB]
            indexA += 1
            indexB += 1
        k += 1

    while indexA < m:
        nums1[k] = nums1[indexA]
        index += 1
        k += 1

    while indexB < n:
        nums1[k] = nums2[indexB]
        indexB += 1
        k += 1

    nums1 = nums1[m:]
    return nums1

if __name__ == '__main__':
    print(f'nums1: {[1, 2, 3]} nums2: {[2, 5, 6]}')
    print(f'merge_array: { merge([1, 2, 3], 3, [2, 5, 6], 3) }  ')