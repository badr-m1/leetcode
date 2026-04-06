import pytest

class Solution(object):
    def robotSim(self, commands, obstacles):
        maxdist = 0
        cx,cy = [0,0]
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        didx = 0

        x_axis = {}
        y_axis = {}
        for x, y in obstacles:
            if x not in x_axis:
                x_axis[x] = []
            x_axis[x].append(y)

            if y not in y_axis:
                y_axis[y] = []
            y_axis[y].append(x)
    
        for x in x_axis: x_axis[x].sort()
        for y in y_axis: y_axis[y].sort()

        
        for c in commands:
            if c > 0:
                dx, dy = dirs[didx]
                nx = cx + dx * c
                ny = cy + dy * c

                moving_vertical = dx == 0
                axis = x_axis if moving_vertical else y_axis
                key = cx if moving_vertical else cy
                sign = dy if moving_vertical else dx

                if key in axis:
                    obstacles = axis[key]
                    iterator = obstacles if sign > 0 else reversed(obstacles)

                    for z in iterator:
                        if moving_vertical:
                            if (sign > 0 and cy < z <= ny) or (sign < 0 and ny <= z < cy):
                                ny = z - sign
                                break
                        else:
                            if (sign > 0 and cx < z <= nx) or (sign < 0 and nx <= z < cx):
                                nx = z - sign
                                break

                cx, cy = nx, ny
                maxdist = max(maxdist, cx**2 + cy**2)

            else:
                didx = (didx + (1 if c == -1 else -1)) % 4

        return maxdist

def test():
    s = Solution()

    assert s.robotSim([4,-1,3],[]) == 25
    assert s.robotSim([4,-1,4,-2,4],[[2,4]]) == 65
    assert s.robotSim([6,-1,-1,6],[[0,0]]) == 36
    assert s.robotSim([7,-2,-2,7,5], [[-3,2],[-2,1],[0,1],[-2,4],[-1,0],[-2,-3],[0,-3],[4,4],[-3,3],[2,2]] ) == 4
