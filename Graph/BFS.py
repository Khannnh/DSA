from collections import deque

def bfs(start_node, adj, v_count):
    visited = [False] * (v_count + 1)
    result = []
    
    # Hàng đợi để quản lý các đỉnh sẽ duyệt
    queue = deque([start_node])
    visited[start_node] = True
    
    while queue:
        u = queue.popleft() # Lấy đỉnh ở đầu hàng đợi ra
        result.append(u)
        
        # Duyệt các đỉnh kề v của u
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v) # Cho đỉnh kề chưa thăm vào cuối hàng đợi
    return result

def solve():
    # Nhập số lượng bộ test
    t_str = input().strip()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        # Nhập V, E, u trên cùng 1 dòng
        line1 = input().split()
        if not line1: continue
        v_num, e_num, start = map(int, line1)
        
        # Nhập toàn bộ danh sách các cạnh trên dòng tiếp theo
        edge_list = list(map(int, input().split()))
        
        # Khởi tạo danh sách kề
        adj = [[] for _ in range(v_num + 1)]
        
        # Đọc từng cặp (u, v) từ danh sách cạnh đã nhập
        for i in range(0, len(edge_list), 2):
            u_edge = edge_list[i]
            v_edge = edge_list[i+1]
            adj[u_edge].append(v_edge) # Đồ thị có hướng
            
        # Gọi hàm BFS và in kết quả
        res = bfs(start, adj, v_num)
        print(*(res))

if __name__ == "__main__":
    solve()