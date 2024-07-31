class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        newArr = [0] * n 

        for i in range(n):
            if i == n-1:
                newArr[i] = -1
            else:
                newArr[i] = max(arr[i+1:])

        return newArr

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]: # repeated work do TC: O(n^2)
    # cut down on repeated values, do it in reverse order so you only need to do max between 2 values
    # initial max = -1
    # reverse iteration
    # new max = max(oldmax, arr[i])

    rightMax = -1

    for i in range(len(arr)-1, -1, -1):
        newMax = max(rightMax, arr[i])
        arr[i] = rightMax
        rightMax = newMax

    return arr