"""
 Given an array "prices" for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note:  you must sell the stock before you buy again

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 10000

Input Format:
Firstline contains the number of days
Secondline contains the elements of Prices array

Output Format:

print the max profit that can be gained

Example 1:

Input:
6
7 1 5 3 6 4

Output:
7

Explanation:
Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:

Input:
5
1 2 3 4 5

Output:
4

Explanation:
Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: 
5
7 6 4 3 1

Output:
0

Explanation: In this case, no transaction is done, i.e. max profit = 0.
 


"""

def maxProfit(prices):
    best = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            best += prices[i] - prices[i-1]
    return best
prices=list(map(int,input().split()))
print(maxProfit(prices))
