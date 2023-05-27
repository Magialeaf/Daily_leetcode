# bfs
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        AdList = [[] for _ in range(n+1)]
        for lst in edges:
            AdList[lst[0]].append(lst[1])
            AdList[lst[1]].append(lst[0])
        Visited = [0 for _ in range(n+1)]

        def bfs(position,time):
            l = len(AdList[position])
            if position > 1:
                l -= 1
            Visited[position] = 1

            if l == 0 or time == 0:
                if position == target:
                    return 1.0
                else:
                    return 0.0

            nextList = []
            for nxt in AdList[position]:
                if Visited[nxt] == 0:
                    Visited[nxt] = 1
                    nextList.append(nxt)
            for nxt in nextList:
                p = bfs(nxt,time - 1)
                if p > 0:
                    return p / l
            return p
        return bfs(1,t)

# dfs
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        AdList = [[] for _ in range(n+1)]
        for lst in edges:
            AdList[lst[0]].append(lst[1])
            AdList[lst[1]].append(lst[0])
        Visited = [0 for _ in range(n+1)]

        def bfs(position,time):
            l = len(AdList[position])
            if position > 1:
                l -= 1
            Visited[position] = 1

            if l == 0 or time == 0:
                if position == target:
                    return 1.0
                else:
                    return 0.0

            for nxt in AdList[position]:
                if Visited[nxt] == 0:
                    p = bfs(nxt,time - 1)
                    if p > 0:
                        return p / l
            return 0.0
        return bfs(1,t)