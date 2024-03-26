class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        mapp = grid
        minutes = 0
        queue = []
        dxdy = ((0,1), (0,-1), (1,0), (-1,0))
        for x in range(len(mapp)):
            for y in range(len(mapp[x])):
                if mapp[x][y] == 2:
                    queue.append((x,y))
        flag = True
        while queue:
            if flag:
                flag = False
            else:
                minutes += 1
            queue1 = queue[:]
            queue = []
            for x, y in queue1:
                for _ in dxdy:
                    nx = x + _[0]
                    ny = y + _[1]
                    if 0 <= nx < len(mapp) and 0 <= ny < len(mapp[0]):
                        if mapp[nx][ny] == 1:
                            mapp[nx][ny] = 2
                            queue.append((nx,ny))
        for x in range(len(mapp)):
            for y in range(len(mapp[0])):
                if mapp[x][y] == 1:
                    return -1
        return minutes
