from typing import List

from collections import namedtuple

Interval = namedtuple("Interval", "start end")


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # sort the intervals by the first value such that the left sides 
    # of the intervals are sorted / aligned.
    intervals = sorted(intervals, key=lambda x: x[0])
    
    # print(str(intervals))
    
    i = 0
    while (i < len(intervals)-1):
        # if the end of the second interval is greater than the start of the first interval OR
        # if the start of the second interval is less than= end of the first interval OR
        # if the end of the first interval is greater than= the start of the second interval
        
        if (intervals[i][0] <= intervals[i+1][0] and intervals[i][1] >= intervals[i+1][1]) or (intervals[i+1][0] <= intervals[i][1])  or (intervals[i][1] >= intervals[i+1][0]):
            intervals[i] = Interval(min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1]))
            del intervals[i+1]
        else:
            i += 1
    
    return intervals

if __name__ == '__main__':
    print(f'  merge_intervals [[1,3],[2,6],[8,10],[15,18]]: { merge([Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18) ]) } ')
    print(f'  merge_intervals [[1, 4], [4, 5]]: { merge([ Interval(1, 4), Interval(4, 5) ]) }  ')