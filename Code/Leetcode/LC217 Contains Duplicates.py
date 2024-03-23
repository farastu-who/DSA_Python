class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set ()
# increase space complexity from O(1) to O(n) to reduce time complexity from 
# O(n^2) - iterating over every element to find duplicates or O(nlogn) - sorted array to O(n) wish hashset
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False