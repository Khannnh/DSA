#viết thuật toán duyệt theo chiều sâu bắt đầu từ 1 đỉnh 
#u là đỉnh bắt đầu duyệt 
def dfs(u:int, adj:list, visited:list, result:list):
    visited[u] = True
    result.append(u)
    
    for v in adj[u]:
        if not visited[v]:
            dfs(v, adj, visited, result)

def solve():
    # Đọc số lượng testcase
    t = int(input())
    
    for _ in range(t):
        # Đọc |V|, |E|, u
        v_num, e_num, start = map(int, input().split())
        
        # Tạo danh sách kề cho đồ thị
        adj = [[] for _ in range(v_num + 1)]
        
        # Đọc toàn bộ các cạnh trong 1 dòng
        edges = list(map(int, input().split()))
        for i in range(0, len(edges), 2):
            u_edge = edges[i]
            v_edge = edges[i + 1]
            adj[u_edge].append(v_edge) # Đồ thị có hướng: u -> v
            
        visited = [False] * (v_num + 1)
        result = []
        
        # Thực hiện DFS từ đỉnh start
        dfs(start, adj, visited, result)
        
        # In kết quả
        print(*result)

if __name__ == "__main__":
    solve()