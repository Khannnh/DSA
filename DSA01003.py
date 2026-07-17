def next_permutation(a, n):
    # Bước 1: Tìm vị trí i đầu tiên từ phải sang sao cho a[i] < a[i+1]
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
        
    # TRƯỜNG HỢP ĐẶC BIỆT: Nếu i < 0, tức là dãy đang giảm dần (cấu hình cuối cùng)
    # Đề bài yêu cầu in ra cấu hình đầu tiên (lật ngược toàn bộ mảng thành tăng dần)
    if i < 0:
        a.reverse()
        return a
        
    # Bước 2: Tìm vị trí j đầu tiên từ phải sang sao cho a[j] > a[i]
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
        
    # Bước 3: Đổi chỗ (swap) a[i] và a[j]
    a[i], a[j] = a[j], a[i]
    
    # Bước 4: Lật ngược (reverse) đoạn từ i + 1 đến hết dãy
    a[i + 1:] = a[i + 1:][::-1]
    
    return a

# --- XỬ LÝ NHẬP XUẤT PHÙ HỢP VỚI HỆ THỐNG CHẤM BÀI ---
if __name__ == "__main__":
    # Đọc số lượng bộ test T
    t = int(input())
    
    for _ in range(t):
        # Đọc số lượng phần tử N của bộ test hiện tại
        n = int(input())
        
        # Đọc dãy hoán vị X[], chuyển thành list các số nguyên
        a = list(map(int, input().split()))
        
        # Tìm hoán vị kế tiếp
        res = next_permutation(a, n)
        
        # In kết quả trên một dòng, các phần tử cách nhau khoảng trắng
        print(*(res))