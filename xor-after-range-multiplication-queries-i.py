class Solution(object):
    def xorAfterQueries(self, nums, queries):
        for q in queries:
            l, r, k, v = q 
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % (10 ** 9 + 7)
                idx += k

        x = 0
        for n in nums:
            x ^= n

        return x
