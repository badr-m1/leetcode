import pytest

class Solution(object):
    
    def areSimilar(self, mat, k):
        for row in mat:
            n = len(row)
            for x in range(n):
                newX = (x-k)%n
                if row[x] != row[newX]:
                    return False 
                
        return True

def test():
    s = Solution()

    assert s.areSimilar([[1,2,3],[4,5,6],[7,8,9]], 4) == False
    assert s.areSimilar([[1,2,1,2],[5,5,5,5],[6,3,6,3]], 2) == True
