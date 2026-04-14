import pytest

class Solution(object):
    def minimumDistance(self, nums):
        occurances = {}
        mindist = float("inf")

        for idx, x in enumerate(nums):
            if x not in occurances:
                occurances[x] = [idx]
            else:
                occurances[x].append(idx)
                if len(occurances[x]) >= 3:
                    dist = 2*(occurances[x][-1] - occurances[x][-3])
                    mindist = min(dist, mindist)

        if mindist == float("inf"): return -1
        
        return mindist

        

def test():
    s = Solution()

    assert s.minimumDistance([1,2,1,1,3]) == 6
    assert s.minimumDistance([1,1,2,3,2,1,2]) == 8
    assert s.minimumDistance([5,5,5,2,5]) == 4

