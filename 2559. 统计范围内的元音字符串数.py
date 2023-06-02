class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # 两个for
        # vowel = {'a','e','i','o','u'}
        # res = []
        # for query in queries:
        #    temp = 0
        #    for word in words[query[0]:query[1]+1]:
        #        if word[0] in vowel and word[-1] in vowel:
        #            temp += 1
        #        else:
        #           continue
        #    res.append(temp)
        # return res
        vowel = {'a','e','i','o','u'}
        sums = []
        res = []
        last = 0
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                last += 1
                sums.append(last)
            else:
                sums.append(last)
        for query in queries:
            if query[0] == 0:
                res.append(sums[query[1]])
            else:
                res.append(sums[query[1]] - sums[query[0]-1])
        return res