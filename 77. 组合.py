# 未剪枝
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(depth):
            if len(path) == k:
                res.append(path.copy())
                return
            else:
                for i in range(depth,n+1):
                    path.append(i)
                    dfs(i + 1)
                    path.pop()
        dfs(1)
        return res

# 剪枝
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(depth):
            sub = k - len(path) - 1 # 计算后续还需要多少个数
            if len(path) == k:
                res.append(path.copy())
                return
            else:
                for i in range(depth,n - sub + 1): # 原值-sub，如果满足条件则可选，否则直接结束
                    path.append(i)
                    dfs(i + 1)
                    path.pop()
        dfs(1)
        return res