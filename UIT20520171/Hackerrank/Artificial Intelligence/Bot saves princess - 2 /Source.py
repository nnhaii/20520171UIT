def nextMove(n,r,c,grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]=='p':
                if i>r:
                    return 'DOWN'
                elif i<r:
                    return 'UP'
                elif j>c:
                    return 'RIGHT'
                else:
                    return 'LEFT'

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))