class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            mins = inf
            idx = -1
            for i in range(len(arr) - 1):
                mini = arr[i] * arr[i+1]
                if mini < mins:
                   mins = mini
                   idx = i if arr[i] < arr[i+1] else i+1
            res += mins
            arr.pop(idx)
        return res
