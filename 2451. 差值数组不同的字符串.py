class Solution:
    def oddString(self, words: List[str]) -> str:
        a = 97
        dic = {}
        for idx, substr in enumerate(words):
            temp = []
            for i in range(len(substr) - 1):
                temp.append((ord(substr[i + 1]) - a) - (ord(substr[i]) - a))
            temp = tuple(temp)
            if temp in dic:
                dic[temp][0] += 1
                if len(dic) > 1:
                    break
            else:
                dic[temp] = [1,idx]
        for value in dic.values():
            if value[0] == 1:
                return words[value[1]]