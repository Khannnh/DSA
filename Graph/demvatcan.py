import sys

# Tăng giới hạn đệ quy phòng trường hợp ma trận lớn (1000 x 1000)
sys.setrecursionlimit(10**6)

# 4 hướng di chuyển: Trên, Dưới, Trái, Phải
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(r, c, n, m, grid):
    # Đánh dấu ô hiện tại đã thăm bằng cách biến nó thành ô trống '.'
    grid[r][c] = '.'
    
    # Loang ra 4 hướng chung cạnh
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        
        # Kiểm tra nằm trong phạm vi ma trận và là ô vật cản '#'
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '#':
            dfs(nr, nc, n, m, grid)

def solve():
    # Đọc nhanh dữ liệu
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Chuyển ma trận ký tự thành list các danh sách để dễ sửa đổi giá trị
    grid = [list(input_data[i + 2]) for i in range(n)]
    
    count = 0
    # Duyệt qua từng ô trong ma trận
    for r in range(n):
        for c in range(m):
            if grid[r][c] == '#':
                count += 1
                dfs(r, c, n, m, grid) # Loang xóa hết khối vật cản này
                
    print(count)

if __name__ == "__main__":
    solve()