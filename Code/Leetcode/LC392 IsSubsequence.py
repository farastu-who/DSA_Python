class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            for j in t:
                if s[i] != t[j]:
            return False
        
        return True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # common in DP, like Longest common subsequence
        # needs to be in ORDER!!
        # have 2 pointers and shift the pointers because we need order; O(n)

        i, j = 0, 0

        while i< len(s) and j< len(t):
            if s[i] == t[j]:
                i += 1
            j+= 1 # j increments regardless so no need for another condition

        return True if i == len(s) else False  # found matching character for every character in s