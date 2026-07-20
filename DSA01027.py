
def hoan_vi_day_so(n, dayso):
    # mảng a lưu cấu hình hoán vị hiện tại gồm n phần tử (Java: int[] a = new int[n])
    a = [0] * n 
    # mảng visited để đánh dấu phần tử tại index j đã được chọn chưa
    visited = [False] * n 
    res = []

    def backtrack(i):
        # Base case: Khi đã điền đủ n vị trí cho hoán vị (Java: if (i == n))
        if i == n:
            res.append(" ".join(map(str, a)))
            return
            
        # Duyệt qua từng phần tử trong dãy số đã sắp xếp
        for j in range(n):
            if not visited[j]:
                a[i] = dayso[j]     # Điền giá trị thực tế vào vị trí i
                visited[j] = True   # Đánh dấu đã dùng phần tử tại index j
                
                backtrack(i + 1)    # Gọi đệ quy điền vị trí tiếp theo
                
                visited[j] = False  # Khôi phục trạng thái (Backtrack)
                
    backtrack(0)
    return res

# --- Luồng xử lý chính ---
n = int(input())
dayso = list(map(int, input().split()))

# Bắt buộc phải sort mảng gốc để backtrack tự sinh theo đúng thứ tự từ điển
dayso.sort()

ket_qua = hoan_vi_day_so(n, dayso)
# Xả hàng một phát bằng \n để tối ưu tốc độ in
print("\n".join(ket_qua))

# #hoán vị dãy số 
# import itertools 
# n= int(input())
# dayso = list(map(int,input().split()))
# dayso.sort()
# cac_hv = itertools.permutations(dayso)
# for hv in cac_hv:
#     s=' '.join(map(str,hv))
#     print(s)