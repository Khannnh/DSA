from collections import deque

# Hàm BFS đếm số lượng sinh viên trong 1 nhóm bạn
def bfs_count_group(start, adj, visited):
    queue = deque([start])
    visited[start] = True
    count = 1  # Đếm đỉnh start
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                count += 1
                queue.append(v)
                
    return count

def solve():
    # Nhập số lượng testcase T
    t_str = input().strip()
    if not t_str:
        return
    t = int(t_str)
    
    for _ in range(t):
        # Nhập N (số sinh viên) và M (số cặp bạn)
        line = input().split()
        if not line:
            continue
        n, m = map(int, line)
        
        # Khởi tạo danh sách kề cho đồ thị vô hướng
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)  # Bạn bè là quan hệ 2 chiều (vô hướng)
            
        visited = [False] * (n + 1)
        max_group_size = 0
        
        # Duyệt qua từng sinh viên
        for i in range(1, n + 1):
            if not visited[i]:
                # Tìm kích thước của nhóm bạn chứa sinh viên i
                current_size = bfs_count_group(i, adj, visited)
                max_group_size = max(max_group_size, current_size)
                
        print(max_group_size)

if __name__ == "__main__":
    solve()