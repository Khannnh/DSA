import itertools 

# Sàng số nguyên tố lên tới limit
def sangnguyento(limit): 
    sang = [True] * (limit + 1)
    sang[0] = sang[1] = False 
    for i in range(2, int(limit**0.5) + 1): 
        if sang[i] == True: 
            for j in range(i * i, limit + 1, i): 
                sang[j] = False
    return sang

# Khởi tạo sẵn bảng sàng số nguyên tố
SANG = sangnguyento(1500)

def daycon_tong_nguyento(a):
    n = len(a)
    res = []
    
    # Sinh tất cả các xâu nhị phân độ dài n
    cac_xau_nhi_phan = itertools.product([0, 1], repeat=n)
    
    for xau in cac_xau_nhi_phan: 
        temp = []
        total_sum = 0
        
        for i in range(n): 
            if xau[i] == 1: 
                temp.append(a[i])
                total_sum += a[i]
        
        # Kiểm tra nếu tổng là số nguyên tố và dãy con không rỗng
        if len(temp) > 0 and SANG[total_sum]: 
            res.append(temp)
            
    # Sắp xếp các dãy con thu được theo thứ tự từ điển tăng dần
    res.sort()
    
    # Chuyển đổi sang dạng chuỗi để in ra
    string_results = []
    for subseq in res:
        string_results.append(" ".join(map(str, subseq)))
        
    return string_results 

# Đọc số bộ test
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # BẮT BUỘC: Sắp xếp giảm dần mảng ban đầu thì mới ra đúng thứ tự dãy con của ví dụ
    a.sort(reverse=True)
    
    result = daycon_tong_nguyento(a)
    
    # In kết quả
    print('\n'.join(result))