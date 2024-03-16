class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use two pointers since we need to keep track of 2 things
        l, r = 0, 1 # initialize the left, l and the right, r to 0 and 1
        maxP = 0 # initialize maximum profit to 0 since we want to keep checking if maximum profit has been reached

        while r < len(prices): #out of bounds exception avoided
            if prices[l] < prices[r]: # check if buy price l is less than sell price r
                profit = prices[r] - prices[l] # calculate profit and copare with the max profit and choose the max
                maxP = max(maxP, profit)
            else:
                l = r
            r+=1 # careful with this since we want to increment r in both if and else

        return maxP

        