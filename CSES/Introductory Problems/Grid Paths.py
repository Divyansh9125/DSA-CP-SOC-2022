grid = [[0 for i in range(7)] for j in range(7)]

def solve(mv, x, y):
    if x==0 and y==6:
        if len(mv)==48:
            found = True
            for i in range(48):
                if stng[i]!=mv[i] and stng[i]!='?':
                    found = False
                    break
            if found:
                return 1
        else:
            return 0
    count = 0
    if mv!=[] and not (stng[len(mv)-1]=='?' or stng[len(mv)-1]==mv[len(mv)-1]):
        return 0
    if 0<x<6 and 0<y<6:
        if (grid[y-1][x]==grid[y+1][x]==0 and grid[y][x-1]==grid[y][x+1]==1) or (grid[y-1][x]==grid[y+1][x]==1 and grid[y][x-1]==grid[y][x+1]==0):
            return 0
    elif (0<x<6 and grid[y][x-1]==grid[y][x+1]==0 and grid[y-abs(y-3)//(y-3)][x]==1) or (0<y<6 and grid[y+1][x]==grid[y-1][x]==0 and grid[y][x-abs(x-3)//(x-3)]==1):
        return 0

    if y!=6 and grid[y+1][x]!=1:
        grid[y+1][x]=1
        mv.append('D')
        count+=solve(mv, x, y+1)
        mv.pop()
        grid[y+1][x]=0
    if y!=0 and grid[y-1][x]!=1:
        grid[y-1][x]=1
        mv.append('U')
        count+=solve(mv, x, y-1)
        mv.pop()
        grid[y-1][x]=0
    if x!=6 and grid[y][x+1]!=1:
        grid[y][x+1]=1
        mv.append('R')
        count+=solve(mv, x+1, y)
        mv.pop()
        grid[y][x+1]=0
    if x!=0 and grid[y][x-1]!=1:
        grid[y][x-1]=1
        mv.append('L')
        count+=solve(mv, x-1, y)
        mv.pop()
        grid[y][x-1]=0
    return count

grid[0][0]=1
stng = input()
print(solve([], 0, 0))