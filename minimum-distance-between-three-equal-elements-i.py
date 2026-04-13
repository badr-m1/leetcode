import pytest

class Solution(object):
    def get_combinations(self, arr):
        n = len(arr)
        result = []
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    result.append((arr[i], arr[j], arr[k]))
        
        return result

    def minimumDistance(self, nums):
        occurances = {}
        for idx, x in enumerate(nums):
            if x not in occurances.keys():
                occurances[x] = [idx]
            else:
                occurances[x].append(idx)
        
        groups = []
        for k in occurances.keys():
            if len(occurances[k]) < 3: continue
            groups += self.get_combinations(occurances[k])


        if len(groups) == 0: return -1

        mindist = float("inf")
        for a, b, c in groups:
            dist = abs(a-b) + abs(b-c) + abs(a-c)
            mindist = min(mindist, dist)
        
        return mindist

        

def test():
    s = Solution()

    assert s.minimumDistance([1,2,1,1,3]) == 6
    assert s.minimumDistance([1,1,2,3,2,1,2]) == 8
    assert s.minimumDistance([5,5,5,2,5]) == 4

