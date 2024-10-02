from typing import List

def knapsack01_unbounded(item_list: List[int], capacity: int) -> int:
    """
    The 0/1 Knapsack problem deals with a bag of items which need to be filled
    with a set of input items. The list of items have a weight, and value attached to them, 
    the key is to fit as many items in the bag as possible.

    We would need to sort the list of items first, and move from the smallest to largest, to
    try and fit as many items as possible in the bag.

    The way to do this is go back from the current index, T[i - weight of jth element] + value of
    jth element. For each index of the result array of the specified capacity ; len(T) specifies
    each capacity iteration for the bag, try to fit all the elements into the bag, provided the weight
    does not exceed the capacity i. So, for each capacity i, the position in the result array would be
    filled with the item that provides the max value for that cell, maximizing them by the value it provides
    to the cell. This problem assumes you have an infinite supply of each element.
    """
    item_list.sort()

    T = [ 0 for i in range(len(item_list) + 1) ]


    for i in range(1, len(T)):
        for j in range(len(item_list)):
            if ( i - item_list[j][0] ) > 0:
                T[i] = max(T[i], item_list[j][1] + T[ i - item_list[j][0] ])

    return T[-1]


def knapsack_weighted(item_list: List[object], capacity: int) -> List[int]:
    """
    The weighted knapsack problem deals with a bag of a specified capacity and
    tries to fill it with a list of items of a certian value, which carry a weight as well.
    Weight subtracts from capacity. The goal is to fill the bag with the most value, such that
    high value, low weight items are preferred. The way to go about this is to traverse the matrix,
    and decide if you would like to pick the item which would mean entering T[i-1][j-weight] (prev.
    optimal + current item's value );  OR move on without the item T[i-1][j]. The way the matrix would
    be filled would look like, initially only the value of item i in the ith row, then as j increases,
    both the i-1th and ith elements could fit into the bag so the sum of their values would appear in 
    the cell T[i][j]. At the end of the process, the whole bag is filled by satisfying this optimality
    condition so, a very heavy item with a low value would be discarded since T[i-1] | [j-weight] | 
    => this term would have a very low or mostly 0 value, so the max condition would prefer excluding 
    this item. For this to work, the list of items should be sorted by their weight/ value ratios.
    """
    item_list = sorted(item_list, key= lambda x: x[0]//x[1])

    T = [ [ 0 for i in range(capacity + 1) ] for j in range(len(item_list) + 1) ]

    for i in range(1, len(item_list) +  1):
        li = i - 1
        weight = item_list[li][0]
        value  = item_list[li][1]

        for j in range(1, capacity + 1):
            if ( j < weight ):
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], T[i-1][j-weight] + value)

    def backtrack(T: List[List[int]], item_list: List[int], capacity: int) -> List[int]:
        """
        Move backwards along the principal diagonal to check which items from the item
        list need to be included in the set of elements that need to be kept. the keep
        array is a binary array which indicates keep/ not keep the element.
        """
        item_list = sorted(item_list, key=lambda x: x[1])

        total_value, diagr, diagc = T[-1][-1], len(item_list) - 1, len(item_list) - 1
        keep = [ 0 for i in range(len(item_list)) ]

        for i in range(len(item_list)):
            for j in range(len(item_list)):
                value = item_list[j][1]

                if ( (total_value - value ) == T[diagr][diagc] ):
                    keep[i] = 1
                    total_value = total_value - value

            diagr, diagc = diagr - 1, diagc - 1

        return keep

    return backtrack(T, item_list, capacity)

if __name__ == '__main__':
    print(f" knapsack01_unbounded [2, 4, 6, 7, 8, 1, 15, 3], 13: { knapsack01_unbounded([ [ 2, 4 ], [ 4, 1 ], [ 6, 2 ], [ 7, 3 ], [ 8, 1 ], [ 1, 1 ], [ 15, 7 ], [ 3, 2] ], 13) } ")
    print(f" knapsack_weighted [1, 2, 3, 4, 6, 7, 8, 15], 13:  keep_items: { knapsack_weighted([ [ 2, 4 ], [ 4, 1 ], [ 6, 2 ], [ 7, 3 ], [ 8, 1 ], [ 1, 1 ], [ 15, 7 ], [ 3, 2] ], 13) } ")










