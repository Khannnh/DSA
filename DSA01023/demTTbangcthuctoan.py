# thực sự đọc ko hiểu lắm :)))))
import math
# Hàm tính tổ hợp chập k của n: C(n, k)
def comb(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

def get_combination_index(n, k, x):
    # Thêm số 0 vào đầu mảng để dễ tính toán chỉ số 1-based index
    x = [0] + x 
    idx = 1
    
    for i in range(1, k + 1):
        # j chạy từ giá trị đứng trước + 1 đến giá trị hiện tại - 1
        for j in range(x[i-1] + 1, x[i]):
            # Cộng số lượng cấu hình bị bỏ qua
            idx += comb(n - j, k - i)
            
    return idx

# --- Luồng xử lý chính ---
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cau_hinh = list(map(int, input().split()))
    print(get_combination_index(n, k, cau_hinh))