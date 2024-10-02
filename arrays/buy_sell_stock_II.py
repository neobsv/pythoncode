from typing import List

def maxProfit(prices: List[int]) -> int:
    """
    :type prices: List[int]
    :rtype: int

    Add the difference of the prices, whenever there is a positive 
    delta between the ith and i-1th element. This emulates a buy at i-1 
    And sell at i, do this repeatedly till the end of the array, since no. 
    of transactions are unlimited.
    """
    ans = 0
    
    for i in range (1, len(prices)):
        if (prices[i] > prices[i-1]):
            ans += prices[i] - prices[i-1]
            
    return ans

if __name__ == '__main__':
    print(f' buy_sell_two [7, 1, 5, 3, 6, 4]: {maxProfit([7,1,5,3,6,4])} ')
    print(f' buy_sell_two [1, 2, 3, 4, 5]: {maxProfit([1, 2, 3, 4, 5])} ')