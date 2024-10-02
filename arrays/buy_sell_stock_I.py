from typing import List

def maxProfit(prices: List[int]) -> int:
    ans = 0
    minj = float('inf')
    
    for i in range(len(prices)):
        ans = max(ans, prices[i] - minj)
        minj = min(minj, prices[i])
    return ans

if __name__ == '__main__':
    print(f' best time to buy sell [7, 1, 5, 3, 6, 4]: { maxProfit([7, 1, 5, 3, 6, 4]) } ')
    print(f' best time to buy sell [7, 6, 4, 3, 1]: { maxProfit([7, 6, 4, 3, 1]) } ')