from collections import deque
# Hàm BFS loang 8 hướng để xóa 1 hòn đảo
def bfs_clear_island(start_r, start_c, n, m, grid):
    # 8 hướng: trên, dưới, trái, phải và 4 đường chéo
    dx = [-1, -1, -1,  0, 0,  1, 1, 1]
    dy = [-1,  0,  1, -1, 1, -1, 0, 1]
    queue = deque([(start_r, start_c)])
    grid[start_r][start_c] = 0  # Đánh dấu ô này đã duyệt bằng cách đổi thành 0
    while queue:
        r, c = queue.popleft()
        for i in range(8):
            nr = r + dx[i]
            nc = c + dy[i]
            # Kiểm tra trong phạm vi ma trận và là ô đất nổi (1)
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                grid[nr][nc] = 0  # Đánh dấu đã thăm
                queue.append((nr, nc))

# Hàm đếm số hòn đảo
def count_islands(n, m, grid):
    islands_count = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                islands_count += 1
                # Loang ra 8 hướng để đánh dấu toàn bộ hòn đảo này
                bfs_clear_island(r, c, n, m, grid)
    return islands_count
# Hàm xử lý Nhập / Xuất
def solve():
    t_str = input().strip()
    if not t_str:
        return
    t = int(t_str)
    
    for _ in range(t):
        # Nhập N và M
        line = input().split()
        if not line:
            continue
        n, m = map(int, line)
        # Nhập ma trận N x M
        grid = []
        for _ in range(n):
            row = list(map(int, input().split()))
            grid.append(row)
        
        # Gọi hàm đếm và in kết quả
        ans = count_islands(n, m, grid)
        print(ans)
if __name__ == "__main__":
    solve()