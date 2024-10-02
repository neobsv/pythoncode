from typing import List

def longest_incr_subsequence(nums: List[int]) -> int:
    """
    Maintain a result matrix T to record the results for each index
    i in the input array, and initialize an index 'j' at every index 'i'
    which moves from 0..j. Count the number of numbers that are lesser than
    the number at the current index i and record them in the result matrix T.
    The final answer is the max(T), which can be viewed as a sequence constructed
    by moving from the final node  (sink) of the DAG constructed, from the final
    node of the longest increasing sequence in the array to the source which is the
    starting node of such a sequence in the input array.

    We initialize the T array to 1 because the longest increasing sequence formed by
    one element of the array is the element itself.
    """
    T = [ 1 for i in range(len(nums)) ]
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                T[i] = max(T[i], T[j] + 1)
    return max(T) if len(T) > 0 else -1


if __name__ == '__main__':
    print(f" longest_incr_subsequence []: { longest_incr_subsequence([]) } ")
    print(f" longest_incr_subsequence [0]: { longest_incr_subsequence([0]) } ")
    print(f" longest_incr_subsequence [0, 1, 0, 3, 2, 3]: { longest_incr_subsequence([0, 1, 0, 3, 2, 3]) } ")
    print(f" longest_incr_subsequence [7, 7, 7, 7, 7, 7, 7]: { longest_incr_subsequence([7, 7, 7, 7, 7, 7, 7]) } ")
    print(f" longest_incr_subsequence [10, 9, 2, 5, 3, 7, 101, 18]: { longest_incr_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) } ")