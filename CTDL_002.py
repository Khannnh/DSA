#bài mà dãy con có tổng bằng k gì gì đó :))) 
import itertools

# Đọc dữ liệu đầu vào
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Sắp xếp mảng A tăng dần để kết quả sinh ra đúng thứ tự từ điển
a.sort()

# Sinh toàn bộ xâu nhị phân độ dài N theo thứ tự giảm dần từ điển
# Ưu tiên số 1 đứng trước số 0 để bốc các phần tử nhỏ trước
cac_cau_hinh = itertools.product([1, 0], repeat=n)

dem_day_con = 0

for cau_hinh in cac_cau_hinh:
    day_con_hien_tai = []
    tong_hien_tai = 0
    
    # Duyệt qua từng phần tử để kiểm tra xem có được chọn không
    for i in range(n):
        if cau_hinh[i] == 1:
            day_con_hien_tai.append(a[i])
            tong_hien_tai += a[i]
            
    # Nếu tổng bằng K thì in ra và tăng biến đếm
    if tong_hien_tai == k:
        print(*day_con_hien_tai)
        dem_day_con += 1

# Dòng cuối cùng in ra tổng số dãy con tìm được
print(dem_day_con)