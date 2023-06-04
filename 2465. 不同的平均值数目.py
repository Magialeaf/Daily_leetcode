class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        dic = {}
        res = 0
        lp = 0
        rp = len(nums) - 1
        while lp < rp:
            sums = nums[lp] + nums[rp]
            if sums not in dic:
                dic[sums] = 1
                res += 1
            lp += 1
            rp -= 1
        return res