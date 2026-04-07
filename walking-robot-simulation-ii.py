class Robot(object):
    dirs = [(1,0), (0,1), (-1,0),(0,-1)]
    dirlabels = {(1,0):"East", (0,-1):"South", (-1,0):"West",(0,1):"North"}

    def __init__(self, width, height):
        x,y = -1, 0
        diridx = 0
        self.positions = []
        self.pos_dirs = []
        self.posidx = 0

        for i in range((width*2 + height*2)-1):
            dx,dy = self.dirs[diridx]
            if x+dx >= width or x+dx < 0 or y+dy >= height or y+dy < 0:
                diridx = (diridx + 1) % 4
                continue
            x += dx
            y += dy
            self.positions.append([x,y])
            self.pos_dirs.append((dx,dy))
    

    def step(self, num):
        self.posidx = (self.posidx + num) % len(self.positions)
        self.pos_dirs[0] = (0,-1)
        

    def getPos(self):
        return self.positions[self.posidx]


    def getDir(self):
        return self.dirlabels[self.pos_dirs[self.posidx]]

        
