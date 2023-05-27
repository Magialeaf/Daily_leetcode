class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        lens = 0
        mins = -1
        maxs = -1
        max_count = [0,0]
        sums = 0
        for idx,c in enumerate(count):
            if c > 0:
                sums = sums + idx * c
                lens += c
                if mins == -1:
                    mins = idx
                maxs = idx
                if max_count[0] < c:
                    max_count = [c,idx]
        temp = int(lens / 2)
        if lens % 2 == 0:
            for idx, c in enumerate(count):
                if temp - c > 0:
                    temp -= c
                elif temp - c == 0:
                    mid = idx
                    for i in range(idx+1,len(count)):
                        if count[i] > 0:
                            mid += i
                            mid /= 2
                            break
                    break
                else:
                    mid = idx
                    break
        else:
            temp += 1
            for idx, c in enumerate(count):
                if temp - c > 0:
                    temp -= c
                else:
                    mid = idx
                    break
        return [mins, maxs, sums / lens, mid, max_count[1]]