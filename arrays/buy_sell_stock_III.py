from typing import List

def maxProfit(prices) -> int:
    """
    Pre compute the prefix and suffix sums of the array, then prepare
    another array with the max of both.
    """
    if not prices:
        return 0
    prefix = [ 0 for i in range(len(prices)) ]
    suffix = [ 0 for i in range(len(prices)) ]
    
    minj = float('inf')
    for i in range(len(prices)):
        prefix[i] = max(prefix[i], prices[i] - minj)
        minj = min(minj, prices[i])
    
    maxj = prices[-1]
    for i in range(len(prices)-2, 0, -1):
        maxj = max(maxj, prices[i])
        suffix[i] = max(suffix[i+1], maxj - prices[i])
    
    ans = 0
    for p, s in zip(prefix, suffix):
        ans = max(ans, p+s)
    
    return ans

if __name__ == '__main__':
    print(f' buy_sell_stock_III [3, 3, 5, 0, 0, 3, 1, 4]: {maxProfit([3, 3, 5, 0, 0, 3, 1, 4])} ')
    print(f' buy_sell_stock_III [1, 2, 3, 4, 5]: {maxProfit([1, 2, 3, 4, 5])} ')
    print(f' buy_sell_stock_III [7, 6, 4, 3, 1]: {maxProfit([7, 6, 4, 3, 1])} ')