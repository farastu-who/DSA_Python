class Solution:
    def isAnagram(self, s: str, t: str) -> bool: # count the characters of each str and create and match the hash maps, tc: O(s+t) same sc
        if len(s)!=len(t):
            return False
        
        countS, countT = {}, {}

        # build the hash maps with the key-value pair
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #s[i] is the character, so increment by 1 when you see character -- key error if the character doesn't exist in hash map yet so use the get call for hashmap
            countT[t[i]] = 1 +countT.get(t[i], 0)

        # iterate through the has maps
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
        
            
    # easy soln: use Counter function: return Counter(s) == Counter (t)

    # can we do it with O(1) memory?
    # put them in sorted order and perform an equals operation, but bubble sort is n^2, but sorting also takes up extra memory.

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool: # count the characters of each str and create and match the hash maps, tc: O(s+t) same sc
        return sorted(s) == sorted(t)
