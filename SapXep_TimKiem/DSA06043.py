#tìm điểm cân bằng sao cho tổng trái = tổng phải 
def diemcanbang(a):
    n=len(a)
    total = sum(a)
    tong_trai = 0 
    for i in range(n):
        tong_phai = total-tong_trai-a[i]
        if tong_phai == tong_trai:
            return i+1 
        tong_trai += a[i] #cập nhật cho vòng for tiếp theo 
    return -1 
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int ,input().split()))
    print(diemcanbang(a))