class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]: # dynamic array O(n+n), memory-- can be O(1)
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans