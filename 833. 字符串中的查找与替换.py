class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        nxt = 0
        res = []
        dic = {}

        for i,idx in enumerate(indices):
            dic[idx] = i

        keys = sorted(dic.keys())

        for idx in keys:
            i = dic[idx]

            l = len(sources[i])

            res.append(s[nxt:idx])

            if s[idx:idx + l] == sources[i]:
                res.append(targets[i])
                nxt = idx + l
            else:
                nxt = idx + l
                res.append(s[idx:nxt])

        res.append(s[nxt:])

        return "".join(res)