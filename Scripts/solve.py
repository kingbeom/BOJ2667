import sys
def dfs(y, x):
    mapp[y][x]='0'
    global cnt
    cnt+=1
    for n in range(4):
        ny = y+dy[n]
        nx = x+dx[n]
        if ny<0 or nx<0 or ny>=a or nx>=a:
            continue
        if mapp[ny][nx] == '1':
            dfs(ny,nx)

a=int(sys.stdin.readline())
mapp=[list(sys.stdin.readline()) for _ in range(a)]
dy,dx=[0,0,1,-1], [1,-1,0,0] #동,서,북,남
sol=[]
for i in range(a):
    for j in range(a):
        if mapp[i][j]=='1':
            cnt=0
            dfs(i, j)
            sol.append(cnt)
print(len(sol))
sol.sort()
for i in sol:
    print(i)