R, C, K = map(int, input().split())
visited = []
world = []

for _ in range(R):
    world.append(list(input().strip()))

world[R-1][0] = 1
change = [(1,0), (0,1), (-1,0), (0,-1)]
result = 0

def walk(x, y):
    global world, result 

    if x == 0 and y == C-1:
        if world[x][y] == K:
            result += 1
        return
    
    for dif in change:
        nx = x + dif[0]; ny = y + dif[1]
        if nx >= 0 and nx < R and ny >= 0 and ny < C:
            if world[nx][ny] == '.':
                world[nx][ny] = world[x][y] + 1
                walk(nx, ny)
                world[nx][ny] = '.'

walk(R-1,0)
print(result)



    