class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic = {}
        for i in range(len(grid)):
            row = tuple(grid[i])
            col = tuple([grid[j][i] for j in range(len(grid[i]))])
            if row in dic:
                dic[row][0] += 1
            else:
                dic[row] = [1,0]
            if col in dic:
                dic[col][1] += 1
            else:
                dic[col] = [0,1]
        count = 0
        for lst in dic.values():
            if lst[0] > 0 and lst[1] > 0:
                count += lst[0] * lst[1]
        return count