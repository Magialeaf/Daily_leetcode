class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        count = mat[0][:k]
        for row in mat[1:]:
            count = sorted(x + y for x in count for y in row)[:k]
        return count[-1]


'''
作者：endlesscheng
链接：https://leetcode.cn/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/solution/san-chong-suan-fa-bao-li-er-fen-da-an-du-k1vd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''