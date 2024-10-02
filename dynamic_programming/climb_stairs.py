from typing import List

def climb_stairs(n: int, steps: List[int]) -> int:
    """
    Iterate over all possible step sizes and add the (i-k)th value to the
    ith position in the result array, for each step size. This adds up the
    possible combinations of ways from each i-kth step to reach the ith step.
    """
    if n < 0:
        return 0

    T = [ 0 for i in range(n + 1) ]

    T[0], T[1] = 1, 1

    for i in range(2, n + 1):
        for step in steps:
            T[i] += T[i - step]

    return T[-1]

if __name__ == '__main__':
    print(f" climb_stairs 5, [1, 2]: { climb_stairs(5, []) } ")
    print(f" climb_stairs 5, [1, 2]: { climb_stairs(-1, [1, 2]) } ")
    print(f" climb_stairs 5, [1, 2]: { climb_stairs(2, [1, 2]) } ")
    print(f" climb_stairs 5, [1, 2]: { climb_stairs(3, [1, 2]) } ")
    print(f" climb_stairs 5, [1, 2]: { climb_stairs(5, [1, 2]) } ")