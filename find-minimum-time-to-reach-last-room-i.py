class Solution(object):

        
    def minTimeToReach(self, moveTime):
        m = len(moveTime)
        n = len(moveTime[0])

        queue = [[0,0]]
        scores = [[float("inf") for i in range(n)] for j in range(m)]
        scores[0][0] = 0

        while len(queue) > 0:
            curr = queue.pop(0)

            for dir in [[0,1], [0,-1], [1,0],[-1,0]]:
                if curr[0] + dir[0] >= -0 and curr[0] + dir[0] < m and curr[1] + dir[1] >= 0 and curr[1] + dir[1] < n:
                    nScore = max(scores[curr[0]][curr[1]] + 1 , moveTime[curr[0] + dir[0]][curr[1] + dir[1]]+1)
                    if scores[curr[0] + dir[0]][curr[1]+dir[1]] > nScore:
                        scores[curr[0] + dir[0]][curr[1]+dir[1]] = nScore
                        queue.append([curr[0] + dir[0], curr[1]+dir[1]])
                        
        return scores[m-1][n-1]
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
         

s = Solution()

print(s.minTimeToReach([[0,4],[4,4]]))
print(s.minTimeToReach([[0,0,0],[0,0,0]]))
print(s.minTimeToReach([[0,1],[1,2]]))