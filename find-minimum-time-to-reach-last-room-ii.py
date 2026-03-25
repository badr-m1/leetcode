import heapq

class Solution(object):


    def minTimeToReach(self, moveTime):
        m = len(moveTime)
        n = len(moveTime[0])

        queue = []
        scores = [[float("inf") for i in range(n)] for j in range(m)]
        scores[0][0] = 0
        curr, s = [0,0], 1
        while curr != [m-1,n-1]:
            

            for dir in [[0,1], [0,-1], [1,0],[-1,0]]:
                if curr[0] + dir[0] >= -0 and curr[0] + dir[0] < m and curr[1] + dir[1] >= 0 and curr[1] + dir[1] < n:
                    nScore = max(scores[curr[0]][curr[1]] + s , moveTime[curr[0] + dir[0]][curr[1] + dir[1]]+s)
                    if scores[curr[0] + dir[0]][curr[1]+dir[1]] > nScore:
                        scores[curr[0] + dir[0]][curr[1]+dir[1]] = nScore
                        nextS = 1 if s == 2 else 2
                        heapq.heappush(queue, (nScore, ([curr[0] + dir[0], curr[1]+dir[1]], nextS)))

            _ , item = heapq.heappop(queue)
            curr, s = item
        
        return scores[m-1][n-1]
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
         

s = Solution()

print(s.minTimeToReach([[0,4],[4,4]]) == 7)
print(s.minTimeToReach([[0,0,0,0],[0,0,0,0]]) == 6)
print(s.minTimeToReach([[0,1],[1,2]]) == 4)