DIRECTIONS = [
    (1,0,"D"), #down
    (0,1,"R") #right
]
def dfs(maze:list[list] , x:int , y:int , path:list , result:list):
    n=len(maze)
    #basecase
    if x == n-1 and y==n-1 : 
        result.append("".join(map(str,path)))
        return 
    #các lựa chọn 
    for directions in DIRECTIONS: 
        dx = directions[0]
        dy = directions[1]
        move = directions[2]

        next_x = x+ dx 
        next_y = y+ dy 

        #nếu ra ngoài mê cung thì thử lựa chọn khác 
        if next_x < 0 or next_x>= n : 
            continue 
        if next_y < 0 or next_y >= n :
            continue 
        # Gặp tường
        if maze[next_x][next_y] == 0:
            continue
        path.append(move)
        dfs(maze,next_x,next_y,path,result)
        path.pop()

def solve(maze):
    res = []
    if maze[0][0] == 0 : 
        return res
    dfs(maze,0,0,[],res)
    return res

t=int(input())
for _ in range(t):
    n=int(input())
    mecung = []
    for _ in range(n):
        row = list(map(int , input().split()))
        mecung.append(row)
    result = solve(mecung)
    if len(result)>= 1 : 
        print(*result)
    else:
        print(-1)


    

    