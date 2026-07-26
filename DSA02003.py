# Các hướng di chuyển ( biến global nên để ngoài hàm tất cả truy cập đều được)
DIRECTIONS = [
    (1, 0, 'D'),   # Down
    (0, 1, 'R')    # Right
]
# DFS / Backtracking
# ==========================
def dfs(
    maze: list[list[int]],
    x: int,
    y: int,
    path: list[str],
    result: list[str]
) -> None: #hàm chỉ xào nấu thôi chứ ko trả về gì :V 
    n = len(maze)
    # 1. Base case
    if x == n - 1 and y == n - 1:
        result.append("".join(path))
        return

    # 2. Sinh các lựa chọn
    for direction in DIRECTIONS:
        dx = direction[0]
        dy = direction[1]
        move = direction[2]

        # 3. Tính trạng thái mới
        next_x = x + dx
        next_y = y + dy

        # 4. Kiểm tra hợp lệ
        # Ra ngoài mê cung
        if next_x < 0 or next_x >= n:
            continue #(skip phương án vừa chọn để chạy vòng for thử pán khác)
        if next_y < 0 or next_y >= n:
            continue
        # Gặp tường
        if maze[next_x][next_y] == 0:
            continue
        # 5. Chọn
        path.append(move)
        # 6. Đệ quy
        dfs(
            maze,
            next_x,
            next_y,
            path,
            result
        )
        # 7. Hoàn tác
        path.pop()
# Giải một test
# ==========================
def solve(maze: list[list[int]]) -> list[str]:
    result = []
    # Nếu ô xuát phát đã là tường 
    if maze[0][0] == 0:
        return result
    dfs(
        maze=maze,
        x=0,
        y=0,
        path=[],
        result=result
    )
    return result
# Main
t = int(input())
for _ in range(t):
    n = int(input())
    maze = []
    for i in range(n):
        row = list(map(int, input().split()))
        maze.append(row)
    res = solve(maze)
    if len(res) == 0:
        print(-1)
    else:
        print(*res)