import sys

# Tăng giới hạn đệ quy phòng xa
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    t = int(next(iterator))
    
    for _ in range(t):
        n = int(next(iterator))
        k = int(next(iterator))
        
        a = [int(next(iterator)) for _ in range(n)]
        # Sắp xếp mảng tăng dần để đảm bảo thứ tự từ điển chuẩn
        a.sort()
        
        cac_day_con_thoa_man = []
        
        # Hàm quay lui tìm các tập hợp con
        def backtrack(index, current_sum, current_list):
            # Nhánh cận: Nếu tổng hiện tại vượt quá K thì dừng (vì mảng toàn số nguyên dương)
            if current_sum > k:
                return
            
            # Khi đã duyệt hết phần tử của mảng
            if index == n:
                if current_sum == k:
                    # Định dạng chuỗi [a1 a2 ... an]
                    chuoi_dinh_dang = "[" + " ".join(map(str, current_list)) + "]"
                    cac_day_con_thoa_man.append(chuoi_dinh_dang)
                return

            # Để chuẩn thứ tự từ điển: Ưu tiên CHỌN phần tử nhỏ đứng trước
            backtrack(index + 1, current_sum + a[index], current_list + [a[index]])
            
            # Sau đó mới đến nhánh KHÔNG CHỌN phần tử đó
            backtrack(index + 1, current_sum, current_list)

        # Chạy quay lui bắt đầu từ phần tử đầu tiên (index = 0)
        backtrack(0, 0, [])
        
        if not cac_day_con_thoa_man:
            print("-1")
        else:
            # Nối các dãy con lại bằng một dấu cách và in trên cùng một dòng
            print(" ".join(cac_day_con_thoa_man))

if __name__ == '__main__':
    solve()