class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # prevMap is a Hash Map that gets appended each time we interate over the array - val:index
# hashmap is used here for instant checking
        # now iterate over the array and look for the difference with the target in the Hash Map
        for i, n in enumerate(nums): # nums is the array and i is the index of the element/value n
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i # if diff isn't found in the Has Map append the Hash Map with the n and i
        return

        # time complexity is O(n) - go through array once - n, adding values to Hah Map is constant time operation. Space complexity O(n)
        # this method works cause we are guranteed that the first element is in the has map when we are on 
        # the second element, since we only need to return 1 pair and assumption is there must be 1 pair atleast.
        