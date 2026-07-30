import sys

def solve():
    # Đọc tất cả các số nguyên trong input vào một list duy nhất
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Con trỏ duyệt qua các phần tử của input_data
    iterator = iter(input_data)
    
    # Đọc số lượng bộ test T
    t = int(next(iterator))
    
    for _ in range(t):
        so_dinh = int(next(iterator))
        so_canh = int(next(iterator))
        
        # Khởi tạo danh sách kề (1-indexed)
        adj = [[] for _ in range(so_dinh + 1)]
        
        # Đọc so_canh cặp (u, v)
        for _ in range(so_canh):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)  # Đồ thị vô hướng
            
        # Sắp xếp và in kết quả
        for x in range(1, so_dinh + 1):
            adj[x].sort()
            print(f"{x}:", *adj[x])

if __name__ == '__main__':
    solve()