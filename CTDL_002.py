import itertools

# 1. Đọc dữ liệu đầu vào
n, k = map(int, input().split())
a = list(map(int, input().split()))

cac_day_con_thoa_man = []

# 2. Sinh cấu hình nhị phân tăng dần
for cau_hinh in itertools.product([0, 1], repeat=n):
    tong_hien_tai = 0
    
    # Tối ưu: Dùng biến cộng dồn trực tiếp thay vì dùng hàm sum() 
    for i in range(n):
        if cau_hinh[i] == 1:
            tong_hien_tai += a[i]
            
    # Chỉ khi nào TỔNG THỎA MÃN thì mới tốn chi phí tạo mảng và ép chuỗi
    if tong_hien_tai == k:
        day_con = [a[i] for i in range(n) if cau_hinh[i] == 1]
        cac_day_con_thoa_man.append(" ".join(map(str, day_con)))

# 3. In kết quả 1 lần duy nhất bằng \n để tối ưu I/O
print("\n".join(cac_day_con_thoa_man))
print(len(cac_day_con_thoa_man))