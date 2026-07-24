# Đọc số đỉnh n
n = int(input())

# Khởi tạo ma trận kề n x n toàn số 0
adj_matrix = [[0]*n for _ in range(n)]

# Đọc danh sách kề cho từng đỉnh từ 1 đến n
for i in range(n):
    line = input().strip()
    if line:  # Tránh lỗi nếu dòng bị trống (đỉnh cô lập)
        neighbors = list(map(int, line.split()))
        for v in neighbors:
            adj_matrix[i][v - 1] = 1

# In ma trận kề
for row in adj_matrix:
    print(*row)