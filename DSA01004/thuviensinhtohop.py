#sinh tổ hơp chập k của n 
import itertools
t=int(input())
for _ in range(t): 
    n,k= list(map(int , input().split()))
    # Tạo một mảng rỗng để gom tất cả các kết quả của bộ test này
    res = []
    tat_ca_cau_hinh = itertools.combinations(range(1 , n+1) , r = k )
    for cau_hinh in tat_ca_cau_hinh: 
        #để biến (1,2,3) => "123"
        chuoi_lien_nhau = ''.join(map(str , cau_hinh))
        res.append(chuoi_lien_nhau) # res= ['123' , '124',...]
    # Sau khi vòng for trên chạy xong xuôi (gom hết cấu hình vào mảng res),
    # ta mới nối các phần tử trong res lại bằng dấu cách và in ra 1 lần duy nhất.
    # Lệnh print này mặc định sẽ tự Enter xuống dòng để chuẩn bị cho bộ test sau!
    print(*res) #hoặc là print(" ".join(res)) nhưng res phải toàn chứa string

