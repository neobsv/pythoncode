from collections import defaultdict
from typing import List

import heapq

class PriorityQueue(object):
    """
    Implements a priority queue of objects that are sorted using 
    the default python sorting rules, and are arranged by priority 
    each time an element is pushed into the queue or popped out of the queue. 
    """
    def __init__(self):
        self.queue = []

    def push(self, x):
        heapq.heappush(self.queue, x)

    def pop(self):
        return heapq.heappop(self.queue) if len(self.queue) > 0 else None

    def peek(self):
        return self.queue[0] if len(self.queue) > 0 else None

    def is_empty(self):
        return True if len(self.queue) == 0 else False


def task_scheduler(tasks: List[int], n: int) -> int:
    """
    Make a priority queue which maintains elements sorted by the number of 
    repetitions of each of 'A'...'Z'. The task with the most repetitions has the 
    highest priority. Use a hashmap to generate this count from the given list of
    tasks, i.e. like ('A', 3); ('B', 3) ('C', 1). 

    Tasks are done between each cool-off period: 
    <tasks batch1>|cool-off|<tasks batch2>|cool-off ...
    
    Insert all these tasks into the priority queue, and for every cool off period,
    do only one of each type of tasks, eg. 'A','B' or 'C'.

    If we encounter tasks with repetitions in the same batch, put them into a temp 
    list and reinsert them into the pq after the cool-off period is done. Process for 
    executing each batch is described below.
    """
    priority_queue = PriorityQueue()
    hmap = defaultdict(int)

    """
    set all priorities to -1*(number of elements), we have a min heap but we want a max heap
    so we need to negate the value assigned to the priorities so that they get sorted in decending order.
    """
    for task in tasks:
        hmap[task] -= 1

    for k, v in hmap.items():
        priority_queue.push((v, k))

    time = 0
    while not priority_queue.is_empty():
        i = 0
        temp = []

        while i <= n:
            """
            While counter is less than the cool-off period, we want to execute tasks 
            such that task 'A' comes before task 'B' (maintained by the pq).
            
            For each unit of time:
            Now if the task 'A' has repetitions, then perform a single task of type 'A', 
            decrement the value assoc. with 'A'. After performing this task, add it to a temp list, 
            to be pushed back into the queue, since it  has repetitions remaining.

            For a task 'C', that has no repetitions, i.e. if 'C'=>1; pop the task from the queue, 
            and consider it done. Increment the time. Check if all tasks are done, then break. 
            (pq and temp are empty) Add all the tasks with repetitions, like 'A' into the pq. Repeat.
            """
            if not priority_queue.is_empty():
                if priority_queue.peek()[0] < -1:
                    value, element = priority_queue.pop()
                    temp.append((value, element))
                else:
                    value, element = priority_queue.pop()
                print(f' { element } -> ', end="")
            
            time += 1
            
            if priority_queue.is_empty() and len(temp) == 0:
                break
            
            i += 1

        print(f' idle -> ', end="")
        for value, key in temp:
            value += 1
            if v < 0:
                priority_queue.push((value, key))

    print("|| \n")
    return time

if __name__ == '__main__':
    print(f'   task_scheduler ["A","A","A","B","B","B"], 2: { task_scheduler(["A","A","A","B","B","B"], 2)  }   ')






